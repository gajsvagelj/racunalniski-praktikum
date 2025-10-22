#  Sestavi program, ki prebere dolžino, podano v svetlobnih letih (recimo  ly (1,231 s.l.) in jo pretvori v km in m.
#  Hitrost svetlobe: Približno 299.792.458  m/s. Za 1,231 s.l. torej dobimo 11.659.100.278.330.400 m, oziroma v znanstvenem
#  zapisu 1.1659e+13 km (Namig: uporabi {km_rezultat:.4e})
sv_leta = float(input('Vnesi število svetlobnih let '))
sekund_leto = 3600 * 24 * 365 * sv_leta
hitrost_svetlobe = 299792458
metrov_leto = hitrost_svetlobe * sekund_leto
print(f'{metrov_leto/1000:.4e}')

