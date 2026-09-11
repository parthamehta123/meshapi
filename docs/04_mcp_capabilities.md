# meshapi-code vs MCP: what each can do

Same MeshAPI account, opposite shapes.

```mermaid
flowchart TB
    subgraph one["meshapi-code — a whole agent"]
        You1["you"] --> Mesh["meshapi CLI"]
    end
    subgraph two["MCP — extra tools for Cursor / Claude Code"]
        You2["you"] --> Agent["editor agent"]
        Agent -->|"one tool call"| Mesh2["MeshAPI"]
    end
```

- **`meshapi-code`** is a full coding agent. You open it instead of Cursor/Claude Code.
- **MCP** does not replace the editor. The agent you already have can call MeshAPI for one job and keep going.

| | `meshapi-code` CLI | MCP |
|---|---|---|
| Chat | ✅ | ✅ `chat` |
| Read / edit project files | ✅ | ✅ (the editor already does this) |
| Run shell commands | ✅ | ✅ (the editor already does this) |
| Switch MeshAPI models | ✅ `/model` | ✅ per `chat` / `compare` call |
| Generate / edit an image | ❌ | ✅ |
| Search uploaded docs (RAG) | ❌ | ✅ `file_search`, `upload_file` |
| Check balance | ❌ | ✅ `get_balance` |
| TTS / STT | ❌ | ❌ |
| Video | ❌ | ❌ |

Audio and video are missing from both. Use the Python SDK (`features.ipynb` or a small script).

```mermaid
flowchart TD
    Q1{"Already in Cursor / Claude Code?"}
    Q1 -->|yes| Q2{"Need something only MeshAPI has?"}
    Q2 -->|yes| A1["Use the MCP tool in this chat"]
    Q2 -->|no| A2["Stay put"]
    Q1 -->|no| Q3{"Want a full session on a MeshAPI model?"}
    Q3 -->|yes| A3["Run meshapi in a terminal"]
    Q3 -->|audio/video| A4["Use the Python SDK"]
```

## Confirmed missing from MCP

- Audio (TTS / STT)
- Video generation
- Batch API
- Realtime voice

Working fallback: `client.audio.synthesize(...)`, `client.videos.generate(...)`.

## What MCP does cover

**Text** — `chat`, `compare`, `responses`, `router_select`

**Images** — `generate_image`, `edit_image` (image comes back as inline base64, even if you ask for a URL)

**Docs** — `upload_file`, `list_files`, `get_file`, `file_search`

**Other** — `embeddings`, `moderations`, `list_models`, `list_voices`, template CRUD, `get_balance`

Quirk: the bytes MeshAPI returns for audio may not match the filename suffix. Check the header (`RIFF` = WAV, `ID3` = MP3) before trusting `.mp3` / `.wav`.

See [`03_cli_and_claude_code.md`](03_cli_and_claude_code.md) for setup and [`01_research.md`](01_research.md) for the full feature list.
