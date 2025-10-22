#Sestavi funkcijo, ki vrne skupno vrženo število pik na dveh kockah
import random

def stevilo_pik():
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)

    rezultat = kocka1 + kocka2
    print(f'Skupno število pik je {rezultat}.')
    
stevilo_pik()