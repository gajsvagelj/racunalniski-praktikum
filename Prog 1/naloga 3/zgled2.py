a = float(input("Vpiši a: "))
b = float(input("Vpiši b: "))
c = float(input("Vpiši c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print('Enačba ima za rešitev poljubno naravno število')
        else:
            print('Enačba nima rešitve')
    else:
        x = -c / b  #izračuna x
        print(f'Enačba ima eno realno rešitev: {x}')
else:
    D = b**2 - 4 * a * c  #izračunamo diskriminanto D
    if D > 0: #če je D > 0 ima enačba dve realni rešitvi
        x1 = (-b + D) / 2 * a
        x2 = (-b - D) / 2 * a
        print(f'Enačba ima dve realni rešitvi: {x1} in {x2}')
    elif D == 0: #če je D = 0 ima enačba eno realno rešitev
        x = -b / 2 * a
        print(f'Enačba ima eno realno rešitev: {x}')
    else:
        print('Enačba nima realnih rešitev.')








