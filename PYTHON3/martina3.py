#Chci v zadanem souboru pocitat, kolikrat se tam vyskytuje Darth, Luke a Lea.
from collections import Counter
with open("zadani_091018.txt") as inp:
   file=inp.read().split()
   luke=file.count("Luke")
   lea=file.count("Lea")
   darth=file.count("Darth")
   print("We have " + str(luke) + " Lukes, " + str(lea) + " Leas and " + str(darth) + " Darths.")

