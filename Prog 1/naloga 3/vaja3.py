#Sestavi funkcijo, ki vrne vsoto števk poljubnega celega števila.

def vsota(n):
    '''Izračuna vsoto števk celega števila'''
    vsota_stevk = 0    
    for stevilo in str(n): #število pretvotimo v niz

        vsota_stevk += int(stevilo) #vsak niz preden ga seštejemo pretvorimo nazaj v celo število

    return vsota_stevk

print(vsota(n))
    
