nombre = input("¿Cúal es tu nombre?\n")

edad = int(input("¿Cúal es tu edad?\n"))

peso = float(input("¿Cúal es tu peso?\n"))

autorizado = input("¿Estas Autorizado?(si/no)\n") == "si"

print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)