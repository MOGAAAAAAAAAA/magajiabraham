def ispalindrome(text):
  result=True
  reversed=""
  for i in range(len(text)-1,-1,-1):
    reversed+=text[i]
  if(reversed==text):
    result=True
  else:
    result=False

  return result

if(ispalindrome("racecar")):
  print("YES")