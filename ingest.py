from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = []
    for page in pages:
        section = page.metadata.get("title", "Unknown Section")
        for chunk in splitter.split_text(page.page_content):
            chunks.append({
                "text": chunk,
                "metadata": {
                    "section": section,
                    "source": "AWS RAG Guide"
                }
            })
    return chunks