#Chci v zadanem souboru pocitat, kolikrat se tam vyskytuje Darth, Luke a Lea.
from collections import Counter
with open("zadani_091018.txt") as inp:
   file=inp.readlines()
   luke=file.count("Luke\n")
   lea=file.count("Lea\n")
   darth=file.count("Darth\n")+file.count("Darth")
   print("We have " + str(luke) + " Lukes, " + str(lea) + " Leas and " + str(darth) + " Darths.")

