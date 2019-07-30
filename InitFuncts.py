from functools import partial

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
      if(str.isdigit(chr)):
        coefs += chr
        foundCoef = True
      if(str.isalpha(chr)):
        var = chr
        if(not foundCoef):
          coefs += "(1)"
      if(chr == "^"):
        expo = True
        start = False
    elif expo:
      exp = int(chr)
      exp+=1
      expos += str(exp)
      tmpcoef = coefs[-1]
      coefs = coefs[:-1]
      coefs += "(" + tmpcoef + "/" + str(exp) + ")"
      start = True
      foundCoef = False
      expo = False

  newpoly = ""
  for i in range(len(coefs)):
    if(coefs[i] == "("):
      newpoly += "("
      for j in range(i+1, len(coefs)):
        if(coefs[j] == ")"):
          newpoly += ")"
          break
        newpoly += coefs[j]
      newpoly += (var+"^"+expos[0])
      expos = expos[1:]
      if(not expos):
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
    '2': partial(intPolyIntegrate, "3x^3+2x^6")
  }
  print(seldict.get(case, error)()) # 9 is default if case not found


def main():
  print("Welcome to a list of learned Functions and Algorithms.\n"
        "Here are the choices...Type the number of selection.\n"
        "1) numerical integrate\n"
        "2) integer polynomial integrate\n"
        "3) \n")
  sel()


if __name__ == '__main__':
  main()
