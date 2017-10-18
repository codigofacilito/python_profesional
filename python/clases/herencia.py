class Animal:
  def comer(self):
    print("Comiendo")

  def dormir(self):
    print("Durmiendo")

class Mascota:
  def fecha_adopcion(self, fecha):
    self.fecha_de_adopcion = fecha

class Perro(Animal, Mascota):
  def __init__(self, nombre):
    self.nombre = nombre

  def ladrar(self):
    print("Ladrando")

  def dormir(self):
    print(self.nombre, "esta durmiendo!")
    Animal.dormir(self)
    print("No molestar")

firulais = Perro("Firulais")
firulais.dormir()

