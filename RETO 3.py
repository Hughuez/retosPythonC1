import numpy as np

def balotera(balotas):
    balotas_revueltas = np.random.permutation(balotas)
    balotas_minimas = []
    b = 0
    i = 0
    n = 0
    g = 0
    o = 0
    for lista in balotas_revueltas:
        if "B" in lista:
            if b <5:
                balotas_minimas.append(lista)
                b +=1
            elif b == 5:
                continue
    
        elif "I" in lista:
            if i <5:
                balotas_minimas.append(lista)
                i +=1
            elif i == 5:
                continue
    
        elif "N" in lista:
            if n <4:
                balotas_minimas.append(lista)
                n +=1
            elif n == 4:
                continue

        elif "G" in lista:
            if g <5:
                balotas_minimas.append(lista)
                g +=1
            elif g == 5:
                continue

        elif "O" in lista:
            if o <5:
                balotas_minimas.append(lista)
                o +=1
            elif o == 5:
                continue
    return tuple(balotas_minimas)

balotas = ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15',
           'I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
           'N31','N32','N33','N34','N35','N36','N37','N38','N39','N40','N41','N42','N43','N44','N45',
           'G46','G47','G48','G49','G50','G51','G52','G53','G54','G55','G56','G57','G58','G59','G60',
           'O61','O62','O63','O64','O65','O66','O67','O68','O69','O70','O71','O72','O73','O74','O75']

