#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random #ab
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
odpowiedz2 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz2) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz3 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz3) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz4 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz4) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz5 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz5) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz6 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz6) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz7 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz7) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz8 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz8) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz9 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz9) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
odpowiedz10 = input ('Pierwsza osoba podaje liczbe: ')
while int (odpowiedz10) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. KONIEC GRY')
    exit()
if odpowiedz1 > 100 or odpowiedz1 < 0: 
    print ('odpowiedz pierwszej osoby jest niepoprawna')
if odpowiedz2 > 100 or odpowiedz2 < 0:
    print ('odpowiedz drugiej osoby jest niepoprawna.')
if odpowiedz3 > 100 or odpowiedz3 < 0:
    print ('odpowiedz trzeciej osoby jest niepoprawna.')
if odpowiedz4 > 100 or odpowiedz4 < 0:
    print ('odpowiedz czwartej osoby jest niepoprawna.')
if odpowiedz5 > 100 or odpowiedz4 < 0:
    print ('odpowiedz piątej osoby jest niepoprawna.')
if odpowiedz6 > 100 or odpowiedz1 < 0: 
    print ('odpowiedz szóstej osoby jest niepoprawna.')
if odpowiedz7 > 100 or odpowiedz2 < 0:
    print ('odpowiedz siódmej osoby jest niepoprawna.')
if odpowiedz8 > 100 or odpowiedz3 < 0:
    print ('odpowiedz ósmej osoby jest niepoprawna.')
if odpowiedz9 > 100 or odpowiedz4 < 0:
    print ('odpowiedz dziewiątej osoby jest niepoprawna.')
if odpowiedz10 > 100 or odpowiedz4 < 0:
    print ('odpowiedz dziesiątej osoby jest niepoprawna.')
if odpowiedz1 == 0:
    print ('N/A')
if odpowiedz2 == 0:
    print ('N/A')
if odpowiedz3 == 0:
    print ('N/A')
if odpowiedz4 == 0:
    print ('N/A')
if odpowiedz5 == 0:
    print ('N/A')
if odpowiedz6 == 0:
    print ('N/A')
if odpowiedz7 == 0:
    print ('N/A')
if odpowiedz8 == 0:
    print ('N/A')
if odpowiedz9 == 0:
    print ('N/A')
if odpowiedz10 == 0:
    print ('N/A')
print ('Wylosowana liczba to: ', liczba)
print ('Typ pierwszej osoby to: ', odpowiedz1)
print ('Typ drugiej osoby to: ', odpowiedz2)
print ('Typ trzeciej osoby to: ', odpowiedz3)
print ('Typ czwartej osoby to: ', odpowiedz4)
print ('Typ piątej osoby to: ', odpowiedz5)
print ('Typ szóstej osoby to: ', odpowiedz6)
print ('Typ siódmej osoby to: ', odpowiedz7)
print ('Typ ósmej osoby to: ', odpowiedz8)
print ('Typ dziewiątej osoby to: ', odpowiedz9)
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
Lista = [odpowiedz1, odpowiedz2, odpowiedz3, odpowiedz4, odpowiedz5, odpowiedz6, odpowiedz7, odpowiedz8, odpowiedz9, odpowiedz10]
print (min(Lista, key=lambda x:abs(x-liczba)))