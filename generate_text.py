from random import randint
import time as t

def generate_random():
    lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    specialCharacters = '.@;!()?"`:'
    characters = lowerCaseLetters + lowerCaseLetters.upper() + digits + specialCharacters

    # length = input("Length: ")
    length = randint(1,2137)
    text = ""

    print("Generating data...")
    t.sleep(1)

    for i in range(int(length)):
        text = text + characters[randint(0, len(characters)-1)]

    print("Data generated ✅")
    return text


def generate_markdown(text):
    with open("./output/file1.md", "w+") as file:
        file.write(text)