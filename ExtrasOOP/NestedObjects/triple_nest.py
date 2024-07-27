class Finger:

    def __init__(self, finger_position: str, length: float):
        self.finger_position = finger_position
        self.length = length

    @staticmethod
    def flex(self, strength: float):
        return "powerful" if strength > 3 else "weak"


class Hand:

    def __init__(self, *fingers: list[Finger]):
        if len(fingers) == 5:
            self.thumb = fingers[0]
            self.index_finger = fingers[1]
            self.middle = fingers[2]
            self.ring_finger = fingers[3]
            self.pinky = fingers[4]
        else:
            raise ValueError("There should be 5 fingers")

        self.counter = -1

    @staticmethod
    def grab(physical_object: str):
        return f"{physical_object} taken."

    def __iter__(self):
        return self

    def __next__(self):
        all_fingers = [self.thumb, self.index_finger, self.middle, self.ring_finger, self.pinky]
        self.counter += 1

        if self.counter < len(all_fingers):
            return all_fingers[self.counter]
        raise StopIteration


class Arm:

    def __init__(self, size: float):
        self.size = size


class Forearm:

    def __init__(self, size: float):
        self.size = size


class FullArm:

    def __init__(self, hand: Hand, arm: Arm, forearm: Forearm):
        self.hand = hand
        self.arm = arm
        self.forearm = forearm

    def take(self, physical_object: str):
        self.hand.grab(physical_object)


def create_full_arm():
    fingers = [Finger(f"finger{finger_i}", finger_i * 1.1) for finger_i in range(5)]
    hand1 = Hand(*fingers)
    arm1 = Arm(13.4)
    forearm1 = Forearm(12.8)
    full_arm = FullArm(hand1, arm1, forearm1)
    return full_arm


if __name__ == "__main__":
    f_arm = create_full_arm()
    for fi in f_arm.hand:
        print(fi.length)






