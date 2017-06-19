def palindrome(str):
    lowercase = str.lower()
    pali_check = list(lowercase)
    for i in pali_check:
        if i == " ":
            pali_check.remove(i)
    print(pali_check)
    pali_back = []
    for i in reversed(pali_check):
        pali_back.append(i)
    if pali_check == pali_back:
        return True
    else:
        return False


def main():
    pali = input("gimme a word bro: ").lower()
    if palindrome(pali):
        print("this is a palindrome")
    else:
        print("this is not a palindrome")


if __name__ == '__main__':
    main()
