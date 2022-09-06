if True:
    print("Ez mindig lefut")

if False:
    print("Ez sosem fut le")

if 5 > 100:
    print("vajon lefut-e")

n = 10
n % 2 == 0 #Páros
n % 2 == 1 #Páratlan

#  Kérj be a felhasználótól egy számot! Ha az páros, írd ki, hogy páros.
#  Ha az páratlan, írd ki, hogy páratlan.

szam = int(input ("Írj be egy számot!"))
maradek = szam % 2
if maradek == 0:
    print("páros")
if maradek ==1:
    print("páratlan")