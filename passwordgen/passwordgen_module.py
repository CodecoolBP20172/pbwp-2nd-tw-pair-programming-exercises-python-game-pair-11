import string
import random


def passwordgen(size=8, chars0=string.ascii_uppercase, chars1=string.ascii_lowercase, chars2 = string.digits):
    symbols = ['!','@','$','#','%','^','&','*','(',')','?']
    pass00 = random.choice(symbols)
    pass01 = pass00 + random.choice(chars0)
    pass02 = pass01 + random.choice(chars1)
    return pass02 + random.choice(chars2) + pass02 + pass01


def main():
    print(passwordgen())


#if __name__ == '__main__':
main()
