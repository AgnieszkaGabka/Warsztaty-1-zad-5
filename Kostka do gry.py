import random
def dice():
    throws = (input("Give the rolls of the dice in the form xDy+z or xDy-z, where x is the number of dice rolls, Dy is the type of the die (can be D3, D4, D6, D8, D10, D12, D20, D100) and az is the number of must be added (optional)"))
    data = list(throws)
    return(data) #funkcja zwraca dane wprowazone przez gracza w postaci listy pojedynczych elementów (np. ["2", "3", "D", "+", "8", "7"])

def spaces(): #funkcja usuwa spacje gdyby gracz wpisał ciąg znakóœ ze spacjami
    dane = dice()
    dane = [x.strip(' ') for x in dane]
    delete = [ele for ele in dane if ele.strip()]
    return(delete)

def merge(): #funkcja łączy wszystkie występujące obok siebie cyfry w liczby
    data = spaces()
    index = 1
    while index < len(data):
        if data[index].isdigit() and data[index - 1].isdigit():
            data[index - 1] += data.pop(index)
        else:
            index += 1
    return(data) #funckja zwraca listę, np ["23", "D", "+", "87"]

def convert(): #funkcja zamienia wszystkie liczby na dane int
    newdane = merge()
    for i in range(0, len(newdane)):
        try:
            newdane[i] = int(newdane[i])
        except (ValueError, TypeError):
            pass
    return(newdane) #funkcja zwraca listę, np [23, "D", "+", 87]

def draw(): #funkcja losuje liczby zgodnie z danymi wprowadzonymi przez gracza i zmienionymi przez powyższe funkcje
    data = convert()
    walls = [3, 4, 6, 8, 10, 12, 20, 100] #dozwolone ścianki kostki w rzutach
    for index, x in enumerate(data):
        if index == 0: #dla pierwszej liczby sprawdzanie czy liczba jest typu int
            if type(x) == int:
                pass
            else:
                print("Enter the correct values")
        if index == 1: #sprawdzanie czy gracz wpisał D
            if x == "D":
                pass
            else:
                print("Make sure you included D in your data")
        if index == 2: #sprawdzanie czy gracz wybrał dozwoloną ilość ścianek
            if x in walls:
                pass
            else:
                print("Enter the appropriate number of cube walls")
        if index == 3: #sprawdzanie czy gracz wybrał + lub -
            if x == "+" or x == "_":
                pass
            else:
                print("Enter a valid value: + or -")
        if index == 4: #sprawdzanie czy gracz wprowadził liczbę do dodania do rzutu
            if type(x) == int:
                pass
            else:
                print("Enter the correct values")
        return(data)

def simulation(): #symulacja losowania
    c = draw()
    x = c[2] #drugi index z listy - ilość ścianek
    y = c[0] #zerowy index z listy - ilość rzutów kostką
    try:
        w = c[3]  # trzeci index liczby - + lub -
    except (IndexError):
        pass
    try:
        z = c[4]  # czwarty index listy - liczba do dodania/odjęcia od rzutu
    except (IndexError):
        pass
    a = random.randint(1, x)
    try: # sprawdzanie czy użytkownik życzy sobie dodać lub odjąć liczbę - jeśli nie, funckja pomija te indexy w liście
        if w == "+":
            score = y * a + z
        elif w == "-":
            score = y * a - z
        else:
            print("Incorrectly entered data")
    except (UnboundLocalError):
        score = y * a

    return(score) #funkcja zwraca wylosowany wynik


print(simulation())
