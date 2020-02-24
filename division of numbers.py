usernumber1 =int(input("Pick a number:"))
if usernumber1 %2 ==0 and usernumber1 %4 != 0:
  print ("Your number is even")
elif usernumber1 %2 ==1:
  print ("Your number is odd")
elif usernumber1 %4 ==0:
  print ("Your number is even and divisible by 4")