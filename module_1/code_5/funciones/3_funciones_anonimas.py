# Funciones anonimas
# Son funciones que no tienen unnombre asociado
# Se definen con la palabra reservada lambda

# comentar ctrl + k + c
# descomentar ctrl + k + u
# copiar la misma línea = alt + shift + UpArrow or DownArrow
# desplazar línea hacia arriba o abajo = alt + UpArrow or DownArrow

def sumar(a,b):
    return  a + b

sumar_2 = lambda a,b: a +b

print(sumar(2,3))
print(sumar_2(2,3))


multiplicar = lambda a,b: a*b
print(multiplicar(2,3))

division = lambda a,b: a / b if (b!=0) else "No se puede dividir"
print(division(6,2))
print(division(6,0))