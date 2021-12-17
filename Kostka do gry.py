import random
def kostka():
    rzuty = (input("Podaj rzuty kostką w formie xDy+z lub xDy-z, gdzie x to ilość rzutów kością, Dy to rodzaj kostki (może być D3, D4, D6, D8, D10, D12, D20, D100), a z to ilość oczek, które należy dodać (opcjonalnie)"))
    dane = list(rzuty)
    return(dane) #funkcja zwraca dane wprowazone przez gracza w postaci listy pojedynczych elementów (np. ["2", "3", "D", "+", "8", "7"])

def spacje(): #funckja usuwa spacje gdyby gracz wpisał ciąg znakóœ ze spacjami
    dane = kostka()
    dane = [x.strip(' ') for x in dane]
    delete = [ele for ele in dane if ele.strip()]
    return(delete)

def merge(): #funkcja łączy wszystkie występujące obok siebie cyfry w liczby
    dane = spacje()
    index = 1
    while index < len(dane):
        if dane[index].isdigit() and dane[index - 1].isdigit():
            dane[index - 1] += dane.pop(index)
        else:
            index += 1
    return(dane) #funckja zwraca listę, np ["23", "D", "+", "87"]

def convert(): #funkcja zamienia wszystkie liczby na dane int
    newdane = merge()
    for i in range(0, len(newdane)):
        try:
            newdane[i] = int(newdane[i])
        except (ValueError, TypeError):
            pass
    return(newdane) #funkcja zwraca listę, np [23, "D", "+", 87]

def losowanie(): #funkcja losuje liczby zgodnie z danymi wprowadzonymi przez gracza i zmienionymi przez powyższe funkcje
    dane=convert()
    scianki = [3, 4, 6, 8, 10, 12, 20, 100] #dozwolone ścianki kostki w rzutach
    for index, x in enumerate(dane):
        if index == 0: #dla pierwszej liczby sprawdzanie czy liczba jest typu int
            if type(x) == int:
                pass
            else:
                print("Podaj pooprawne wartości")
        if index == 1: #sprawdzanie czy gracz wpisał D
            if x == "D":
                pass
            else:
                print("Upewnij się, że uwzględniłeś D w danych")
        if index == 2: #sprawdzanie czy gracz wybrał dozwoloną ilość ścianek
            if x in scianki:
                pass
            else:
                print("Podaj odpowiednią ilośc ścianek kostki")
        if index == 3: #sprawdzanie czy gracz wybrał + lub -
            if x == "+" or x == "_":
                pass
            else:
                print("Podaj poprawną wartość: + lub -")
        if index == 4: #sprawdzanie czy gracz wprowadził liczbę do dodania do rzutu
            if type(x) == int:
                pass
            else:
                print("Podaj poprawne wartości")
        return(dane)

def symulacja(): #symulacja losowania
    c = losowanie()
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
            wynik = y * a + z
        elif w == "-":
            wynik = y * a - z
    except (UnboundLocalError):
        wynik = y * a
    else:
        print("Błednie wprowadzone dane")
    return(wynik) #funkcja zwraca wylosowany wynik


print(symulacja())
