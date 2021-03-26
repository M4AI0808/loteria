#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random 
odpowiedz1 = 1
odpowiedz2 = 1
odpowiedz3 = 1
odpowiedz4 = 1
odpowiedz5 = 1
odpowiedz6 = 1
odpowiedz7 = 1
odpowiedz8 = 1
odpowiedz9 = 1
odpowiedz10 = 1
print ('Program ma na celu wylosować kolejnośc osób np. do gry czy do kolejki. Zasady są proste: ')
print ('1. Ten kto wylosuje najbliższą liczbe do liczby wylosowanej ten wygrywa.')
print ('2. Wybieracie liczby od 1 do 100 włącznie z 1 i 100')
print ('3. W losowaniu może brać udział max. 10 osób')
print ('4. jeżeli jest mniej niż 10 osób, więc jak wszyskie osoby ')
print ('wytypują swoje liczby w reszte wolnych slotów wpiszcie liczbe 0, wtedy program będzie ignorował te sloty.')
liczba = random.randint(1,100)
odpowiedz1 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz1) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz2 = input ('Druga osoba podaje liczbe: ')
while int (odpowiedz2) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz3 = input ('Trzecia osoba podaje liczbe: ')
while int (odpowiedz3) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz4 = input ('Czwarta osoba podaje liczbe: ')
while int (odpowiedz4) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz5 = input ('Piąta osoba podaje liczbe: ')
while int (odpowiedz5) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz6 = input ('Szósta osoba podaje liczbe: ')
while int (odpowiedz6) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz7 = input ('Siódma osoba podaje liczbe: ')
while int (odpowiedz7) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz8 = input ('Ósma osoba podaje liczbe: ')
while int (odpowiedz8) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz9 = input ('Dziewiąta osoba podaje liczbe: ')
while int (odpowiedz9) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz10 = input ('Dziesiąta osoba podaje liczbe: ')
while int (odpowiedz10) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
print ('Wylosowana liczba to: ', liczba)
if int (odpowiedz1) > 100 or int (odpowiedz1) < 0: 
    print ('odpowiedz pierwszej osoby jest niepoprawna')
if int (odpowiedz2) > 100 or int (odpowiedz2) < 0:
    print ('odpowiedz drugiej osoby jest niepoprawna.')
if int (odpowiedz3) > 100 or int (odpowiedz3) < 0:
    print ('odpowiedz trzeciej osoby jest niepoprawna.')
if int (odpowiedz4) > 100 or int(odpowiedz4) < 0:
    print ('odpowiedz czwartej osoby jest niepoprawna.')
if int (odpowiedz5) > 100 or int(odpowiedz5) < 0:
    print ('odpowiedz piątej osoby jest niepoprawna.')
if int (odpowiedz6) > 100 or int(odpowiedz6) < 0:
    print ('odpowiedz szóstej osoby jest niepoprawna.')
if int (odpowiedz7) > 100 or int(odpowiedz7) < 0:
    print ('odpowiedz siódmej osoby jest niepoprawna.')
if int (odpowiedz8) > 100 or int(odpowiedz8) < 0:
    print ('odpowiedz ósmej osoby jest niepoprawna.')
if int (odpowiedz9) > 100 or int(odpowiedz9) < 0:
    print ('odpowiedz dziewiątej osoby jest niepoprawna.')
if int (odpowiedz10) > 100 or int(odpowiedz10) < 0:
    print ('odpowiedz dziesiątej osoby jest niepoprawna.')
if int (odpowiedz1) == 0:
    print ('N/A')
else:
    print ('Typ pierwszej osoby to: ', odpowiedz1)
if int (odpowiedz2) == 0:
    print ('N/A')
else:
    print ('Typ drugiej osoby to: ', odpowiedz2)
if int (odpowiedz3) == 0:
    print ('N/A')
else:
    print ('Typ trzeciej osoby to: ', odpowiedz3)
if int (odpowiedz4) == 0:
    print ('N/A')
else:
    print ('Typ czwartej osoby to: ', odpowiedz4)
if int (odpowiedz5) == 0:
    print ('N/A')
else:
    print ('Typ piątej osoby to: ', odpowiedz5)
if int (odpowiedz6) == 0:
    print ('N/A')
else:
    print ('Typ szóstej osoby to: ', odpowiedz6)
if int (odpowiedz7) == 0:
    print ('N/A')
else:
    print ('Typ siódmej osoby to: ', odpowiedz7)
if int (odpowiedz8) == 0:
    print ('N/A')
else:
    print ('Typ ósmej osoby to: ', odpowiedz8)
if int (odpowiedz9) == 0:
    print ('N/A')
else:
    print ('Typ dziewiątej osoby to: ', odpowiedz9)
if int (odpowiedz10) == 0:
    print ('N/A')
else:
    print ('Typ dziesiątej osoby to: ', odpowiedz10)
if liczba == int(odpowiedz1):
    print ('Pierwsza osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz2):
    print ('Druga osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz3):
    print ('Trzecia osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz4):
    print ('Czwarta osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz5):
    print ('Piąta osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz6):
    print ('Szósta osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz7):
    print ('Siódma osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz8):
    print ('Ósma osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz9):
    print ('Dziewiąta osoba trafiła perfekcyjnie')
if liczba == int(odpowiedz10):
    print ('Dziesiąta osoba trafiła perfekcyjnie')
Lst = [odpowiedz1, odpowiedz2, odpowiedz3, odpowiedz4, odpowiedz5, odpowiedz6, odpowiedz7, odpowiedz8, odpowiedz9, odpowiedz10]
def closest(Lst, liczba):
    return Lst[min(range(len(Lst)), liczba = lambda i: abs(Lst[i]-liczba))]
print('najbliżej była osoba z liczbą: ', closest(Lst, liczba))