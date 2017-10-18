class Gato:
  def __init__(self, nombre):
    self.nombre = nombre

  def __str__(self):
    return self.nombre


class Pato(object):
  def __init__(self, nombre):
    self.nombre = nombre
  
  def __str__(self):
    return self.nombre

gato = Gato("Bigotes")
gato.edad = 6
pato = Pato("Lucas")

print(gato.__dict__)
print(pato.__dict__)