from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Industrial RAG Knowledge Assistant Demo API",
    description="Public-safe simplified API for an industrial RAG portfolio project.",
    version="0.1.0",
)


DEMO_CHUNKS = [
    {
        "chunk_id": "chunk-xr500-001",
        "text": (
            "If alarm E-214 is present, inspect the lubrication oil level before "
            "restart. Confirm the lubrication pump is energized and delivering flow."
        ),
        "citation": "compressor-maintenance-manual-v3.pdf, Section 4.2, Page 18",
        "tags": ["compressor", "alarm", "lubrication"],
    },
    {
        "chunk_id": "chunk-xr500-002",
        "text": (
            "If pressure remains below threshold for more than 15 seconds, inspect "
            "the inlet filter and pressure sensor wiring. Do not continue "
            "operation until nominal pressure is restored."
        ),
        "citation": "compressor-maintenance-manual-v3.pdf, Section 4.2, Page 18",
        "tags": ["pressure", "sensor", "safety"],
    },
    {
        "chunk_id": "chunk-fsg-021",
        "text": (
            "Low lubrication pressure alarms should be checked against oil level, "
            "pump status, and filter restriction before equipment restart."
        ),
        "citation": "field-service-troubleshooting-guide.pdf, Section 2.1, Page 7",
        "tags": ["troubleshooting", "alarm", "filter"],
    },
]


class SearchRequest(BaseModel):
    query: str
    top_k: int = 3
    equipment_model: Optional[str] = None


class SearchResult(BaseModel):
    chunk_id: str
    score: float
    text: str
    citation: str


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    citations: List[str]
    grounded: bool


def score_chunk(query: str, chunk_text: str) -> float:
    query_terms = {term.lower() for term in query.split() if term.strip()}
    chunk_terms = {term.lower().strip(".,") for term in chunk_text.split()}
    if not query_terms:
        return 0.0
    overlap = len(query_terms & chunk_terms)
    return round(overlap / len(query_terms), 3)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "industrial-rag-demo-api"}


@app.get("/ingestion/status")
def ingestion_status() -> dict:
    return {
        "pipeline": "demo",
        "documents_indexed": 1,
        "chunks_available": len(DEMO_CHUNKS),
        "last_ingestion_status": "completed",
    }


@app.post("/search", response_model=List[SearchResult])
def search(request: SearchRequest) -> List[SearchResult]:
    ranked = []
    for chunk in DEMO_CHUNKS:
        score = score_chunk(request.query, chunk["text"])
        ranked.append(
            SearchResult(
                chunk_id=chunk["chunk_id"],
                score=score,
                text=chunk["text"],
                citation=chunk["citation"],
            )
        )

    ranked.sort(key=lambda item: item.score, reverse=True)
    return ranked[: request.top_k]


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    results = search(SearchRequest(query=request.question, top_k=2))
    supported_results = [result for result in results if result.score > 0]

    if not supported_results:
        return AskResponse(
            answer=(
                "I could not find enough supporting context in the demo knowledge "
                "base to answer that safely."
            ),
            citations=[],
            grounded=False,
        )

    answer = (
        "Based on the retrieved maintenance guidance, the first check is the "
        "lubrication oil level, then confirmation that the lubrication pump is "
        "active and delivering flow."
    )
    citations = [result.citation for result in supported_results]
    return AskResponse(answer=answer, citations=citations, grounded=True)
