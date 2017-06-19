def listoverlap(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    union = list(set1 & set2)
    return union


def main():
    print(listoverlap(a, b))


if __name__ == '__main__':
    main()
