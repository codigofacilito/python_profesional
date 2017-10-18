def comenzar_play_list(lista):

  def reproducir():
    nonlocal lista
    lista = [1,2,3]
    for val in lista:
      print(val)

  reproducir()
  print(lista)

lista = ['track 1', 'track 2', 'track 3', 'track 4']
comenzar_play_list(lista)