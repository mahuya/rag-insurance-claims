# ClaimPilot — RAG Travel Insurance Copilot

**Multilingual • Multi-format • Powered by Langflow + AstraDB**

ClaimPilot is a Retrieval-Augmented Generation (RAG) demo that acts as a **travel insurance copilot**.  
It can read policies, forms, tables, and certificates in **different formats** (PDF, CSV, DOCX, TXT) and **multiple languages** (French, German, Spanish, Hindi), then answer questions in **English with citations**.

---

## Features
- Multilingual document support (FR, DE, ES, HI)
- Multi-format ingestion (PDF, CSV, DOCX, TXT)
- Vector storage in **Astra DB** with 768-dim multilingual embeddings
- Built entirely with **Langflow** (free hosted version works)
- Safe answers: responds **“Unclear”** if no evidence is found
- Includes sample data for quick testing

---

## Solution Diagram
![Solution Architecture](https://drive.google.com/uc?id=1s7pSAG5zpezN0FSWHz6pYUkHmrwSFKko)
*(Diagram showing ingestion → vector storage in AstraDB → Langflow orchestration → RAG responses with citations.)*

---

## Repo Structure
```
claimpilot-rag/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ .env.example
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ flows/   # Langflow JSON exports
├─ data/    # Sample docs (PDF, CSV, DOCX, TXT)
└─ scripts/ # Optional Astra helper scripts
```

---

## Quickstart
Full setup instructions will follow (Python, Docker, Astra DB).  
For now, clone the repo and explore the flow in `/flows`.

---

## License
MIT — free to use, modify, and share.
