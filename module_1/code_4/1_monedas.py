'''
RETO 1 : CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA 
QUE PERMITA CONVERTIR EL VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA,
POR EJEMPLO SI INGRESO CONVERTIR SOLES A DOLARES E INGRESO 3000 SOLES 
DEBERIA MOSTRARME SU VALOR EN DOLARES QUE SERIA 1000 DOLARES CONSIDERANDO 
QUE EL TIPO DE CAMBIO ES 3
            =============================================
                        CONVERTIDOR DE MONEDAS
            =============================================
                    [1] CONVERTIR SOLES A DOLARES
                    [2] CONVERTIR DOLARES A SOLES
                    [3] SALIR
            =============================================
'''
import os
from time import sleep

#  Datos de entrada
TIPO_CAMBIO = 3 

while True :
    #os.system("clear")
    os.system("cls")
    print("""
          
            =============================================
                        CONVERTIDOR DE MONEDAS
            =============================================
                    [1] CONVERTIR SOLES A DOLARES
                    [2] CONVERTIR DOLARES A SOLES
                    [3] SALIR
            =============================================    
          
          """)
    
    opcion =int(input("Ingrese una opción"))
    
    if opcion == 1:
        MONEDA_ORIGEN = "SOLES"
        MONEDA_DESTINO = "DOLARES"
        print("Convertir de soles a dolares")
        monto_origen = float(input(f"Ingrese el monto en {MONEDA_ORIGEN} : "))
        monto_destino = round(monto_origen/TIPO_CAMBIO)
    elif opcion == 2:
        MONEDA_ORIGEN = "DOLARES"
        MONEDA_DESTINO = "SOLES"
        print("Convertin de dolares a soles")
        monto_origen = float(input(f"Ingrese el monto en {MONEDA_ORIGEN}"))
        monto_destino = round(monto_origen/TIPO_CAMBIO)
    elif opcion ==3:
        print("Gracias...")
        exit()
    else:
        print("Opción no valida...")
        exit()
    
    print(f"Resultado : {monto_origen} {MONEDA_ORIGEN} SON {monto_destino} {MONEDA_DESTINO}")
    sleep(3)  