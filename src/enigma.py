"""enigma.py
Enigma Machine class file
"""
import sys
from collections import deque


class Enigma:
    """Enigma Machine class"""

    def __init__(self, msg_key: str, day_key: str, user_rotors=None):
        # Conditional auto generated from PyCharm
        if user_rotors is None:
            user_rotors = ["I", "II", "III"]

        self.msg_key = msg_key.upper()
        self.day_key = day_key.upper()
        self.user_rotors = user_rotors
        self.letter = None
        self.message = None

        # fmt: off
        self.keyboard = deque([
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
            ])

        self.rotors = {
                "I": deque([
                    "U", "L", "T", "A", "O", "P", "I", "Q", "F", "Z", "Y", "N", "R",
                    "M", "B", "E", "V", "X", "W", "H", "G", "D", "J", "K", "S", "C"
                    ]),
                "II": deque([
                    "N", "Y", "L", "S", "V", "I", "M", "T", "C", "F", "Z", "G", "Q",
                    "K", "E", "R", "H", "U", "X", "B", "P", "A", "D", "J", "O", "W"
                    ]),
                "III": deque([
                    "P", "R", "X", "Z", "A", "F", "L", "C", "O", "M", "E", "N", "S",
                    "D", "Q", "W", "J", "T", "U", "B", "K", "Y", "H", "I", "V", "G"
                    ]),
                "IV": deque([
                    "L", "A", "P", "M", "V", "Q", "H", "S", "U", "G", "B", "J", "T",
                    "C", "I", "D", "Y", "F", "W", "E", "O", "Z", "R", "N", "X", "K"
                    ]),
                "V": deque([
                    "T", "R", "N", "F", "L", "P", "Z", "K", "W", "M", "J", "V", "C",
                    "O", "Y", "Q", "X", "H", "B", "A", "U", "G", "I", "D", "S", "E"
                    ]),
                "VI": deque([
                    "E", "K", "S", "T", "D", "H", "Y", "B", "N", "Z", "O", "R", "X",
                    "G", "L", "J", "A", "W", "U", "C", "F", "M", "P", "I", "V", "Q"
                    ]),
                "VII": deque([
                    "X", "B", "Q", "W", "A", "J", "Y", "P", "G", "O", "N", "H", "U",
                    "S", "T", "D", "V", "E", "M", "C", "R", "K", "L", "I", "Z", "F"
                    ]),
                "VIII": deque([
                    "J", "O", "C", "F", "R", "L", "A", "N", "H", "T", "S", "U", "G",
                    "E", "B", "W", "V", "Z", "M", "X", "K", "I", "P", "Y", "D", "Q"
                    ]),
                }

        self.enigma_rotors = {
                "right": [deque([
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
                    deque([])
                    ],
                "center": [deque([
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
                    deque([])
                    ],
                "left": [deque([
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]),
                    deque([])
                    ],
                }
        # fmt: on

    def show_rotors(self):
        """Print the rotors with the left rotor being on top
        the right rotor being on bottom. Both sides of the
        rotors is printed.
        """
        for letter in self.enigma_rotors["left"][0]:
            print(letter, end=" ")
        print()
        for letter in self.enigma_rotors["left"][1]:
            print(letter, end=" ")
        print()
        print()
        for letter in self.enigma_rotors["center"][0]:
            print(letter, end=" ")
        print()
        for letter in self.enigma_rotors["center"][1]:
            print(letter, end=" ")
        print()
        print()
        for letter in self.enigma_rotors["right"][0]:
            print(letter, end=" ")
        print()
        for letter in self.enigma_rotors["right"][1]:
            print(letter, end=" ")
        print()

    def set_rotors(self):
        self.enigma_rotors["left"][1] = self.rotors[self.user_rotors[0]]
        self.enigma_rotors["center"][1] = self.rotors[self.user_rotors[1]]
        self.enigma_rotors["right"][1] = self.rotors[self.user_rotors[2]]

    def rotate_rotor(self, rotor_position, rotations=1):
        postions = ["left", "center", "right"]
        if rotor_position not in postions:
            print("Enter left, center, right rotor position")
            sys.exit()

        for _ in range(rotations):
            deque.rotate(self.enigma_rotors[rotor_position][0], -1)
            deque.rotate(self.enigma_rotors[rotor_position][1], -1)

    def set_rotors_to_day_key(self):
        while self.enigma_rotors["left"][1][0] != self.day_key[0]:
            deque.rotate(self.enigma_rotors["left"][1], -1)
        while self.enigma_rotors["center"][1][0] != self.day_key[1]:
            deque.rotate(self.enigma_rotors["center"][1], -1)
        while self.enigma_rotors["right"][1][0] != self.day_key[2]:
            deque.rotate(self.enigma_rotors["right"][1], -1)


if __name__ == "__main__":
    enigma = Enigma("ABC", "XYZ", ["II", "VI", "III"])
    enigma.set_rotors()
    enigma.show_rotors()
    enigma.set_rotors_to_day_key()
    print()
    enigma.show_rotors()
