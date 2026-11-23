from math import pi as PI
def main()->None:
    while True:
        legenda()
        inp = input().lower().strip()
        if inp == "a":
            pp_fig_pl()
        elif inp == "b":
            obw_fig_pl()
        elif inp == "c":
            bryly()
        elif inp == "e":
            print("Program zkonczyl dzialanie")
            break
        else:
            print("Nie ma takiej komendy")
def legenda()->None:
    print("a = fig plaskie")
    print("b = obw fig plaskich")
    print("c = bryly")
    print("e = wyjdz z programu")

def legenda_pp_fig_pl()->None:
    print("a = kwadrat")
    print("b = prostokat")
    print("c = rownoleglobok")
    print("d = trapez")
    print("e = trojkat")
    print("f = kola")
    print("g = romb")

def legenda_obw()->None:
    print("a = kwadrat")
    print("b = prostokat")
    print("c = rownoleglobok")
    print("d = trapez")
    print("e = trojkat")
    print("f = kola")
    print("g = romb")

def legenda_bryl()->None:
    print("a = kula")
    print("b = graniastoslup")
    print("c = stozek")
    print("d = szescian")
    print("e = walec")
    print("f = prostopadloscian")
    print("g = ostroslup")
def bryly()->None:
    while True:
        legenda_bryl()
        inp = input().lower().strip()
        if inp == "a":
            r = float(input("r: "))
            objetosc_kuli(r)
        elif inp == "b":
            pp = float(input("pp: "))
            h = float(input("h: "))
            objetosc_graniastoslupa(pp, h)
        elif inp == "c":
            r = float(input("r: "))
            h = float(input("h: "))
            objetosc_stozka(r, h)
        elif inp == "d":
            a = float(input("a: "))
            objetosc_szescianu(a)
        elif inp == "e":
            r = float(input("r: "))
            h = float(input("h: "))
            objetosc_walca(r, h)
        elif inp == "f":
            a = float(input("a: "))
            b = float(input("b: "))
            h = float(input("h: "))
            objetosc_prostopadloscianu(a, b, h)
        elif inp == "g":
            pp = float(input("pp: "))
            h = float(input("h: "))
            objetosc_ostroslupa(pp, h)
        else:
            print("Nie ma takiej komendy")

def pp_fig_pl()->None:
        while True:
            legenda_pp_fig_pl()
            inp = input().lower().strip()
            if inp == "a":
                a = float(input("a: "))
                wynik = pp_kwadratu(a)
                print(wynik)
            elif inp == "b":
                a = float(input("a: "))
                b = float(input("b: "))
                pp_prostokata(a, b)
            elif inp == "c":
                a = float(input("a: "))
                h = float(input("h: "))
                pp_rownolegloboku(a, h)
            elif inp == "d":
                a = float(input("a: "))
                b = float(input("b: "))
                h = float(input("h: "))
                pp_trapezu(a, b, h)
            elif inp == "e":
                a = float(input("a: "))
                h = float(input("h: "))
                pp_trojkata(a, h)
            elif inp == "f":
                r = float(input("r: "))
                pp_kola(r)
            elif inp == "g":
                e = float(input("e: "))
                f = float(input("f: "))
                pp_romb(e, f)
            else:
                print("Nie ma takiej komendy")

                
def pp_kwadratu(a:float)->float:
    return a**2
def pp_prostokata(a:float,b:float)->float:
    pp_prostokat = ab
    return pp_prostokat
def pp_rownolegloboku(a:float,h:float)->float:
    pp_rownoleglobok = ah
    return pp_rownoleglobok
def pp_trapezu(a:float,b:float,h:float)->float:
    pp_trapez = (a+b)h/2
    return pp_trapez
def pp_trojkata(a:float,h:float)->float:
    pp_trojkat = ah/2
    return pp_trojkat
def pp_kola(r:float)->float:
    pp_kolo = PI*r2
    return pp_kolo
def pp_romb(e:float,f:float)->float:
    pp_romb = ef/2
    return pp_romb
def ob_kwadratu(a:float)->float:
    ob_kw = 4a
    return ob_kw
def ob_prostokata(a:float,b:float)->float:
    ob_prostokat = 2(a+b)
    return ob_prostokat
def ob_rownolegloboku(a:float,b:float)->float:
    ob_rownoleglobok = 2(a+b)
    return ob_rownoleglobok
def ob_trapezu(a:float,b:float,c:float,d:float)->float:
    ob_trapez = a+b+c+d
    return ob_trapez
def ob_trojkata(a:float,b:float,c:float)->float:
    ob_trojkat = a+b+c
    return ob_trojkat
def ob_kola(r:float)->float:
    ob_kolo = 2PIr
    return ob_kolo
def ob_romb(a:float)->float:
    ob_romb = 4a
    return ob_romb
def objetosc_kuli(r: float) -> float:
    V_kula = (4/3) PI * r**3
    return V_kula
def objetosc_graniastoslupa(pp: float, h: float) -> float:
    V_graniastoslup = pp * h
    return V_graniastoslup

def objetosc_stozka(r: float, h: float) -> float:
    V_stozek = (1/3) * PI * r2 * h
    return V_stozek

def objetosc_szescianu(a: float) -> float:
    V_szescian = a3
    return V_szescian

def objetosc_walca(r: float, h: float) -> float:
    V_walec = PI * r*2 h
    return V_walec

def objetosc_prostopadloscianu(a: float, b: float, h: float) -> float:
    V_prostopadloscian = a * b * h
    return V_prostopadloscian

def objetosc_ostroslupa(pp: float, h: float) -> float:
    V_ostroslup = (1/3) * pp * h
    return V_ostroslup
