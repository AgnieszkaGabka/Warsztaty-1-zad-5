import random
def kostka():
    rzuty = (input("Podaj rzuty kostką w formie xDyz, gdzie x to ilość rzutów kością, Dy to rodzaj kostki (może być D3, D4, D6, D8, D10, D12, D20, D100), a z to ilość oczek, które należy dodać (opcjonalnie)"))
    dane = list(rzuty)
    return(dane)

def spacje():
    dane = kostka()
    dane = [x.strip(' ') for x in dane]
    delete = [ele for ele in dane if ele.strip()]
    return(delete)

def merge():
    dane = spacje()
    index = 1
    while index < len(dane):
        if dane[index].isdigit() and dane[index - 1].isdigit():
            dane[index - 1] += dane.pop(index)
        else:
            index += 1
    return(dane)

def convert():
    newdane = merge()
    for i in range(0, len(newdane)):
        try:
            newdane[i] = int(newdane[i])
        except (ValueError, TypeError):
            pass
    return(newdane)

def losowanie():
    dane=convert()
    scianki = [3, 4, 6, 8, 10, 12, 20, 100]
    for index, x in enumerate(dane):
        if index == 0:
            if type(x) == int:
                pass
            else:
                print("Podaj pooprawne wartości")
        if index == 1:
            if x == "D":
                pass
            else:
                print("Upewnij się, że uwzględniłeś D w danych")
        if index == 2:
            if x in scianki:
                pass
            else:
                print("Podaj odpowiednią ilośc ścianek kostki")
        if index == 3:
            if x == "+" or x == "_":
                pass
            else:
                print("Podaj poprawną wartość: + lub -")
        if index == 4:
            if type(x) == int:
                pass
            else:
                print("Podaj poprawne wartości")
        return(dane)

def symulacja():
    c = losowanie()
    x = c[2]
    y = c[0]
    z = c[4]
    w = c[3]
    a = random.randint(1, x)
    if w == "+":
        wynik = y * a + z
    elif w == "-":
        wynik = y * a - z
    else:
        print("Błednie wprowadzone dane")
    return(wynik)


print(symulacja())
