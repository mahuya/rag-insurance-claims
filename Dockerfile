FROM python:3.11-slim

WORKDIR /app

# Install system deps for OCR/PDF handling (optional but useful for Unstructured loader)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the repo content (flows & data can be mounted via compose as volumes)
COPY . .

EXPOSE 7860
CMD ["bash", "-lc", "langflow run --host 0.0.0.0 --port ${LANGFLOW_PORT:-7860}"]
