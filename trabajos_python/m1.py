edad = int(input("Ingresa la edad para clasificar: "))

if edad < 2:
    categoria = "Bebé (0-1 años)"
elif 2 <= edad <= 12:
    categoria = "Niño (2-12 años)"
elif 13 <= edad <= 17:
    categoria = "Adolescente (13-17 años)"
elif 18 <= edad <= 64:
    categoria = "Adulto (18-64 años)"
else:
    categoria = "Anciano (65+ años)"

print(categoria)
