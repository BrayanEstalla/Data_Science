# Funciones para maximos, minimos y ordenamiento en listas

numeros = [5,3,4,7,2]
print("La lista de números son :", numeros)

# obtener el mayor
mayor = max(numeros)
print("el mayor es : ", mayor)

# obtener el menor
menor = min(numeros)
print("el menor es : ", menor)

# Lista ordenada
lista_ordenada = sorted(numeros)
print("lista ordenada : ", lista_ordenada)


# Lista ordenada desendente
lista_ordenada_des = sorted(numeros, reverse=True)
print("lista ordenada descendente: ", lista_ordenada_des)
