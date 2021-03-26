#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
liczba = random.randint  (1,10)
odpowiedz = input ('Jaką liczbe od 1-10 mam na myśli?:')
while int (odpowiedz) > 31 or odpowiedz < 1:
    print ('ZŁa LICZBA, TYLKO LICZBY OD 1 DO 10. ')
    exit()
if liczba==int (odpowiedz):
    print ("BRAWO, zgadłeś!!") #brawo
else: 
    print ('niezgadłeś :C')
    print ('poprawna liczba to: ', liczba)