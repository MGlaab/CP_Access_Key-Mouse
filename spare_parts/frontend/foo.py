import string

alphabet = string.ascii_uppercase[:26]

# Python code to convert string to list character-wise
def Convert(string):
	list1=[]
	list1[:0]=string
	return list1

# Driver code 
print(Convert(alphabet))
