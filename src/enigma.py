"""enigma.py
Enigma Machine class file
"""
from collections import deque


class Enigma:
    """Enigma Machine class"""

    def __init__(self, msg_key: str, day_key: str, user_rotors=None):
        # Conditional auto generated form PyCharm
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
        for letter in self.enigma_rotors["right"][0]:
            print(letter, end=" ")
        print()
        for letter in self.enigma_rotors["right"][1]:
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
        for letter in self.enigma_rotors["left"][0]:
            print(letter, end=" ")
        print()
        for letter in self.enigma_rotors["left"][1]:
            print(letter, end=" ")
        print()

    def set_rotors(self):
        self.enigma_rotors["right"][1] = self.rotors[self.user_rotors[0]]
        self.enigma_rotors["center"][1] = self.rotors[self.user_rotors[1]]
        self.enigma_rotors["left"][1] = self.rotors[self.user_rotors[2]]


if __name__ == "__main__":
    enigma = Enigma("ABC", "XYZ")
    enigma.set_rotors()
    enigma.show_rotors()
