import datetime


def years(age):
    birth_year = 2017 - int(age)

    return birth_year + 99


def main():
    age = input("Gimme ur age: ")
    print(years(age))
    return


if __name__ == '__main__':
    main()
