lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separador = "; "

resultado = lenguajes.split(separador) #resultado es una lista

nuevo_string = separador.join(resultado)

texto = """Este es un texto
con
saltos
de

línea"""

resultado = texto.splitlines()
print(resultado)