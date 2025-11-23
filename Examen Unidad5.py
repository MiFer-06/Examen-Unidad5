# Pedir número de estudiantes y materias
num_estudiantes = int(input("Ingrese el número de estudiantes: "))
num_materias = int(input("Ingrese el número de materias: "))

# Crear la matriz de calificaciones
calificaciones = []
for i in range(num_estudiantes):
    estudiante = []
    for m in range(num_materias):
        calif = float(input(f"Ingrese la calificación del estudiante {i+1} en la materia {m+1} (0-100): "))
        estudiante.append(calif)
    calificaciones.append(estudiante)

promedios_estudiantes = [sum(estudiante) / num_materias for estudiante in calificaciones] # promedio de cada estudiante
promedios_materias = [sum(calificaciones[i][m] for i in range(num_estudiantes)) / num_estudiantes for m in range(num_materias)] # promedio de materias

todas_calificaciones = [calif for estudiante in calificaciones for calif in estudiante]
max_calif = max(todas_calificaciones) #calificasion mas alta
min_calif = min(todas_calificaciones) # mas baja

# Imprimir resultados
print("\nPromedio de cada estudiante:")
for i, promedio in enumerate(promedios_estudiantes, 1):
    print(f"Estudiante {i}: {promedio:.2f}")

print("\nPromedio de cada materia:")
for j, promedio in enumerate(promedios_materias, 1):
    print(f"Materia {j}: {promedio:.2f}")

print(f"\nCalificación más alta: {max_calif:.2f}")
print(f"Calificación más baja: {min_calif:.2f}")
