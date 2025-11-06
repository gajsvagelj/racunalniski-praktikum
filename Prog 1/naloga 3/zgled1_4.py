def menu():
    '''Načrtovanje obrokov'''
    #obroke zapišemo v seznam
    obrok = ['1. Piščančji kari', '2. Vegeterjanska lasanja', '3. Burger s solato', '4. Pizza']
    
    print('Načrtovanje obrokov')
    print()
    for jedi in obrok: #program se sprehodi po seznamu in izpiše jedi
        print(jedi)
    print()
    odg = input('Kateri od teh obrokov ti je najljubši? (1, 2, 3 ali 4) ') 
    #Vpraša uporabnika kaj bi rad jedel

    # Na podlagi uporabnikovega odgovora program izpiše obrok in dobere tek        
    if odg == '1':
        print('1. Piščančji kari prihaja')        
    elif odg == '2':
        print('2. Vegeterjanska lasana prihaja')
    elif odg == '4':
        print('4. Pizza prihaja')
    else:
        print('3. Burger s solato prihaja')
        
    print('Dober tek')


menu()