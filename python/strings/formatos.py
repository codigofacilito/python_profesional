curso = "Python"
version = "3"

#resultado = "Curso de %s %s" %(curso, version)
resultado = "Curso de {a} {b}".format(b=version, a=curso)

print(resultado)