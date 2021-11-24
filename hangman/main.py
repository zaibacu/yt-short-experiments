import os
import random


def clear_screen():
    if os.name == "nt":
        # Windows
        os.system("cls")
    else:
        # Mac, Linux
        os.system("clear")


def main():
    with open("words.txt", "r") as f:
        words = [line.strip()
                 for line in f.readlines()
                 if line.strip() != ""]
    secret_word = random.choice(words).upper()
    clear_screen()
    lives = 5
    guesses = [" "]
    while lives > 0:
        print(" ".join(["❤️"] * lives))
        secret_masked = ""
        for letter in secret_word:
            if letter in guesses:
                secret_masked += letter
            else:
                secret_masked += "*"
        # print("".join(["*"] * len(secret_word)))
        print(secret_masked)
        if "*" not in secret_masked:
            break
        c = input("Guess the letter: ").upper()[0]
        guesses.append(c)
        if c not in secret_word:
            lives -= 1

        clear_screen()

    if lives > 0:
        print("Great success!")
    else:
        print("Better luck next time...")


if __name__ == "__main__":
    main()
