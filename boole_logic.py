#  Logikai kifejezések

#  Logikai literál
True
False
print(type(True))

#Ha van tojás, és van szalonna, akkor csináljunk ham&eggs
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#  Vagy
# Ha éhes vagy vagy 16:00 óra múlt, akkor egyél
print( True or True)
print(True or False)
print(False or True)
print(False or False)

# Negáció
print(not True)
print(not False)

#  Kombinálva
print((( not True) or (False)) and (not False))

#  Összeshasonlítások: relációs jelek
print(1 < 2)
print(1 > 2)
print( 1 == 2)  #Vigyázz, összehasonlitás KÉT egyenlőség jel
print( 1 <= 2)
print(1 >= 2)
print(1 >= 1)

print(1 < 5 < 10)

# Hogyan döntjük el egy számról, hogy páros-e?
# A számot osztjuk kettővel, és páros, ha a maradéka nulla
print(9 % 2 == 0)
print(10 % 2 ==0)
print(11 % 2 == 0)
print(12 % 2 ==  0)

#  Kérjünk be a felhasználótól egy számot, és írjuk ki, hogy False, ha
#  a szám páros, és írjuk ki, hogy True, ha a szám páratlan


number = int(input("Írj be egy számot!"))
#print(number % 2 ==1 )
print(not (number % 2 ==0))
print(( number % 2 == 0) == False)
