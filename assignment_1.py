'''
# python assignment 1:
a = 23
var1 = 12.9
var2 = 'hello'
var3 = "I'm good"
#5="python"
print('a type is',type(a))

print('type of var1, var2, var3 is',type(var1), type(var2), type(var3))
#print(' type of 5', 5) 

# take user input 
name = raw_input("Please enter your name: ")
#your_age =input("enter your age: ")
'''
# To take input from the user
num = int(input("Enter a number: "))
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
