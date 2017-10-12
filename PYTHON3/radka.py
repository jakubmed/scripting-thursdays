FILE_NAME = 'python.txt'

wordCounter = {}

with open(FILE_NAME,'r') as fh:
   for line in fh:
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      if word not in wordCounter:wordCounter[word] = 1
      else:
        wordCounter[word] = wordCounter[word] + 1
for  (word,occurance)  in wordCounter.items(): 
  print (word,occurance)

