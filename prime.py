
# function to check prime or not
num= int(input("Please enter your number: "))

#def isPrime(num)
if num >1:
  for i in range (2,num):
    if (num % i) == 0:
      print("this is not a prime")
      print(i,"x",num//i,"=",num)
      break
  else:
    print("this is a prime")
else:
  print("It is not a prime")


  
 


