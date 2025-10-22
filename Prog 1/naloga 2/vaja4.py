#Sestavi funkcijo, ki vrne vsoto števk trimestnega celega števila

stevilo = int(input('Vnesi trimestno celo število '))

def vsota_stevk():
    abs_stevilo = abs(stevilo) #zapišemo absolutno vrednost števila, saj v nasprotnem primeru
#pride do težave pri celoštevilskem deljenju
#dobimo enice, desetice in stotice
    stotice = abs_stevilo//100
    desetice = abs_stevilo//10 % 10
    enice = abs_stevilo % 10
#jih seštejemo
    vsota = stotice + desetice + enice
    return vsota

print(f'Vsota števk trimestnega celega števila {stevilo} je {vsota_stevk()}.')