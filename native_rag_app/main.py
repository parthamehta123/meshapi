"""HTML page plus JSON routes for the MeshAPI RAG demo."""

from pathlib import Path

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import meshapi_client, rag
from .config import settings
from .schemas import AskRequest, AskResponse, IngestResponse, VoiceAskResponse

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Harbor Desk Support")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def _reject_if_flagged(question: str) -> None:
    if meshapi_client.is_flagged(question):
        raise HTTPException(400, "That question was flagged by content moderation -- try rephrasing.")


@app.on_event("startup")
def on_startup() -> None:
    settings.validate()


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html", {})


@app.post("/api/ingest", response_model=IngestResponse)
def api_ingest() -> IngestResponse:
    uploaded, ready = rag.ingest()
    return IngestResponse(documents_uploaded=uploaded, embedded_ready=ready)


@app.post("/api/ask", response_model=AskResponse)
def api_ask(req: AskRequest) -> AskResponse:
    _reject_if_flagged(req.question)
    answer_text, sources = rag.answer(req.question, top_k=req.top_k)
    audio_b64 = meshapi_client.synthesize_base64(answer_text) if req.speak else None
    return AskResponse(answer=answer_text, sources=sources, audio_base64=audio_b64)


@app.post("/api/ask-voice", response_model=VoiceAskResponse)
async def api_ask_voice(audio: UploadFile = File(...)) -> VoiceAskResponse:
    audio_bytes = await audio.read()
    question = meshapi_client.transcribe(audio_bytes, filename=audio.filename or "recording.webm")
    if not question.strip():
        raise HTTPException(400, "Could not make out any speech in that recording -- try again.")
    _reject_if_flagged(question)
    answer_text, sources = rag.answer(question)
    audio_b64 = meshapi_client.synthesize_base64(answer_text)
    return VoiceAskResponse(
        question=question, answer=answer_text, sources=sources, audio_base64=audio_b64
    )
