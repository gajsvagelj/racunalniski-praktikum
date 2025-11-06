
def menu():
    '''Načrtovanje obrokov'''
    print('Načrtovanje obrokov')
    print()
    print('1. Piščančji kari')
    print('2. Vegeterjanska lasanja')
    print('3. Burger s solato')
    print('4. Pizza')
    print()
    odg = int(input('Kateri od teh obrokov ti je najljubši? (1, 2, 3 ali 4) '))
    while True: 
        
        if odg in range(0,5): # če bo vnesena številka od 1 do 4 se bo zanka prekinila
            break             # in izvajanje programa se bo nadeljevalo.
        else:
            odg = int(input('Napačen vnos. Vnesi 1, 2, 3 ali 4: '))
            # ce nismo vnesili celega števila med 1 in 4 nas bo program opozoril na napako
            # in bo zahteval da ponovno vnesemo število.
            
    if odg == 1:
        print('1. Piščančji kari prihaja')        
    elif odg == 2:
        print('2. Vegeterjanska lasana prihaja')
    elif odg == 4:
        print('4. Pizza prihaja')
    elif odg == 3:
        print('3. Burger s solato prihaja')
        
    print('Dober tek')


menu()
