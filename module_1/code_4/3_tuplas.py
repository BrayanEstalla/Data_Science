# TUPLAS
# Son inmutables, no se pueden modificar
# Se definen utilizando paréntesis () y los elementos están separados por comas.


dias = ("lunes","martes","miercoles","jueves","viernes")
print(type(dias))
print("los datos que contiene esta tupla son: ", dias)
print("el primer día es:", dias[0])
print("los dos primeros dias son:", dias[0:2])
print("el ultimo día es: ", dias[-1])
print("el ultimo día es: ", dias[4])

# Esto generará un error porque las tuplas son inmutables
#dias.append("sabado")

# ¿Cuándo se deben usar tuplas en vez de listas?
# Cuando no se necesite modificar la colección de datos
# Cuando se requiere asegurar que los datos permanezcan constantes
# Cuando se busca optimizar el rendimiento, ya que las tuplas son más rápidas que las listas


# Agregar elementos a una tupla
dias = list(dias)
print(type(dias))
dias.append("sabado")
dias.append("domingo")

dias = tuple(dias)
print(type(dias))
print(dias)

# recorrer una tupla
for dia in dias:
    print(dia)
