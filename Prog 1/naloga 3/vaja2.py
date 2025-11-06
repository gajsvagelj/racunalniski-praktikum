#Sestavi funkcijo, ki vrne število števk 0 danega naravnega števila


def stevke(n):
    '''izpiše število števk 0 danega naravnega števila'''
    stevilo_nicel = 0
    for stevka in str(n):  #celo stevilo spremenimo v niz da bomo lahko analizirali vsak znak posebaj
        if stevka == '0':
            stevilo_nicel += 1

    return stevilo_nicel

print(stevke(n))
    
    