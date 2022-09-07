import numbers


numbers = [23, 0, 54, 76, 0, -10, 54, 0, -21, 0, -35, 10]

#  Adjuk össze csak a pozitív számokat!

sum = 0
for n in numbers:
    if n > 0:
        sum += n
print(sum)

#  Számoljuk meg, és írjuk ki, hogy a listában hány nulla szerepel!
count = 0
for n in numbers:
    if n == 0:
        count += 1
print(count)
