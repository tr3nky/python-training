fruits = ["apple", "raspberry", "cherry"]

for fruit in fruits:
    print(fruit)

print(len(fruits))

print(fruits[1])

print(fruits[1:3])

print("apple" in fruits)

#  Függvények
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

fruits = ["apple", "raspberry", "cherry"]
print(fruits.index("raspberry"))
#print(fruits.index("banana"))
#print(fruits.index("banana"))
#ValueError: 'banana' is not in list

#  Óriási különbség: a lista múdosítható
#fruits = ["apple", "raspberry", "cherry"]
#fruits[1] = "banana"
#print(fruits)

fruits.append("peach")
print(fruits)