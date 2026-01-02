from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.texts = []
        self.metadatas = []
        self.index = None

    def build(self, chunks):
        embeddings = []
        for c in chunks:
            emb = self.model.encode(c["text"])
            embeddings.append(emb)
            self.texts.append(c["text"])
            self.metadatas.append(c["metadata"])

        embeddings = np.array(embeddings).astype("float32")
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def search(self, query, top_k=5):
        q_emb = self.model.encode(query).astype("float32").reshape(1, -1)
        scores, ids = self.index.search(q_emb, top_k)

        results = []
        for i, idx in enumerate(ids[0]):
            results.append({
                "text": self.texts[idx],
                "metadata": self.metadatas[idx],
                "score": float(scores[0][i])
            })
        return results