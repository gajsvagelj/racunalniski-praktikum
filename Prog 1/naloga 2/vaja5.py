#Sestavi izraz, katerega vrednost je vsota števk trimestnega celega števila n



#zapišemo absolutno vrednost števila, saj v nasprotnem primeru
#pride do težave pri celoštevilskem deljenju
#dobimo enice, desetice in stotice
abs_stevilo % 10 + abs_stevilo // 10 % 10 + abs_stevilo // 100
