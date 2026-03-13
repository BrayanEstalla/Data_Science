# ==========================================
# Ejercicio: Lista de números
# ==========================================

# Escribe un programa en Python que realice las siguientes tareas:
# 
# 1. Solicite al usuario ingresar 5 números enteros.
# 2. Guarde cada número en una lista.
# 3. Una vez ingresados todos los números, el programa debe:
#
#    - Mostrar la lista de números ingresados.
#    - Mostrar cuál es el número mayor.
#    - Mostrar cuál es el número menor.
#    - Mostrar la lista ordenada de mayor a menor.


# Mostrar la lista de números ingresados
numeros = []
for i in range(5):
    num = int(input(f"Ingrese un número {i+1} : " ))
    numeros.append(num)
    
print(f"Lista ingresada : {numeros}")


# Mostrar cuál es el número mayor 
mayor = numeros[0]
for i in numeros:
    if i > mayor:
        mayor = i

print(f"el mayor es : {mayor}")
    

# Mostrar cuál es el número menor 
menor = numeros[0]
for i in numeros:
    if i < menor:
        menor = i

print(f"el menor es : {menor}")



# Mostrar la lista ordenada de mayor a menor
# Método de burbuja

for i in range(len(numeros)):
    for j in range(len(numeros)-1):
        if numeros[j] < numeros[j + 1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
print("Lista ordenada : ", numeros)
      
