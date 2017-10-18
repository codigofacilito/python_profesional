def crear_usuario(nombre='', apellido='', edad=10):
  return {
    'nombre' : nombre,
    'apellido': apellido,
    'nombre_completo' : "{} {}".format(nombre, apellido),
    'edad': edad
  }

codi = crear_usuario(edad=11, apellido='Facilito', nombre='Codi')

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])