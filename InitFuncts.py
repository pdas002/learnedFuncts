def integrate(f, a, b):
  delta = 1 / 10000
  x = a
  x2 = a + delta
  total = 0
  for i in range(a, (b - a) * 10000):
    total += f(x + (.5 * (x2 - x))) * (x2 - x)
    x += delta
    x2 += delta
  return total


def error():
  print("Error!")


def testfunct(x):
  return x ** 2


def sel():
  case = input("Selection: ")
  seldict = {
    '1': integrate,
  }
  print(seldict.get(case, error)(testfunct, 1, 5))  # 9 is default if case not found


def main():
  print("Welcome to a list of learned Functions and Algorithms.\n"
        "Here are the choices...Type the number of selection.\n"
        "1) integrate\n"
        "2) \n"
        "3) \n")
  sel()


if __name__ == '__main__':
  main()
