#Generiraj naključno liho trimestno število in izpiši vsoto njegovih števk

import random

stevilo = random.randint(100, 999) * random.choice([-1,1])

abs_stevilo = abs(stevilo)#zapišemo absolutno vrednost števila, saj v nasprotnem primeru
#pride do težave pri celoštevilskem deljenju
#dobimo enice, desetice in stotice

enice = abs_stevilo % 10
desetice = abs_stevilo // 10 % 10
stotice = abs_stevilo // 100
vsota = enice + desetice + stotice
#jih seštejemo

print(f'Vsota števk trimestnega celega števila {stevilo} je {vsota}.')