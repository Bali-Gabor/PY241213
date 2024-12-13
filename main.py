# Feladat: Számok statisztikája

# Írj egy programot, amely bekér egy számokból álló listát a felhasználótól (számokat vesszővel elválasztva), majd kiszámolja és kiírja az alábbi statisztikákat:

# A lista elemeinek száma: Hány szám van a listában?
# Az elemek összege: A számok összege.
# Az elemek átlaga: Az átlagos érték.
# A legnagyobb és legkisebb szám: A lista maximum- és minimumértéke.
# A lista elemei növekvő sorrendben: Rendezett lista.

from moduls import *

szoveg=input('Adjon meg egy számsort ,-vel elválasztva!  ')

print(f'A listában {darab(konvertal(szoveg))} szám van.')
print(f'A számok összege: {osszeg(konvertal(szoveg))}')
print(f'A számok átlaga: {atlag(konvertal(szoveg))}')
print(f'A legkisebb szám a listában: {legkis(konvertal(szoveg))}')
print(f'A legnagyobb szám a listában: {legnagy(konvertal(szoveg))}')
print(f'A lista rendezve: {rendez(konvertal(szoveg))}')