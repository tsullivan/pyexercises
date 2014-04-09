"xpos" answer
hoechstes_produkt = 0

for faktor1 in range(1,1000):
    for faktor2 in range(1,1000):
        produkt = faktor1 * faktor2
        if produkt == int(str(produkt)[::-1]):
            if produkt > hoechstes_produkt:
                hoechstes_produkt = produkt

print hoechstes_produkt
