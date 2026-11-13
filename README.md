# Multi-Agent Wedding Planner

A command-line wedding planning assistant built with LangChain. A main agent coordinates two subagents, which can search the web for relevant information.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- An OpenRouter API key
- A Tavily API key

## Setup

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Install dependencies:

```bash
uv sync
```

## Run

```bash
uv run python main.py
```

Enter your wedding requirements when prompted.
