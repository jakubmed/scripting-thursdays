while True:
   try:    
      num = int(input("Please insert a whole number and I will tell you if it is odd or even: "))
      break
   except ValueError:
      print("Sorry, it is not a whole number..")
      pass
                                            
if num%4 == 0:
   print("Your number is even and it is divisible by 4 as well")
elif num%2 == 0:
   print("Your number is even")
else: 
   print("Your number is odd")
