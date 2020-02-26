import random
def generatepassword():

  for i in range(6):
    print(chr(random.randint(45,99)), end="")

generatepassword()