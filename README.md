# AGENTICBATCH2

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Repo-success)

Hands-on notebooks and practice material for **LangChain**, **LangGraph**, **RAG**, vector databases, and agentic AI workflows.

## Table of Contents

- [Repository Overview](#repository-overview)
- [Quick Start](#quick-start)
- [Notebook Index](#notebook-index)
- [Requirements Files](#requirements-files)
- [Notes](#notes)
- [License](#license)

## Repository Overview

- `1-Pydantic/` — Pydantic basics and validation notebooks.
- `2-Langchain Basics/` — LangChain fundamentals, ingestion, and transformation examples.
- `2.3-Embeddings/` — Embeddings with different providers/models.
- `2.4-VectorDatabase/` — FAISS and Pinecone notebook examples.
- `Agentic-2.0-main/` — Extended assignments and agentic workflow material.
- `data/`, `data2/` — Local text resources used by notebooks.
- `requirements*.txt` — dependency sets for different sessions/modules.

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/nitinchaurey8/AGENTICBATCH2.git
cd AGENTICBATCH2
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies (start with base):

```bash
pip install -r requirements.txt
```

4. Open notebooks in VS Code or Jupyter and run cells in order.

## Notebook Index

- Core LangGraph assignment:
  - `Agentic-2.0-main/langgraph/langgraph_class_2 assign.ipynb`
- LangGraph series:
  - `Agentic-2.0-main/langgraph/langgraph_class_3.ipynb`
  - `Agentic-2.0-main/langgraph/langgraph_class_4.ipynb`
  - `Agentic-2.0-main/langgraph/langgraph_class_5.ipynb`
  - `Agentic-2.0-main/langgraph/langgraph_class_6_multiagent.ipynb`
  - `Agentic-2.0-main/langgraph/langgraph_class_7_supervisor_multiagent.ipynb`
  - `Agentic-2.0-main/langgraph/langgraph_class_8_humaninloop.ipynb`
- LangChain basics:
  - `2-Langchain Basics/gettingstartedlangchain.ipynb`
  - `2-Langchain Basics/2.1-DataIngestion/dataingestion.ipynb`
  - `2-Langchain Basics/2.2-DataTransformer/2.2.1-Recursivetextsplitter.ipynb`
- Vector DB examples:
  - `2.4-VectorDatabase/FAISS/code.ipynb`
  - `2.4-VectorDatabase/Pinecone/code.ipynb`

## Requirements Files

Use the file that matches your notebook/module context:

- `requirements.txt` (base)
- `requirements_lg.txt` (LangGraph-focused)
- `requirements_lc.txt` (LangChain-focused)
- `requirements_rg.txt` (RAG-focused)
- `requirements_py.txt` (Python utilities)

## Notes

- Some notebooks require API keys (for example, LLM providers).
- Some workflows require internet access (for web tools/search).
- Vector DB notebooks may create local index artifacts (for example FAISS index files).

## License

This repository is intended for educational and practice use.
