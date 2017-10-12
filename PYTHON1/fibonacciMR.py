# print the fibonacci numbers
def fibonacci(n):
   a=[1,1]
   for i in range(n):
      last=a[-1]
      b_last=a[-2]
      new=last+b_last
      a.append(new)
   print(a)

while True:
   try:
      num=int(input("How many Fibonnaci numbers do you want me to print out? "))
      break
   except:
      print("You need to insert an integer. Let's try it again. ")
      pass

fibonacci(num)
