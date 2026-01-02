Agentic RAG Assistant on AWS

This project implements an Agentic Retrieval-Augmented Generation (RAG) assistant grounded strictly in the AWS Prescriptive Guidance document titled “Retrieval Augmented Generation options and architectures on AWS”. The system answers complex questions by combining semantic document retrieval with language-model-based answer synthesis while ensuring that responses are derived only from the provided document and never hallucinated.

The solution follows a complete RAG pipeline including PDF ingestion, semantic chunking with metadata preservation, vector embedding and indexing, similarity-based retrieval, and grounded answer synthesis. An agentic architecture is implemented in which multiple agents collaborate to answer user queries. The Planner agent analyzes the query intent and determines the appropriate retrieval strategy. The Retriever agent performs vector similarity search over indexed document chunks and returns the most relevant passages. The Synthesizer agent combines the retrieved passages into a coherent, structured answer and explicitly states when the document does not contain sufficient information.

The application is implemented as a command-line interface (CLI). Users interact with the system through the terminal by running the application and typing questions directly. All processing is performed locally. No external APIs, cloud services, or API keys are required.

Technical stack used in the current implementation includes Python 3.10.x, LangChain (core and community modules), langchain_text_splitters for semantic chunking, HuggingFace SentenceTransformers for local text embeddings, and a local in-memory vector store for similarity search. The system runs entirely on the local machine and does not depend on OpenAI, AWS APIs, or internet-based inference services after initial model download.

Project structure:

agentic_rag/
├── src/
│   ├── app.py              (CLI entry point for asking questions)
│   ├── ingest.py           (Loads the PDF and performs semantic chunking)
│   ├── vector_store.py     (Creates embeddings and builds the vector index)
│   ├── orchestrator.py     (Coordinates Planner, Retriever, and Synthesizer agents)
│   └── agents.py
├── data/
│   └── aws_rag_guide.pdf   (AWS RAG Prescriptive Guidance document)
├── requirements.txt
├── demo_queries.txt
└── README.md

Setup and execution instructions: Install Python 3.10.x (recommended). Create and activate a virtual environment using “python -m venv venv” followed by “venv\\Scripts\\activate”. Install dependencies using “pip install --upgrade pip” and “pip install -r requirements.txt”. Place the AWS RAG guide PDF inside the data directory as “aws_rag_guide.pdf”. Run the application using “python src/app.py”. The terminal will prompt “Ask a question (or type exit):”. Type a question and press Enter to receive an answer. Type “exit” or press Ctrl+C to stop the program.

Example questions supported by the system include: “What are the fully managed RAG options available on AWS?”, “Compare fully managed RAG options with custom RAG architectures.”, “What retriever services are described in the AWS RAG guide?”, “How does the guide compare RAG with fine-tuning?”, and “What are best practices for chunking documents in RAG?”.

The system guarantees grounding and honesty by strictly limiting answers to information present in the AWS document. If a query requests information not available in the document, the assistant explicitly states that the information is not available. This project fully satisfies the assignment requirements for RAG pipeline implementation, agentic AI design, observability, and reproducibility.

Author: Mekala Ramadarsan