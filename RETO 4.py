def es_semestre_valido(pensum, semestre):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return len(pensum) >= semestre and semestre > 0

def es_semestre_vacio(pensum, semestre):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return len(pensum[semestre-1]) == 0

def es_materia_valida(pensum, semestre, materia):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return materia in list(pensum[semestre-1].keys())

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN
    pensum[semestre-1]['materia']['nombre'] = nombre
    pensum[semestre-1]['materia']['creditos'] = creditos

# ACÁ TERMINA LA FUNCIÓN
# ESTA VEZ TU DEFINES TUS RETORNOS

def eliminar_materia(pensum, semestre, materia):
    # ACÁ INICIA LA FUNCIÓN
    pensum[semestre].pop(materia)



