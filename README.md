# MCP Core Components

A small Python project demonstrating three Model Context Protocol (MCP) components with [FastMCP](https://gofastmcp.com/): a tool, a resource, and a prompt. The server uses Streamable HTTP; a separate client connects to it and exercises each component.

## Components

- **Tool: `add`** - Adds two numbers. FastMCP derives its argument schema from the function signature and exposes its name, description, title, tags, and metadata to clients.
- **Resource: `training://slm/recommended-configuration`** - Returns a basic, static JSON recommendation for single-GPU SLM fine-tuning. It is guidance, not a hardware detector or a training script.
- **Prompt: `passport_photo_image_prompt`** - Produces image-generation instructions for a passport-style portrait. It accepts an optional issuing country. The prompt does not create an image; pass its result and a genuine reference photo to an image-generation model separately. Passport authorities may reject AI-generated or edited photos, so check the issuing country's official requirements.

## Requirements

- Python 3.10 or newer
- `pip`

FastMCP is pinned to `4.0.10` in `requirements.txt`.

## Setup on Windows

Run these commands from the project directory in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the Server and Client

Start the server in the first terminal:

```powershell
.\.venv\Scripts\python.exe mcp_server.py
```

The Streamable HTTP MCP endpoint is `http://127.0.0.1:8000/mcp`.

In a second terminal, from the same project directory, run the client:

```powershell
.\.venv\Scripts\python.exe app.py
```

The client lists available tools, calls `add` with sample values, reads and prints the SLM configuration resource, and requests and prints the passport-photo prompt. Keep the server running while the client connects; stop it with `Ctrl+C` when finished.

## Use with Another MCP Client

Connect to `http://127.0.0.1:8000/mcp` using an MCP client that supports Streamable HTTP. The client can discover and call the `add` tool, read the SLM resource, and request the `passport_photo_image_prompt` prompt. When requesting the prompt, `issuing_country` is optional; for example, provide `United States` to include that country's official photo requirements in the generated instructions.

## Project Files

- `mcp_server.py` - FastMCP server and component definitions.
- `app.py` - Example MCP client.
- `requirements.txt` - Python dependency pin.
