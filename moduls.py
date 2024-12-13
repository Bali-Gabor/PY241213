def konvertal(a:str)->list[int]:
    adat=a.split(',')
    szamok=[]
    for x in adat:
        szamok.append(int(x))
    return szamok


def darab(lista:list):
    return len(lista)


def osszeg(lista:list):
    return sum(lista)


def atlag(lista:list):
    return sum(lista) / len(lista)


def legkis(lista:list):
    return min(lista)


def legnagy(lista:list):
    return max(lista)

def rendez(lista:list)->list[int]:
    return sorted(lista)