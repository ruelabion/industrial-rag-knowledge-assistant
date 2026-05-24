# Industrial RAG Knowledge Assistant

Public showcase repository for an Industrial Retrieval-Augmented Generation (RAG) Knowledge Assistant designed for technical businesses, industrial support teams, and AI knowledge systems portfolios.

This repo is intentionally simplified for public presentation. It demonstrates the architecture, ingestion flow, chunking strategy, vector search patterns, citation-based responses, and a minimal FastAPI interface without exposing production secrets, client data, proprietary prompts, or internal deployment details.

## What This Showcase Covers

- Architecture for document ingestion, normalization, chunking, embedding, vector indexing, retrieval, and answer generation
- Sample ingestion artifacts for industrial manuals and troubleshooting content
- Example chunking output with metadata and citation anchors
- Example vector search results and answer assembly patterns
- Simplified FastAPI endpoints for ingestion status, search, and Q&A
- Docker Compose example for local development
- AWS deployment overview for a production-style topology
- Sample citation-based answer examples for industrial support use cases

## Portfolio Positioning

This project is positioned as a portfolio artifact for:

- AI Knowledge Systems
- Retrieval-Augmented Generation for technical businesses
- AI-enabled industrial support systems
- Internal knowledge assistants for operations, maintenance, and field service

## Repository Structure

```text
.
├── api/
│   └── simplified-fastapi-example/
├── docs/
│   ├── architecture.md
│   ├── aws-deployment-overview.md
│   └── sample-queries.md
├── examples/
│   ├── sample-chunking/
│   ├── sample-ingestion/
│   └── sample-vector-search/
├── docker-compose.yml
└── .env.example
```

## Solution Overview

This showcase models a typical industrial RAG pipeline:

1. Source documents are ingested from manuals, SOPs, troubleshooting guides, and knowledge articles.
2. Files are normalized into structured text plus metadata.
3. Content is chunked into retrieval-friendly sections with source anchors.
4. Chunks are embedded and stored in a vector index.
5. User questions are matched against relevant chunks.
6. Retrieved passages are passed to an LLM for grounded answer generation.
7. Answers are returned with citations so operators can verify the source.

## Example Use Cases

- Troubleshooting industrial equipment alarms
- Locating maintenance procedures in technical manuals
- Answering field-service questions with source citations
- Summarizing safety or operational guidance from internal documents
- Supporting customer success teams serving industrial clients

## Public-Safe Scope

Included:

- Sample files and fabricated industrial-style content
- Simplified API example
- Illustrative architecture and deployment documentation
- Non-sensitive environment template

Excluded:

- Production API keys or AWS credentials
- Real customer or plant data
- Proprietary prompts or internal chain logic
- Full production ingestion and orchestration code
- Private dashboards or client-specific integrations

## Local Demo

1. Copy `.env.example` to `.env`.
2. Review the simplified API in [api/simplified-fastapi-example/main.py](/Users/ruelabion/Sites/Lightsail_RAGApp/industrial-rag-knowledge-assistant/api/simplified-fastapi-example/main.py).
3. Start the demo stack:

```bash
docker compose up --build
```

4. Open the FastAPI docs at `http://localhost:8000/docs`.

## Screenshots

This repository includes a placeholder location for screenshots from the existing SpiceWorx AI Systems demo:

- `docs/screenshots/ai-systems-demo-home.png`
- `docs/screenshots/ai-systems-demo-chat.png`
- `docs/screenshots/ai-systems-demo-citations.png`
- `docs/screenshots/ai-systems-demo-mobile.png`

Suggested captures from the current public demo at `https://www.spiceworx.com/en/service_ai-systems.html`:

- Landing section introducing the AI Knowledge Systems offering
- Demo chat interface in use
- Citation-style answer or retrieved context example
- Mobile view of the demo experience

Optional supporting images:

- `docs/screenshots/aws-architecture-placeholder.png`
- Architecture diagram or AWS deployment overview slide

To automate screenshot generation locally, use the Playwright instructions in [docs/screenshots/capture-instructions.md](/Users/ruelabion/Sites/Lightsail_RAGApp/industrial-rag-knowledge-assistant/docs/screenshots/capture-instructions.md).

## Key Design Principles

- Grounded responses over free-form generation
- Traceable citations for operator trust
- Metadata-aware chunking for better retrieval
- Public-safe documentation and examples
- Clear separation between showcase code and production logic

## Related Documentation

- [Architecture](./docs/architecture.md)
- [AWS Deployment Overview](./docs/aws-deployment-overview.md)
- [Sample Queries](./docs/sample-queries.md)

## Notes

This repository is a showcase, not a full production distribution. The included examples are designed to communicate system thinking, implementation approach, and RAG patterns suitable for industrial knowledge applications.
