'''
Ejercicio Nº 4 - Funciones - Calculadora de impuestos

crear una función para calcular el total a abonar incluyendo el impuesto IVA

Utilizar la siguiente fórmula: pago_ttl = pago_sin_impueto + pago_sin_impueto * (impuesto/100)

Pago sin impuesto: 1000
Valor del impuesto: 21%
Pago con impuesto: xxx
'''

# Función que permite calcular el pago total incluyendo el impuesto del 21%

def calcular_pago_ttl(pago_sin_impueto, impuesto):
    pago_ttl = pago_sin_impueto + pago_sin_impueto * (impuesto/100)
    return pago_ttl

# Ejecución de la función

pago_sin_impueto = float(input("Ingrese monto sin impuesto: $"))
impuesto = float(input("Ingrese el valor del impuesto a aplicar: "))
pago_con_impueto = calcular_pago_ttl(pago_sin_impueto, impuesto)
print(f"\nEl monto que debe abonar incluido el IVA del 21% es de: ${pago_con_impueto}")