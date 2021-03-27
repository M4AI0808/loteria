#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random 
odpowiedz1 = 2
odpowiedz2 = 2
odpowiedz3 = 2
odpowiedz4 = 2
odpowiedz5 = 2
odpowiedz6 = 2
odpowiedz7 = 2
odpowiedz8 = 2
odpowiedz9 = 2
odpowiedz10 = 2
print ('Program ma na celu wylosować 1 osobe z pozostałych. Zasady są proste: ')
print ('1. Ten kto wylosuje najbliższą liczbe do liczby wylosowanej ten wygrywa.')
print ('2. Wybieracie liczby od 1 do 100 włącznie z 1 i 100')
print ('3. W losowaniu może brać udział max. 10 osób')
print ('4. jeżeli jest mniej niż 10 osób, więc jak wszyskie osoby ')
print ('wytypują swoje liczby w reszte wolnych slotów wpiszcie liczbe 0, wtedy program będzie ignorował te sloty.')
print ('5.Program pokazuje tylko 1 miejscem, może w przyszłości zrobię aby pokazywał też inne miejsca :D')
liczba = random.randint(1,100)
print(' ')
print(' ')
print(' ')
print('Typy graczy:')


# Kod pierwszej osoby
odpowiedz1 = input ('Pierwsza osoba typuje liczbe: ')
if int (odpowiedz1) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz1 = 0
if int (odpowiedz1) > 100 or int (odpowiedz1) < 0: 
    print ('Odpowiedz pierwszej osoby jest niepoprawna')
if int (odpowiedz1) == 0:
    print ('N/A')
else:
    print ('Typ pierwszej osoby to: ', odpowiedz1)
print(' ')



# Kod drugiej osoby
odpowiedz2 = input ('Druga osoba typuje liczbe: ')
if int (odpowiedz2) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz1 = 0
if int (odpowiedz2) > 100 or int (odpowiedz2) < 0: 
    print ('Odpowiedz drugiej osoby jest niepoprawna')
if int (odpowiedz2) == 0:
    print ('N/A')
else:
    print ('Typ drugiej osoby to: ', odpowiedz2)
print(' ')



# Kod trzeciej osoby
odpowiedz3 = input ('Trzecia osoba typuje liczbe: ')
if int (odpowiedz3) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz3 = 0
if int (odpowiedz3) > 100 or int (odpowiedz3) < 0: 
    print ('Odpowiedz trzeciej osoby jest niepoprawna')
if int (odpowiedz3) == 0:
    print ('N/A')
else:
    print ('Typ trzeciej osoby to: ', odpowiedz3)
print(' ')



# Kod czwartej osoby
odpowiedz4 = input ('Czwarta osoba typuje liczbe: ')
if int (odpowiedz4) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz4 = 0
if int (odpowiedz4) > 100 or int (odpowiedz4) < 0: 
    print ('Odpowiedz czwartek osoby jest niepoprawna')
if int (odpowiedz4) == 0:
    print ('N/A')
else:
    print ('Typ czwartej osoby to: ', odpowiedz4)
print(' ')



# Kod piątej osoby
odpowiedz5 = input ('Piąta osoba typuje liczbe: ')
if int (odpowiedz5) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz5 = 0
if int (odpowiedz5) > 100 or int (odpowiedz5) < 0: 
    print ('Odpowiedz piątej osoby jest niepoprawna')
if int (odpowiedz5) == 0:
    print ('N/A')
else:
    print ('Typ piątej osoby to: ', odpowiedz5)
print(' ')



# Kod szóstej osoby
odpowiedz6 = input ('Szósta osoba typuje liczbe: ')
if int (odpowiedz6) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz6 = 0
if int (odpowiedz6) > 100 or int (odpowiedz6) < 0: 
    print ('Odpowiedz szóstej osoby jest niepoprawna')
if int (odpowiedz6) == 0:
    print ('N/A')
else:
    print ('Typ szóstej osoby to: ', odpowiedz6)
print(' ')



# Kod siódmej osoby
odpowiedz7 = input ('Siódma osoba typuje liczbe: ')
if int (odpowiedz7) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz7 = 0
if int (odpowiedz7) > 100 or int (odpowiedz7) < 0: 
    print ('Odpowiedz siódmej osoby jest niepoprawna')
if int (odpowiedz7) == 0:
    print ('N/A')
else:
    print ('Typ siódmej osoby to: ', odpowiedz7)
print(' ')



# Kod ósmej osoby
odpowiedz8 = input ('Ósma osoba osoba typuje liczbe: ')
if int (odpowiedz8) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz8 = 0
if int (odpowiedz8) > 100 or int (odpowiedz8) < 0: 
    print ('Odpowiedz ósmej osoby jest niepoprawna')
if int (odpowiedz8) == 0:
    print ('N/A')
else:
    print ('Typ ósmej osoby to: ', odpowiedz8)
print(' ')



# Kod dziewiątej osoby
odpowiedz9 = input ('Dziewiąta osoba typuje liczbe: ')
if int (odpowiedz9) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz9 = 0
if int (odpowiedz9) > 100 or int (odpowiedz9) < 0: 
    print ('Odpowiedz dziewiątej osoby jest niepoprawna')
if int (odpowiedz9) == 0:
    print ('N/A')
else:
    print ('Typ dziewiątej osoby to: ', odpowiedz9)
print(' ')



# Kod dziesiątej osoby
odpowiedz10 = input ('Dziesiąta osoba typuje liczbe: ')
if int (odpowiedz10) > 100:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. Zostajesz wyrzucony z losowania :C')
    odpowiedz10 = 0
if int (odpowiedz10) > 100 or int (odpowiedz10) < 0: 
    print ('Odpowiedz dziesiątej osoby jest niepoprawna')
if int (odpowiedz10) == 0:
    print ('N/A')
else:
    print ('Typ dziesiątej osoby to: ', odpowiedz10)
print(' ')





# Kod sprawdzający zwycięstwo
print(' ')
Lst = [odpowiedz1, odpowiedz2, odpowiedz3, odpowiedz4, odpowiedz5, odpowiedz6, odpowiedz7, odpowiedz8, odpowiedz9, odpowiedz10]
if liczba == int(odpowiedz1):
    print ('Pierwsza osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz2):
    print ('Druga osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz3):
    print ('Trzecia osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz4):
    print ('Czwarta osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz5):
    print ('Piąta osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz6):
    print ('Szósta osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz7):
    print ('Siódma osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz8):
    print ('Ósma osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz9):
    print ('Dziewiąta osoba trafiła perfekcyjnie!!!')
if liczba == int(odpowiedz10):
    print ('Dziesiąta osoba trafiła perfekcyjnie!!!')
print ('Wylosowana liczba to: ', liczba)
print ('Najbliższy numer do wylosowanego numeru to: ', min(Lst, key=lambda x:abs(int (x)-liczba)))
print ('Co oznacza że osoba z tym numerem jest zwycięscą!!!!')
print (' ')
print('Czy program ma się wyłączyć? ')
koniec = input('Y/N ---> ')
print(koniec)