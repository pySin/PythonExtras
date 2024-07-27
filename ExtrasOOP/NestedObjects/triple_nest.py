class Finger:

    def __init__(self, finger_position: str, length: float):
        self.finger_position = finger_position
        self.length = length

    @staticmethod
    def flex(self, strength: float):
        return "powerful" if strength > 3 else "weak"