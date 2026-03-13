# Parametros en funciones
# Una función puede recibir parámetros para trabajar con datos externos.
# Los parámetros se definen entre los paréntesis de la definición de la función.

def potencia(base,exponente=2):
    return base**exponente

print(potencia(3))
print(potencia(3,4))

def operaciones(a,b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = operaciones(3,5)
print(f"La suma es : {resultado_suma}")
print(f"La resta es: {resultado_resta}")


# Parametos ARGS y KWARGS
def sumar_todos(*args):
    print(args)
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(sumar_todos(1,2,3))
print(sumar_todos(10,20))


def calculadora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'suma':
        return kwargs['a'] + kwargs['b']
    elif kwargs['operacion'] == 'resta':
        return kwargs['a'] - kwargs['b']
    else:
        return 'operacion incorrecta ...'
    
    
resultado_1 = calculadora(operacion='suma', a=10, b=5)
resultado_2 = calculadora(operacion='resta', a=10, b=5)  

print(f"Resultado 1 es : {resultado_1}") 
print(f"Resultado 2 es : {resultado_2}") 