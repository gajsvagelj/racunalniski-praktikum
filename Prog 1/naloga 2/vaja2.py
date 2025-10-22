#Sestavi izraz, katerega vrednost je naključno sodo dvomestno število


stevilo = random.randrange(10,99,2) * random.choice([-1,1]) 
#generira naključno število od 10 do 99 z korakom 2
#in ga pomnoži z naključno izbranim pozitivnim ali negativnim koeficientom
