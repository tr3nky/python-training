#  Függvény definició
def print_hello_world():
    print("hello")
    print("world")

def print_hello_world_five_times():
    for i in range(0, 5):
        print_hello_world()

#  egy paraméteres függvény, paraméter = argument
#  a paraméter nem más, mint egy változó
# függvény definició
def print_hello(text):
    print(f"hello {text}")
    print(text)

print_hello("Joe")
print_hello(input()) #  a hívás helye

#  Beépített függvények: input(), print(), str(), range()
fruits = ["meggy", "csereszenye", "körte"]

#len()
print(len(fruits))   # length - hossz

print(len("hello world")) #  string hosszát adja vissza

#  függvény: névvel ellátott utasítás csoport

#  DRY
#print("hello")
#print("world")

#print("hello")
#print("world")

print_hello_world()  # meghívom a függvényt, végrehajtásra kerül a függvényben lévő utasítások

print_hello_world()

print("-------")

print_hello_world_five_times()

print("---------------")

print_hello("Joe")
print_hello("Jack")

