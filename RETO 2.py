def calcular_promedio_y_cuadro_honor(grupo):
    suma_notas = 0
    notas = set()
    cuadro_honor = {1: [],
                    2: [],
                    3: []}
    for estudiante in grupo:
        suma_notas += estudiante['nota_fundamentos']
        #Me quedo con las notas diferentes del grupo
        notas = notas.union([estudiante['nota_fundamentos']])
    #Me quedo con las mejores 3 notas del grupo
    notas = list(notas)
    notas.sort()
    notas = notas[-3:]
    #Busco qué estudiantes tienen las mejores notas
    for estudiante in grupo:
        if estudiante['nota_fundamentos'] == notas[0]:
            cuadro_honor[3].append(estudiante['cédula'])
        elif estudiante['nota_fundamentos'] == notas[1]:
            cuadro_honor[2].append(estudiante['cédula'])
        elif estudiante['nota_fundamentos'] == notas[2]:
            cuadro_honor[1].append(estudiante['cédula'])
    return suma_notas / len(grupo), cuadro_honor

estudiante1 = {'cédula':14301503, 
               'nombre':'Pepito', 
               'nota_fundamentos':4.3}
estudiante2 = {'cédula':1037678471, 
               'nombre':'Fulanito', 
               'nota_fundamentos':3.2}
estudiante3 = {'cédula':71023567, 
               'nombre':'Pancho', 
               'nota_fundamentos':5}
estudiante4 = {'cédula':32276123, 
               'nombre':'Rita', 
               'nota_fundamentos':4.7}
estudiante5 = {'cédula':1036765245, 
               'nombre':'Anita', 
               'nota_fundamentos':4.7}
estudiante6 = {'cédula':89122456, 
               'nombre':'Pedrito', 
               'nota_fundamentos':4.7}
estudiante7 = {'cédula':289765345, 
               'nombre':'Mat', 
               'nota_fundamentos':4.8}
estudiante8 = {'cédula':4576890, 
               'nombre':'Dan', 
               'nota_fundamentos':4.8}

grupo = [estudiante1, 
         estudiante2, 
         estudiante3, 
         estudiante4, 
         estudiante5, 
         estudiante6, 
         estudiante7, 
         estudiante8]

calcular_promedio_y_cuadro_honor(grupo)