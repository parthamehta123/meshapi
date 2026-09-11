"""Ingest the sample docs, search them, and answer from retrieved chunks.

The MeshAPI file store is account-wide and has no delete. We persist the
file_ids from our own ingest and pass them on every search so other uploads
on this key do not leak into results.
"""

import json
import time
from pathlib import Path

from . import meshapi_client
from .config import settings
from .data import KNOWLEDGE_BASE

_STATE_FILE = Path(__file__).resolve().parent / ".rag_state.json"


def _save_file_ids(file_ids: list[str]) -> None:
    _STATE_FILE.write_text(json.dumps({"file_ids": file_ids}))


def _load_file_ids() -> list[str] | None:
    if not _STATE_FILE.exists():
        return None
    return json.loads(_STATE_FILE.read_text()).get("file_ids")


def ingest() -> tuple[int, int]:
    file_ids = [
        meshapi_client.upload_document(
            file_name=f"{doc['id']}.txt",
            mime_type="text/plain",
            content=doc["text"].encode("utf-8"),
            metadata={"title": doc["title"], "doc_id": doc["id"]},
        )
        for doc in KNOWLEDGE_BASE
    ]
    _save_file_ids(file_ids)

    pending = set(file_ids)
    for _ in range(20):
        if not pending:
            break
        time.sleep(3)
        pending = {
            fid
            for fid in pending
            if meshapi_client.embedding_status(fid) not in ("ready", "failed")
        }

    return len(file_ids), len(file_ids) - len(pending)


def retrieve(query_text: str, top_k: int | None = None) -> list[dict]:
    top_k = top_k or settings.rag_top_k
    return meshapi_client.search(query_text, top_k, file_ids=_load_file_ids())


def answer(question: str, model: str | None = None, top_k: int | None = None) -> tuple[str, list[dict]]:
    hits = retrieve(question, top_k=top_k)
    context = "\n\n".join(f"[{h['title']}] {h['text']}" for h in hits)
    prompt = f"""Answer the question using ONLY the context below. If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {question}"""
    text = meshapi_client.ask(prompt, model=model, temperature=0.2, max_tokens=400)
    return text, hits
