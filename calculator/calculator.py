import art

print(art.logo)
def add(n1, n2):
  return n1+n2
def sub(n1, n2):
  return n1-n2
def mul(n1, n2):
  return n1*n2
def div(n1, n2):
  return n1/n2
to_con = True
while to_con:
  num1 = int(input("Provide a number:\n"))
  num2 = int(input("Provide another number:\n"))
  operation = input("Choose an operand:\n+\n-\n*\n/\n")
  if operation == "+":
    print(add(num1, num2))
  elif operation == "-":
    print(sub(num1, num2))
  elif operation == "*":
    print(mul(num1, num2))
  elif operation == "/":
    print(div(num1, num2))
  else:
    print("Invalid Input")
  
  con = input("Do you wish to continue? Y or N\n")
  if con == "N":
    to_con = False