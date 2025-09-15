
"""
Helper script to create (or verify) an Astra DB vector collection
for the ClaimPilot RAG demo.

Reads config from environment variables (see .env.example).

Required env vars:
  - ASTRA_DB_API_ENDPOINT
  - ASTRA_DB_APPLICATION_TOKEN
  - ASTRA_DB_DATABASE          (namespace/keyspace, e.g., "langflow")
  - ASTRA_DB_COLLECTION        (e.g., "MultiLingual2")

Embedding dimension is set to 768 for Google text-embedding-004.
"""
import os
from astrapy.db import AstraDB

EMBEDDING_DIMS = 768

def main():
    api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
    token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    namespace = os.getenv("ASTRA_DB_DATABASE", "langflow")
    collection = os.getenv("ASTRA_DB_COLLECTION", "MultiLingual2")

    if not api_endpoint or not token:
        raise SystemExit("Please set ASTRA_DB_API_ENDPOINT and ASTRA_DB_APPLICATION_TOKEN in your environment (.env)")

    print(f"Connecting to Astra DB @ {api_endpoint}, namespace={namespace}")
    db = AstraDB(token=token, api_endpoint=api_endpoint, namespace=namespace)

    # Check existing collections
    try:
        existing_collections = db.get_collections().get("data", {}).get("collections", [])
        existing = [c.get("name") for c in existing_collections]
    except Exception as e:
        raise SystemExit(f"Failed to list collections: {e}")

    if collection in existing:
        print(f"Collection '{collection}' already exists ✓")
        return

    # Create collection
    print(f"Creating collection '{collection}' with dim={EMBEDDING_DIMS} (metric=cosine) ...")
    try:
        db.create_collection(
            collection,
            dimension=EMBEDDING_DIMS,
            metric="cosine",
            indexing={"allow": ["$vector", "text", "metadata.file", "metadata.section", "metadata.lang"]},
        )
    except Exception as e:
        raise SystemExit(f"Create collection failed: {e}")

    print(f"Collection '{collection}' created ✓")

if __name__ == "__main__":
    main()
