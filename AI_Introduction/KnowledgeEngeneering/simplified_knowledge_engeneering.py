class PropositionalElement:
    def __init__(self, name: str):
        self.name = name
        self.value = None


class GenerateModels:
    def __init__(self, *elements):
        self.elements: list = list(elements)
        self.model_elements = []
        for tf in [True, False]:
            pairs = {}
            for el in self.elements:
                pairs[el] = tf
            self.model_elements.append(pairs)
        print(self.model_elements)

    def generate(self):
        true_elements = self.model_elements[0]
        false_elements = self.model_elements[1]

        for te in true_elements:

            for fe in false_elements:
                if te == fe:
                    pass
                else:



if __name__ == "__main__":
    models = GenerateModels("Ivan", "Kolio", "Nikolai", "rain")


