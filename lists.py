from calendar import month


names = ["Joe", "Jack", "Jane"]

#  végigliterálunk a names változó elemein
for name in names:
    print(name)


counter = 10
for name in names:
    print(counter)
    print(name)
    counter +=2


months = ["január", "február", "március" ]
for month in months:
        print(month)


months = ["január", "február", "március"]
for month in months:
    print(f"Az év egyik hónapja {month}")


numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    print(number)
    sum += number
print(sum) 

