import os
from hybrid_llm.llm.mistral_local import LocalMistral

class Router:
    def __init__(self, mode="local"):
        self.mode = mode
        self.local = LocalMistral()

    def set_mode(self, mode):
        self.mode = mode

    def answer(self, prompt):
        return self.local.answer(prompt)

def create_router(mode="local"):
    return Router(mode=mode)
