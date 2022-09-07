#  Szimuláljuk a dobókockadobásr! 1-6

from random import randint, shuffle
from secrets import choice

#  randint fgv. nem build-in function
#  randint fgv a standard library részre
number = randint(1, 6)
print(number)

numbers = [2, 4, 6, 8]
shuffle(numbers)
print(numbers)

cards =["alsó", "felső", "király", "ász"]
card = choice(cards)
print(card)
