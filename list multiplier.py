list1=[2,4,6,3,4,8,6,5,4,3,6]
def multiplylist(mylist):
  result=1
  for x in mylist:
    result=result*x
  return result
print(multiplylist(list1))