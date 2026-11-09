"""
Lab 5, Task 1, Question 4 - TEMPLATE
Secure randomness with os.urandom and secrets.
Fill in the sections marked TODO, then run with:
    python3 randomness.py

Useful documentation:
  os.urandom: https://docs.python.org/3/library/os.html#os.urandom
  secrets:    https://docs.python.org/3/library/secrets.html
  random:     https://docs.python.org/3/library/random.html
"""

import os
import secrets
import random


def main():
    # Part 1: os.urandom for a key and a nonce.
    # TODO: generate a 16-byte key and a 12-byte nonce with os.urandom,
    #       and print each as a hex string.

    # Part 2: secrets as an alternative.
    # TODO: generate a 16-byte secret with secrets
    #       and a hex string; print both.

    # Part 3: the random module (NOT for cryptographic use).
    # TODO: generate a value with the random module.

    # Q4: two os.urandom calls should essentially never match.
    # TODO: call os.urandom twice and print whether the two results are equal.

    pass  # TODO: remove this once you have added your code above


if __name__ == "__main__":
    main()
