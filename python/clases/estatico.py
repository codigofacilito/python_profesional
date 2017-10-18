class Triangulo:

  numero = 2

  @staticmethod
  def area(base, altura):
    return (base * altura) / Triangulo.numero


resultado = Triangulo.area(10, 20)
print(resultado)