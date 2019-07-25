def test():
    print("test")


def test2():
    print("test2")


def error():
    print("Error!")


def sel():
    case = input("Selection: ")
    seldict = {
        '1': test,
        '2': test2,
    }
    seldict.get(case, error)()    # 9 is default if case not found


def main():
    print("Welcome to a list of learned Functions and Algorithms.\n"
          "Here are the choices...Type the number of selection.\n"
          "1) \n"
          "2) \n"
          "3) \n")
    sel()


if __name__ == '__main__':
    main()