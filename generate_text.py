from random import randint

def generate_random():
    lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
    upperCaseLetters = lowerCaseLetters.upper()
    digits = "0123456789"
    specialCharacters = '.@;!()?"`:'
    characters = lowerCaseLetters + upperCaseLetters + digits + specialCharacters

    # length = input("Length: ")
    length = randint(1,2137)
    text = ""

    for i in range(int(length)):
        text = text + characters[randint(0, len(characters)-1)]

    return text


def generate_markdown(text):
    with open("./output/file1.md", "w+") as file:
        file.write(text)