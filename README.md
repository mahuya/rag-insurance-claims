# RAG Travel Insurance Copilot  

**Multilingual • Multi-format • Built with Langflow + AstraDB**  

An Agentic **Retrieval-Augmented Generation (RAG) workflow** designed as a travel insurance copilot.  
It ingests policies, forms, tables, and certificates across **multiple formats** (PDF, CSV, DOCX, TXT) and supports **multiple languages** (French, German, Spanish, Hindi). The system then delivers clear **answers in English with trusted citations**, making insurance claims faster, transparent, and easier to process.  

---

## Features
- Multilingual document support (FR, DE, ES, HI)
- Multi-format ingestion (PDF, CSV, DOCX, TXT)
- Vector storage in **Astra DB** with 768-dim multilingual embeddings
- Built entirely with **Langflow** (free hosted version works)
- Safe answers: responds **“Unclear”** if no evidence is found
- Includes sample data for quick testing

---

## Demo Video
[![Watch the demo](https://img.youtube.com/vi/Fd3-hpZlfPA/hqdefault.jpg)](https://youtu.be/Fd3-hpZlfPA)

👉 Click the thumbnail to watch the full walkthrough on YouTube.

---

## Solution Diagram
![Solution Architecture](https://drive.google.com/uc?id=1s7pSAG5zpezN0FSWHz6pYUkHmrwSFKko)
*(Diagram showing ingestion → vector storage in AstraDB → Langflow orchestration → RAG responses with citations.)*

---

## Repo Structure
```
rag-insurance-claims/
├─ README.md
├─ LICENSE
├─ gitignore
├─ env.example
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ flows/   # Langflow JSON exports
├─ data/    # Sample docs (PDF, CSV, DOCX, TXT)
└─ scripts/ # AstraDB helper scripts
```

---

## Quickstart
Full setup instructions will follow (Python, Docker, Astra DB).  
For now, clone the repo and explore the flow in `/flows`.

---

## License
MIT — free to use, modify, and share.
