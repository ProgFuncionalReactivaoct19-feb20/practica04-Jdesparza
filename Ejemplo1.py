"""
	Jdesparza
"""
# para importar el archivo
import codecs
# para poder transformar en diccionarios
import json
# se llama al archivo con el uso de codecs
archivo = codecs.open("datos.txt", "r")
# para leer cada linea del archivo
lineas = archivo.readlines()
# para transformar cada linea del archivo en diccionarios 
lineas_diccionario = [json.loads(l) for l in lineas]
# para saber que jugadores han hecho mas de 3 goles
goles = filter(lambda x: list(x.items())[1][1] >= 3, lineas_diccionario)
# para saber que jugadores son del pais de Nigeria
pais = filter(lambda x: list(x.items())[0][1] == "Nigeria", lineas_diccionario)
# para ubicarme en la columna de los caracteres de height
maximo_minimo = lambda x: list(x.items())[2][1]
# se imprimen todos los resultados en forma de lista
print("\nLos que han hecho mas de tres goles son:\n")
print(list(goles))
print("\nLos del país de Nigeria son:\n")
print(list(pais))
print("\nEl valor máximo de Height es:\n")
# para imprimir solo el valor maximo que existe en Height
print(max(list(map(maximo_minimo, lineas_diccionario))))
print("\nEl valor mínimo de Height es:\n")
# para imprimir solo el valor minimo que existe en Height
print(min(list(map(maximo_minimo, lineas_diccionario))))