#Sestavi funkcijo, ki vrne naključno liho trimestno število  število

import random
def naključno_stevilo():
    stevilo = random.randrange(101,999,2)*random.choice([-1,1])

#generira naključno število od 101 do 999 z korakom 2 in ga pomnoži
#z naključno izbranim pozitivnim ali negativnim koeficientom
    print(f'naključno liho trimestno število  število je {stevilo}.')

naključno_stevilo()

