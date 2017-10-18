diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}

resultado = diccionario.setdefault("z", {})

print(resultado)
print(diccionario)