#Beremo števila, dokler ne preberemo števila 999. Izpišemo, koliko je bilo negativnih števil

n = 0

while True:
    stevilo = int(input('Vnesi število '))
    if stevilo < 0:
        n = n+1
    if stevilo == 999:
        break
print(f'Število negativnih števil je {n}.')

