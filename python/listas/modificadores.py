cursos = ["python", "django", "flask", "c", "c++", "c#", "java", "php"]
nuevos_cursos = ["Go", "Android"]

cursos[0] = "python3"

#Ingresar elemento
cursos.append("JS")
cursos.insert(4, "MongoDb")
cursos.extend(nuevos_cursos)

#Eliminar elementos
cursos.remove("c")
del cursos[0]
valor_eliminado = cursos.pop(1)

cursos.clear()

print(cursos)