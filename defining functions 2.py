text="Python rocks"
text2 = text + " AAA"
print(text2)
def reverseString(text):
  for letter in range(len(text)-1,-1,-1):
    print(text[letter],end="")

def reverseReturn(text):
  result=""
  for letter in range(len(text)-1,-1,-1):
    result = result + text[letter]

  return result

print(reverseReturn("zoom"))