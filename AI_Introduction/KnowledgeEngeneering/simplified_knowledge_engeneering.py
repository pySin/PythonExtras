class PropositionalElement:
    def __init__(self, name: str):
        self.name = name
        self.value = None


class GenerateModels:
    def __init__(self, *elements):
        self.elements: list = list(elements)
        self.model: list = []

    def generate(self):

        for element in self.elements:
            current_model = {}
            for element_2_iteration in self.elements:
                current_model[element_2_iteration] = True
            self.model.append(current_model)
        return self.model


if __name__ == "__main__":
    models = GenerateModels(["Ivan", "Kolio", "Nikolai", "rain"])
    models_list = models.generate()
    print(models_list)


