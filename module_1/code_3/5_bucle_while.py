#   BUCLE WHILE

''' 
contador =1
while(contador < 10):
    print(contador)
    contador += 1
'''

contador =1
numero_adivinar = 5
print("Adivina que número estoy pensando")

while contador != numero_adivinar:
    contador = int(input())
    if contador == numero_adivinar:
        print("Ganaste")
    else:
        print("Intenta otra vez")

         