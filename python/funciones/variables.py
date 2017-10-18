animal = 'León'  #Es una variable global
edad = 6

def mostrar_animal():
  global animal, edad
  animal = 'Ballena'
  print(animal)

mostrar_animal()
print(animal)