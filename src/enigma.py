"""enigma.py
Enigma Machine class file
"""
from collections import deque


class Enigma:
    """Enigma Machine class"""

    def __init__(self):
        self.keyboard = deque([
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ])

        self.rotors = {
            "rotor_I": deque([
                "U", "L", "T", "A", "O", "P", "I", "Q", "F", "Z", "Y", "N", "R",
                "M", "B", "E", "V", "X", "W", "H", "G", "D", "J", "K", "S", "C"
            ]),
            "rotor_II": deque([
                "N", "Y", "L", "S", "V", "I", "M", "T", "C", "F", "Z", "G", "Q",
                "K", "E", "R", "H", "U", "X", "B", "P", "A", "D", "J", "O", "W"
            ]),
            "rotor_III": deque([
                "P", "R", "X", "Z", "A", "F", "L", "C", "O", "M", "E", "N", "S",
                "D", "Q", "W", "J", "T", "U", "B", "K", "Y", "H", "I", "V", "G"
            ]),
            "rotor_IV": deque([
                "L", "A", "P", "M", "V", "Q", "H", "S", "U", "G", "B", "J", "T",
                "C", "I", "D", "Y", "F", "W", "E", "O", "Z", "R", "N", "X", "K"
            ]),
            "rotor_V": deque([
                "T", "R", "N", "F", "L", "P", "Z", "K", "W", "M", "J", "V", "C",
                "O", "Y", "Q", "X", "H", "B", "A", "U", "G", "I", "D", "S", "E"
            ]),
            "rotor_VI": deque([
                "E", "K", "S", "T", "D", "H", "Y", "B", "N", "Z", "O", "R", "X",
                "G", "L", "J", "A", "W", "U", "C", "F", "M", "P", "I", "V", "Q"
            ]),
            "rotor_VII": deque([
                "X", "B", "Q", "W", "A", "J", "Y", "P", "G", "O", "N", "H", "U",
                "S", "T", "D", "V", "E", "M", "C", "R", "K", "L", "I", "Z", "F"
            ]),
            "rotor_VIII": deque([
                "J", "O", "C", "F", "R", "L", "A", "N", "H", "T", "S", "U", "G",
                "E", "B", "W", "V", "Z", "M", "X", "K", "I", "P", "Y", "D", "Q"
            ]),
        }


if __name__ == "__main__":
    ...
