diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7, 'h':8}

del diccionario["a"]
valor = diccionario.pop("b")

diccionario.clear()

print(valor)
print(len(diccionario))
print(diccionario)