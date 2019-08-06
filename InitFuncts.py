from functools import partial
import math


def letterCombination(word):
  num = math.factorial(len(word))
  denom = 1
  checked = []
  for i in range(len(word)):
    tempC = 0
    if (word[i] not in checked):
      checked.append(word[i])
      for j in range(len(word)):
        if (word[i] == word[j]):
          tempC += 1
    denom = denom * (math.factorial(tempC))
  return num / denom


def matrixReduce(array2d):
  lead = 0
  rowC = len(array2d)
  colC = len(array2d[0])
  for r in range(rowC):
    if colC <= lead:
      break
    i = r
    while (array2d[i][lead]) == 0:
      i += 1
      if rowC == i:
        i = r
        lead += 1
        if colC == lead:
          break
    array2d[r], array2d[i] = array2d[i], array2d[r]
    if array2d[r][lead] != 0:
      array2d[r] = [(x / array2d[r][lead]) for x in array2d[r]]
    for j in range(rowC):
      if j != r:
        temparray2d = [(array2d[j][lead] * x) for x in array2d[r]]
        array2d[j] = [k - l for k, l in zip(array2d[j], temparray2d)]
    lead += lead
  return array2d


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


def intPolyIntegrate(string):
  var = ""
  start = True
  expo = False
  foundCoef = False
  coefs = ""
  expos = ""
  for chr in string:
    if start:
      if (str.isdigit(chr)):
        coefs += chr
        foundCoef = True
      if (str.isalpha(chr)):
        var = chr
        if (not foundCoef):
          coefs += "(1)"
      if (chr == "^"):
        expo = True
        start = False
    elif expo:
      exp = int(chr)
      exp += 1
      expos += str(exp)
      tmpcoef = coefs[-1]
      coefs = coefs[:-1]
      coefs += "(" + tmpcoef + "/" + str(exp) + ")"
      start = True
      foundCoef = False
      expo = False

  newpoly = ""
  for i in range(len(coefs)):
    if (coefs[i] == "("):
      newpoly += "("
      for j in range(i + 1, len(coefs)):
        if (coefs[j] == ")"):
          newpoly += ")"
          break
        newpoly += coefs[j]
      newpoly += (var + "^" + expos[0])
      expos = expos[1:]
      if (not expos):
        break
      else:
        newpoly += "+"
  return newpoly


def error():
  print("Error!")


def testfunct(x):
  return x ** 2


def sel():
  case = input("Selection: ")
  seldict = {
    '1': partial(integrate, testfunct, 0, 5),
    '2': partial(intPolyIntegrate, "3x^3+2x^6"),
    '3': partial(matrixReduce, [[1, 2, -1, -4], [2, 3, -1, -11], [-2, 0, -3, 22]]),
    '4': partial(letterCombination, "MISSISSIPPI")

  }
  print(seldict.get(case, error)())  # 9 is default if case not found


def main():
  print("Welcome to a list of learned Functions and Algorithms.\n"
        "Here are the choices...Type the number of selection.\n"
        "1) numerical integrate\n"
        "2) integer polynomial integrate\n"
        "3) reduced row echelon matrix\n"
        "4) combination of letters in string\n")
  sel()


if __name__ == '__main__':
  main()
