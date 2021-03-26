#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
liczba = random.randint  (1,10)
odpowiedz = input ('Jaką liczbe od 1-17 mam na myśli?:')
if liczba==int (odpowiedz):
    print ("BRAWO, zgadłeś!!") #brawo
else: 
    print ('niezgadłeś :C')
    print ('poprawna liczba to: ', liczba)