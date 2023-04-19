"""rotors.py"""
import random

letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

rotors_dict = {
    "rotor_I": list(),
    "rotor_II": list(),
    "rotor_III": list(),
    "rotor_IV": list(),
    "rotor_V": list(),
    "rotor_VI": list(),
    "rotor_VII": list(),
    "rotor_VIII": list(),
}


def create_rotors():
    global letters, rotors_dict

    for rotor, rotor_list in rotors_dict.items():
        while len(rotors_dict[rotor]) < 26:
            random_letter = random.choice(letters)
            if random_letter in rotors_dict[rotor]:
                continue
