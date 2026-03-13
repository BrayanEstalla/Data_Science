#  CALCULATOR
import math
salir = "no"

while salir == "no":
    
    print("================ CALCULADORA CON PYTHON ============")
    print("========= OPCIONES ========")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. tabla de multiplicar")
    print("6. raiz cuadrada")
    opcion = int(input("Ingrese la opcion que desea: "))
    
    if opcion  >=1 and opcion <=4:
        num_1 = int(input("numero 1: "))
        num_2 = int(input("numero 2: "))
        
        if opcion == 1:
            operacion = "suma"
            resultado = num_1 + num_2
        elif opcion == 2:
            operacion = "resta"
            resultado = num_1 - num_2
        elif opcion == 3:
            operacion = "multiplicacion"
            resultado = num_1 * num_2
        else:
            operacion = "división"
            resultado = num_1  / num_2
        
        print(f"La {operacion} de {num_1} y {num_2} es {resultado}")
        
        
    elif opcion == 5:
        tabla = int(input("Ingresa un valor de la tabla: "))
        for contador in range(1,13,1):
            resultado = tabla * contador
            print(f"{tabla} x {contador} = {resultado}") 
             
    elif opcion == 6:
         numero = int(input("Ingrese el número para calcular su raiz cuadrada: "))
         raiz = math.sqrt(numero)
         print(f"La raiz cuadrada de {numero} es {raiz}")
    else:
        print("Opción no valida...")
                 
    
    
    
    salir = input("¿Desea salir del programa? (si o no) ")
    if salir == "si":
        print("Saliendo de programa")
        break