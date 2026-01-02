from agents import PlannerAgent, RetrievalAgent, SynthesisAgent

class AgentOrchestrator:
    def __init__(self, vector_store):
        self.planner = PlannerAgent()
        self.retriever = RetrievalAgent()
        self.synthesizer = SynthesisAgent()
        self.vector_store = vector_store

    def run(self, query):
        plan = self.planner.plan(query)
        passages = self.retriever.retrieve(self.vector_store, plan)
        answer = self.synthesizer.synthesize(query, passages)
        return answer