#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
poprawna = 0 
liczba1 = random.randint  (1,30)
liczba2 = random.randint  (1,30)
liczba3 = random.randint  (1,30)
liczba4 = random.randint  (1,30)
liczba5 = random.randint  (1,30)
odpowiedz1 = input ('Podaj pierwszą liczbe (1-30): ')
while int (odpowiedz1) > 31:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. ')
    break
odpowiedz2 = input ('Podaj drugą liczbe (1-30): ')
while int (odpowiedz2) > 31:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. ')
    break
odpowiedz3 = input ('Podaj trzecią liczbe (1-30): ')
while int (odpowiedz3) > 31:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. ')
    break
odpowiedz4 = input ('Podaj czwartą liczbe (1-30): ')
while int (odpowiedz4) > 31:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. ')
    break
odpowiedz5 = input ('Podaj piątą liczbe (1-30): ')
while int (odpowiedz5) > 31:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. ')
    break
print ("Pierwsza liczba to: ", liczba1)
print ("Druga liczba to: ", liczba2)
print ("Trzecia liczba to: ", liczba3)
print ("Czwarta liczba to: ", liczba4)
print ("Czwarta liczba to: ", liczba5)
if liczba1==int (odpowiedz1):
    poprawna + 1 
if liczba2==int (odpowiedz2):
    poprawna + 1
if liczba3==int (odpowiedz1):
    poprawna + 1
if liczba4==int (odpowiedz2):
    poprawna + 1
if liczba5==int (odpowiedz2):
    poprawna + 1
print ("zgadłeś ")
print (poprawna)
print ('z 5 odpowiedzi, gratulacje!!!')
