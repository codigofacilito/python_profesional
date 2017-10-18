def mostrar_mensaje(mensaje):
  mensaje = mensaje.title() #local
  
  def mostrar():
    print(mensaje)

  return mostrar


nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()