edad = int(input('Indicar la edad del paciente: '))
peso_kg = float(input('Indicar el peso del paciente en kilogramos: '))

ac = 0.0601 #aporte carbohidrato
ap = 0.0305 #aporte proteina 
av = -0.0244 #aporte frutas & verduras
desnutricion = 'A'
sobrepeso = 'B'
saludable = 'C'
diet_desnutricion = ac * 2 + ap + av * 2 
diet_sobrepeso = ac * 0.6 + ap + av * 4
diet_saludable = ac * 0.5 + ap * 0.7 + av * 2 
pso_t = 0
dias_diet = 0
estado = 0 

if edad>=5 and edad<=10: 
    if peso_kg <16:
       estado = desnutricion
       peso_ideal = 22
       pso_t = peso_ideal - peso_kg     
    elif peso_kg >28:
       estado = sobrepeso
       peso_ideal = 24 
       pso_t = peso_ideal - peso_kg
    else:
       estado = saludable
       peso_ideal = 28
       pso_t = peso_ideal - peso_kg  

if edad>10 and edad<=13:
    if peso_kg <30:
       estado = desnutricion
       peso_ideal = 32
       pso_t = peso_ideal - peso_kg
    elif peso_kg >=50:
       estado = sobrepeso
       peso_ideal = 43 
       pso_t = peso_ideal - peso_kg
    else:
       estado = saludable
       peso_ideal = 50
       pso_t = peso_ideal - peso_kg
       
if edad>13 and edad<=17:
    if peso_kg <51:
       estado = desnutricion
       peso_ideal = 56
       pso_t = peso_ideal - peso_kg
    elif peso_kg >=63:
       estado = sobrepeso
       peso_ideal = 58
       pso_t = peso_ideal - peso_kg
    else:
       estado = saludable
       peso_ideal = 63
       pso_t = peso_ideal - peso_kg

if estado == desnutricion:
    if pso_t % diet_desnutricion != 0:
       dias_diet = int(pso_t // diet_desnutricion + 1)
    else:
       dias_diet = int(pso_t // diet_desnutricion)
      
if estado == sobrepeso:
    if pso_t % diet_sobrepeso != 0:
       dias_diet = int(pso_t // diet_sobrepeso + 1)
    else:
       dias_diet = int(pso_t // diet_sobrepeso) 

if estado == saludable:
    if pso_t % diet_sobrepeso != 0:
       dias_diet = int(pso_t // diet_saludable + 1)
    else:
       dias_diet = int(pso_t // diet_saludable) 

if estado=='A' or estado=='B':
   print(f'El estado nutricional del paciente es {estado} y se requieren {dias_diet} dias de dieta para que alcance un peso saludable')
else:
   print(f'El estado nutricional del paciente es {estado} y se requieren {dias_diet} dias de dieta para que alcance el peso maximo')
   