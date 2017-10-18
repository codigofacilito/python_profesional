animal = 'León' #Es una variable global

def mostrar_animal():
  global animal
  animal = 'Ballena' #variables locales
  print(animal)

mostrar_animal()
print(animal)