print("Ingrese los platos favoritos de la Persona 1 (separados por comas): ")
platos_persona1 = set(input().split(','))

print("Ingrese los platos favoritos de la Persona 2 (separados por comas): ")
platos_persona2 = set(input().split(','))

platos_comunes = platos_persona1 & platos_persona2

platos_unicos_persona1 = platos_persona1 - platos_persona2
platos_unicos_persona2 = platos_persona2 - platos_persona1

print("Platos favoritos en común:", list(platos_comunes))
print("Platos únicos de la Persona 1:", list(platos_unicos_persona1))
print("Platos únicos de la Persona 2:", list(platos_unicos_persona2))
