# Python program to add two hexadecimal numbers. 

# Driver code 
# Declaring the variables 
a = "01B"
b = "378"

# Calculating hexadecimal value using function 
sum = hex(int(a, 16) + int(b, 16)) 

# Printing result 
print(sum[2:]) 
