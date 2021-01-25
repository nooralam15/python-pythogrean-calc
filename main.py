#imoport libraries
import math

#this function does the calculation
def pythagoreanFormula(a, b):
  calc =  str(round(math.sqrt(a**2 + b**2), 2))
  return print("The Value of C is " + calc)

#this function gets the user input
def getInfo(): 
  aValue = int(input("Enter the A value: "))
  bValue = int(input("Enter the B value: "))
  pythagoreanFormula(aValue, bValue)
getInfo()
