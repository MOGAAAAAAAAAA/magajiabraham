num = int(input("Pick a number: "))
check = int(input("Pick a number to divide it by: "))
if num %check == 0:
  print("Your number is divisible by", check)
else:
  print("Your number is not divisible by", check)