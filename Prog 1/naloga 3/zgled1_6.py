def menu():
    '''Načrtovanje obrokov'''
    print('Načrtovanje obrokov')
    print()
    print('1. Piščančji kari')
    print('2. Vegeterjanska lasanja')
    print('3. Burger s solato')
    print('4. Pizza')
    print()
    odg = input('Kateri od teh obrokov ti je najljubši? (1, 2, 3 ali 4) ')
    
            
    if odg == '1':
        print('1. Piščančji kari prihaja')        
    if odg == '2':
        print('2. Vegeterjanska lasana prihaja')
    if odg == '4':
        print('4. Pizza prihaja')
    if odg == '3':
        print('3. Burger s solato prihaja')
        
    print('Dober tek')

menu()