input_list=[1,1,2,2,3,3,4,4,5,5,6,6,7]

def my_function(input_list):
  return list(dict.fromkeys(input_list))
mylist = my_function(input_list)
print(mylist) 
