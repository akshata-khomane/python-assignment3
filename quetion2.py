# Python program to count the frequency of 
# elements in a list using a dictionary 

def CountFrequency(my_list): 
	
# Creating an empty dictionary 
    count = {} 
    for i in [11,45,8,11,23,45,23,45,89]: 
	    count[i] = count.get(i, 0) + 1
    return count 

# Driver function 
if __name__ == "__main__": 
	my_list =[11,45,8,11,23,45,23,45,89] 
	print(CountFrequency(my_list)) 
