# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 13:40:10 2025

@author: gajsv_hktqfmf
"""
mesecni_zasluzek=input("koliko si zasluživ v prejšnjem mesecu?")
stroski=input("koliko si zapravil?")
ostanek=float(mesecni_zasluzek)-float(stroski)
print(f"ostalo ti je še {ostanek}€")
