#Preberi tri trimestna naravna števila in izračunaj vsoto števk vsote vsot števk  vseh treh. 

a = int(input('Vnesi trimestno naravno število '))
b = int(input('Vnesi trimestno naravno število '))
c = int(input('Vnesi trimestno naravno število '))

enice_a = a % 10
desetice_a = a // 10 % 10
stotice_a = a // 100
vsota_a = enice_a + desetice_a + stotice_a 

enice_b = b % 10
desetice_b = b // 10 % 10
stotice_b = b // 100
vsota_b = enice_b + desetice_b + stotice_b

enice_c = c % 10
desetice_c = c // 10 % 10
stotice_c = c // 100
vsota_c = enice_c + desetice_c + stotice_c
# do sem program izračuna vsoto števk vsakega števila
vsota = vsota_a + vsota_b + vsota_c #sešteje vsote števk vsakega števila

enice = vsota % 10
desetice = vsota // 10 % 10
stotice = vsota // 100
vsota_koncna = enice + desetice + stotice
#sešteje števke vsote števk vsakega števila
print(f'Vsota števk vsote vsot števk vseh treh je {vsota_koncna}')







