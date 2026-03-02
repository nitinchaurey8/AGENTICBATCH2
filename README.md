# AGENTICBATCH2

This repository contains hands-on notebooks and practice material for **LangChain**, **LangGraph**, **RAG**, vector databases, and agentic AI workflows.

## Repository Overview

- `1-Pydantic/` — Pydantic basics and validation notebooks.
- `2-Langchain Basics/` — LangChain fundamentals, ingestion, and transformation examples.
- `2.3-Embeddings/` — Embeddings with different providers/models.
- `2.4-VectorDatabase/` — FAISS and Pinecone notebook examples.
- `Agentic-2.0-main/` — Extended assignments and agentic workflow material.
- `data/`, `data2/` — Local text resources used by notebooks.
- Multiple `requirements*.txt` files — dependency sets for different sessions/modules.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/nitinchaurey8/AGENTICBATCH2.git
cd AGENTICBATCH2
```

2. Create and activate a Python environment.

3. Install dependencies (choose the file relevant to your notebook/session):

```bash
pip install -r requirements.txt
```

You may also use module-specific files such as:
- `requirements_lg.txt`
- `requirements_lc.txt`
- `requirements_rg.txt`
- `requirements_py.txt`

4. Open notebooks in VS Code or Jupyter and run cells in order.

## Notes

- Some notebooks require API keys (for example, LLM providers).
- Some workflows require internet access (for web tools/search).
- Vector DB notebooks may create local index artifacts (for example FAISS index files).

## Suggested Entry Points

- LangGraph assignment notebook:
  - `Agentic-2.0-main/langgraph/langgraph_class_2 assign.ipynb`
- LangGraph class notebooks:
  - `Agentic-2.0-main/langgraph/`

## License

This repository is intended for educational and practice use.
