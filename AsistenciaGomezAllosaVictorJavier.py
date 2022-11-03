#ejercicio cajero
saldo = 1000
print("...Programa Cajero...")
print("--¿Que accion desea realizar--")
print(" 1) Ingresar Dinero")
print(" 2) Retirar Dinero de la cuenta")
print(" 3) Mostrar Dinero disponible")
print(" 4) salir")
 
while True:
    num=int(input("Ingrese numero de opcion: "))
    if num == 1:
        ingreso=int(input("¿Cuanto desea ingresar: "))
        saldo += ingreso
    elif num == 2:
        egreso=int(input("¿Cuanto desea retirar: "))
        if egreso>saldo:
            print(f"No tiene saldo para esa operacion, su saldo actual es {saldo}, monto menor al que desea retirar")
        else:
            saldo -=egreso
    elif num == 3:
        print(f"Su saldo disponibles es {saldo}")
    elif num==4 :
        break
    else:
        print("elija una opcion")

      
