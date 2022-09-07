# Írjátok meg a signum függvényt!
#  Ha a szám kisebb, mint 0, akkor -1-et vissza
#  Ha a 0, akkor 0-át ad vissza
#  Ha nagyobb, mint 0, akkor 1-et ad vissza


def signum(n):
    #if n > 0:
        #return 1
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1
print(signum(0))

#  Írjatok egy függvényt, ami vár egy egész számot, és visszaadja
#  annak abszolútértékét!

def abs(n):
    if n < 0:
        return -n
    else:
        return n

#  Struktúrált programozás: minden függvényben CSAK egy
#  return utasítás lehet
def abs_structured(n):
    if n < 0:
        result = -n
    else:
        result = n
    return result

print(abs(10))
print(abs(-20))

print(abs_structured(10))
print(abs_structured(-20))


#  Írjátok meg a függvényt, mely várja a téglalap a és b oldalát, és
#  visszaadja a területet!

print("----------------")

def area(a, b):
    return a * b

print(area(10, 5))
print(area(3, 2))


#  Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
#  visszaadja kerületet!

print("----------------")

def calculate_perimeter(a, b):
    return (a + b) * 2

print(calculate_perimeter(4, 6))
print(calculate_perimeter(3, 5))


#  Írjatok egy függvényt, amely vár két számot, és visszaadja a
#  kettő közül a nagyobbat!

print("----------------")

def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(6, 9))
print(max(5, 5))
print(max(10, 4))


#  Vár egy számot és visszaadja a "páros" szöveget, ha páros,
#  ellenkező esetben hogy "páratlan"

print("----------------")

def get_type(n):
    if n % 2 == 0:
        return "páros"
    else:
        return "páratlan"

print(get_type(5))
print(get_type(6))

def get_type_structured(n):
    if n % 2 == 0:
        type = "páros"
    else:
        type = "páratlan"
    return type

print(get_type_structured(11))


#  Ha a függvény boolean értéket ad vissza, akkor
#  logikai függvény: True, vagy False

#  Írj egy is_even nevű függvényt, mely a paraméteréről
#  eldönti, hogy páros-e!
#  True-t adjon vissza, ha páros, False értéket adjon vissza,
#  ha páratlan

def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False

def is_even_simple(n):
    return n % 2 == 0

print(is_even(6))

if is_even(10):
    print("Ez egy szép páros szám")
else:
    print("Ez egy páratlan szám")


