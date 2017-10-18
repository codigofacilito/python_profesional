def suma(parametro_requerido,*args):
  total = 0
  print(parametro_requerido)
  for valor in args:
    total+=valor
  return total

def usuarios_autenticados(**kwargs):
  print(kwargs)

resultado = suma("Este es un argumento requerido",10, 20, 30, 40, 50, 60, 70)
print(resultado)

def combinacion(requerido, *args, **kwargs):
  print(requerido)
  print(args)
  print(kwargs)

combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)