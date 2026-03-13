# LISTAS
# Una lista es una coleccióm ordenada y mutable de elementos
# Se definen utilizando corchetes [] y los elementos están separados por comas
# en otros lenguajes se llaman arrays



dias = ["lunes","martes","miercoles","jueves","viernes"]
print("la lista contienen: ", dias)
print("el primer día es:", dias[0])
print("los dos primeros dias son:", dias[0:2])
print("el ultimo día es: ", dias[-1])
print("el ultimo día es: ", dias[4])

# AGREGAR
dias.append("sabado")
dias.append("domingo")
print("la lista actualizada es: ", dias)

# BORRAR
dias.pop()
#dias.pop(5)
dias.pop(4)
print("la lista actualizada es:", dias)

# MODIFICAR
dias[4] = "viernes"
print("la lista actualizada es:", dias)

# RECOGER UNA LISTA
print("***metodo 1***")
for contador in range(len(dias)):
    
    print(dias[contador])

print("***metodo 2***")  
for dia in dias:

    print(dia)