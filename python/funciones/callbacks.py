def promedio(lista_valores):
  total = 0
  for valor in lista_valores:
    total+=valor
  return total/len(lista_valores)

aprobatorio = lambda total, minimo=7 : True if total>=minimo else False

def mensaje_calificacion(calificaciones, func_promedio, func_aprobatorio):
  promedio = func_promedio(calificaciones)
  if func_aprobatorio(promedio):
    print("Felicitaciones")


calificaciones = [10, 9, 8, 7, 10]
mensaje_calificacion(calificaciones, promedio, aprobatorio)
