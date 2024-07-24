class PropositionalElement:
    def __init__(self, name: str):
        self.name = name
        self.value = None


class GenerateModels:
    def __init__(self, *elements):
        self.elements = list(elements)


