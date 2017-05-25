#!/usr/bin/env python
import sys

print("Zadej cislo:")
cislo=0
#print(cislo)
while True:
    try:
        cislo=int(input())
    except ValueError:
        print("To neni integer! Zopakuj cislo")
        pass
    else:
        print("V pohode")
        break
mod=cislo%2
#print(mod)
if mod > 0:
    print(cislo,"je liche cislo")
else:
    print(cislo,"je sude cislo")
