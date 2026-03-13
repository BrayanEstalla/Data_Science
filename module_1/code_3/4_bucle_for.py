#BUCLE FOR

''' 
for contador in range(10):
    print(contador)
'''


''' 
for contador in range(3,22,3):
    print(contador)
'''    

tabla = int(input("Ingresa un valor de la tabla: "))
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")