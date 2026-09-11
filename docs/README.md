# Documentation

Read these in order.

```mermaid
flowchart LR
    A["01 + 02\nwhat MeshAPI offers"] --> B["03 + 04 + 05\nCLI, MCP, Claude Code"] --> C["06\nthe RAG app"]
```

| # | File | What it covers |
|---|------|----------------|
| 01 | [`01_research.md`](01_research.md) | Feature inventory, checked live against docs and a real key |
| 02 | [`02_features.md`](02_features.md) | Walkthrough of `features.ipynb` without opening Jupyter |
| 03 | [`03_cli_and_claude_code.md`](03_cli_and_claude_code.md) | `meshapi-code` CLI vs MeshAPI as an MCP tool |
| 04 | [`04_mcp_capabilities.md`](04_mcp_capabilities.md) | What MCP can and cannot do |
| 05 | [`05_meshapi_vs_claude_code.md`](05_meshapi_vs_claude_code.md) | `meshapi-code` vs Claude Code as products |
| 06 | [`06_native_rag_app.md`](06_native_rag_app.md) | The FastAPI RAG app: architecture, env, endpoints, the account-wide store gotcha |
