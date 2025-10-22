#  Trgovec Pepe se je odločil, da bo podražil repo za vsaj 7 odstotkov, a ne več kot 13.
#  Napiši program, ki bo prebral staro ceno (v centih kot celo število), določil interval dopustnih novih cen
#  (v evrih in centih) ter izpisal naključno ceno s tega intervala. Pazi, da bo izračun mej korekten!
import random
import math

stara_cena = int(input('Vnesi staro ceno v centih '))
min_cena = math.ceil(stara_cena * 1.07)
max_cena = math.floor(stara_cena * 1.13)

nova_cena = random.randint(min_cena,max_cena)
evri = nova_cena//100
centi = nova_cena%100

print(f'Nova cena bo {evri} € {centi} c')