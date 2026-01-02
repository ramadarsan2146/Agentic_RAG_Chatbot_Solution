class PlannerAgent:
    def plan(self, query):
        print("\n[PLANNER]")
        if "compare" in query.lower():
            qtype = "comparison"
            sections = ["Fully managed", "Custom"]
        elif "list" in query.lower():
            qtype = "listing"
            sections = ["Retrievers"]
        else:
            qtype = "general"
            sections = []

        print(f"Query Type: {qtype}")
        print(f"Target Sections: {sections}")
        return {"query": query, "sections": sections}


class RetrievalAgent:
    def retrieve(self, vector_store, plan):
        print("\n[RETRIEVER]")
        results = vector_store.search(plan["query"], top_k=6)

        filtered = []
        for r in results:
            if not plan["sections"] or any(
                s.lower() in r["metadata"]["section"].lower()
                for s in plan["sections"]
            ):
                filtered.append(r)

        for r in filtered:
            print(f"- Section: {r['metadata']['section']} | Score: {r['score']:.2f}")

        return filtered


class SynthesisAgent:
    def synthesize(self, query, passages):
        print("\n[SYNTHESIS]")

        if not passages:
            return "This information is not available in the provided AWS RAG guide."

        answer = "Answer:\n"
        for p in passages:
            answer += f"- {p['text']}\n"
            answer += f"  (Source: {p['metadata']['section']})\n\n"

        return answer