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

    for rotor in rotors_dict.keys():
        while len(rotors_dict[rotor]) < 26:
            random_letter = random.choice(letters)
            if random_letter in rotors_dict[rotor]:
                continue
            else:
                rotors_dict[rotor].append(random_letter)


def shuffle_rotors():
    for _ in range(1000):
        for rotor in rotors_dict.values():
            random.shuffle(rotor)


def write_rotors():
    with open("./rotors.txt", "w") as w:
        for rotor_key, rotor in rotors_dict.items():
            w.write("\"" + rotor_key + "\": [")
            for i, letter in enumerate(rotor):
                if i == len(rotor) - 1:
                    w.write("\"" + letter + "\"")
                else:
                    w.write("\"" + letter + "\", ")
            w.write("]\n")


create_rotors()
shuffle_rotors()
write_rotors()
