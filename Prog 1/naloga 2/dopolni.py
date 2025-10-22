

def razbij(stevilo):
    """Tromestno naravno število razbijemo na enice, desetice in stotice"""
    enice = stevilo % 10
    desetice = stevilo // 10 % 10
    stotice = stevilo // 100
    return enice, desetice, stotice

def obrat(stevilo):
    """Vrne obrat tromestnega naravnega števila.
       Iz 156 dobimo 651
    """
    en, des, st = razbij(stevilo)
    return en * 100 + des * 10 + st

def vsota_stevk(stevilo):
    """Vrne vsoto števk tromestnega naravnega števila.
       Iz 156 dobimo 12"""
    enice, desetice, stotice = razbij(stevilo)
    vsota = enice + desetice + stotice
    return vsota # A1

def produkt_stevk(stevilo):
   """Vrne produkt števk tromestnega naravnega števila."""
   enice, desetice, stotice = razbij(stevilo)
   produkt = enice * desetice * stotice
   return produkt # B1
      # B2

# glavni program 
stevilo = int(input('Vnesi tromestno naravno število '))   #C1
# spremenljivkam priredimo ustrezne funkcije                    #D1
obrnjeno = obrat(stevilo)
vsota = vsota_stevk(stevilo)
produkt = produkt_stevk(stevilo) #E1   
# izračuni
razlika = abs(stevilo - obrnjeno)
ostanek_vsota = razlika % vsota      #F1
ostanek_produkt = razlika % produkt    #F2
# izpisi
print(f'Dano je tromestno naravno število {stevilo}.')      #G1
print(f'Vsota števk je {vsota}, produkt pa {produkt}')   #G2 
print(f'Razlika je: {razlika}.')                   #G3 
print(f'Ta razlika da pri deljenju z vsoto števk ostanek {ostanek_vsota}.')       #G4 
print(f'In pri deljenju s produktom števk ostanek {ostanek_produkt}.') #G5
