from ingest import load_and_chunk
from vector_store import VectorStore
from orchestrator import AgentOrchestrator

PDF_PATH = "data/aws_rag_guide.pdf"

chunks = load_and_chunk(PDF_PATH)

vs = VectorStore()
vs.build(chunks)

agentic_rag = AgentOrchestrator(vs)

while True:
    query = input("\nAsk a question (or type exit): ")
    if query.lower() == "exit":
        break
    print(agentic_rag.run(query))