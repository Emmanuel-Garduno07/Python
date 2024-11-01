alumnos = {
    1: {"nombre": "Juan Pérez", "edad": 20, "localidad": "CDMX", "carrera": "Ingeniería", "año": 2},
    2: {"nombre": "María López", "edad": 21, "localidad": "Guadalajara", "carrera": "Medicina", "año": 3},
    3: {"nombre": "Carlos Hernández", "edad": 22, "localidad": "Monterrey", "carrera": "Derecho", "año": 4}
}
numero = int(input("Ingrese el número del alumno (1, 2 o 3): "))
if numero in alumnos:
    print("Información del alumno:")
    print("Nombre:", alumnos[numero]["nombre"])
    print("Edad:", alumnos[numero]["edad"])
    print("Localidad:", alumnos[numero]["localidad"])
    print("Carrera:", alumnos[numero]["carrera"])
    print("Año de carrera:", alumnos[numero]["año"])
else:
    print("Número de alumno no válido.")
