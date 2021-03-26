#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
liczba = random.randint  (1,10)
odpowiedz = input ('Jaką liczbe od 1-10 mam na myśli?:')
while int (odpowiedz) > 31:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 30. ')
    exit()
if liczba==int (odpowiedz):
    print ("BRAWO, zgadłeś!!") #brawo
else: 
    print ('niezgadłeś :C')
    print ('poprawna liczba to: ', liczba)