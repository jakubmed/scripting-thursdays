
# chci funkci, ktera mi vrati nejvetsi ze tri promennych
def max_of_three (a,b,c):
   if (a > b) & (a > c):
      print(str(a) + " is the largest")
   elif (b > a) & (b > c):
      print(str(b) + " is the largest")
   else:
      print(str(c) + " is the largest")

while True:
   try:
      i = float(input("Please input three numbers and I will tell you which one is the largest. First one is:")) 
      break
   except:
      print("It is not a number, let's do it again.")
      pass

while True:
   try:
      j = float(input("The second one is:"))
      break
   except:
      print("It is not a number, let's do it again.")
      pass
                                                                                                                                          
while True:
   try:
      k = float(input("The third one is:"))
      break
   except:
      print("It is not a number, let's do it again.")
      pass

max_of_three(i,j,k)
                                                                                                                                                                                         
                                                                                                                                                                                             





