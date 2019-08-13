from functools import partial
import math, os, subprocess

class resistor:
  def __init__(self, resistance):
    self.val = resistance


class voltageSource:
  def __init__(self, volts):
    self.val = volts

class element:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class circuit:
  def __init__(self):
    self.head = None
    self.tail = None

  def addElement(self, elem):
    if not isinstance(elem, element):
      elem = element(elem)

    if self.head == None:
      self.head = elem
    else:
      self.tail.next = elem

    prevTail = self.tail
    self.tail = elem
    self.tail.prev = prevTail

  def printCircuit(self):
    circuit = ''
    head = self.head
    while head!= None:
      circuit += str(head.data.val)
      if(isinstance(head.data, resistor)):
        circuit += "R"
      elif(isinstance(head.data, voltageSource)):
        circuit += "V"
      head = head.next
      if head != None:
        circuit += "---"
    return circuit

  def calcCurrent(self):
    head = self.head
    voltage = 0
    resistance = 0
    while head != None:
      if (isinstance(head.data, resistor)):
        resistance += head.data.val
      elif (isinstance(head.data, voltageSource)):
        voltage += head.data.val
      head = head.next
    return voltage/resistance

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
        coefs += "("+ chr + ")"
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
      tmpcoef = coefs[-2]
      coefs = coefs[:-3]
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

def arrayCreate():
  l = []
  while(1):
    row = input("Enter coloumn members, seperated by only commas. Enter nothing to finish: ")
    if len(row) == 0:
      break
    temprow = []
    index = 0
    while(1): #create a row
      if index > (len(row)-1):
        break
      tempcol = ""
      while(1): #create a row element
          if index > (len(row)-1):
            temprow.append(int(tempcol))
            break
          if(row[index] == ','):
            index+=1
            temprow.append(int(tempcol))
            break
          tempcol += row[index]
          index+=1
    l.append(temprow)
  return l


def sel():
  case = input("Selection: ")
  if case == '1':
    return partial(integrate, testfunct, 0, 5)()
  elif case == '2':
    string = input("Enter polynomial: ")
    return partial(intPolyIntegrate, string)()
  elif case == '3':
    return partial(matrixReduce, arrayCreate())()
  elif case == '4':
    string = input("Enter word: ")
    return partial(letterCombination, string)()
  elif case == '5':
    c = circuit()
    while(1):
      element = input("Resistor or Voltage? (R/V): ")
      if element == 'R':
        r = input("Resistance: ")
        c.addElement(resistor(int(r)))
      elif element == "V":
        v = input("Voltage: ")
        c.addElement(voltageSource(int(v)))
      else:
        break
    func = input("Print or calculate current? (P/C):")
    if func == "P":
      return c.printCircuit()
    else:
      return c.calcCurrent()
  elif case == "6":
    return runExe("C:\\", "firefox.exe")

def runExe(dirPath, filename):
  for root, dirs, files in os.walk(dirPath):
    for file in files:
      if file == filename:
        exe = root + '\\' + file
        subprocess.call(exe)
        return "Found and ran!"
  return "Cannot find file"



def main():
  print("Welcome to a list of learned Functions and Algorithms.\n"
        "Here are the choices...Type the number of selection.\n"
        "1) numerical integrate\n"
        "2) integer polynomial integrate\n"
        "3) reduced row echelon matrix\n"
        "4) combination of letters in string\n"
        "5) circuit create and print\n"
        "6) Run .exe")
  print(sel())


if __name__ == '__main__':
  main()
