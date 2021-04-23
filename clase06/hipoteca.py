# hipoteca.py
# Archivo 
# Ejercicio de hipoteca

# Ejercicio 1.11

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes_actual = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if mes_actual >= pago_extra_mes_comienzo and mes_actual <= pago_extra_mes_fin:
        # Solo hacemos el pago extra si todavia adeudamos más que un pago mensual + un pago extra
        if saldo - pago_extra - pago_mensual >= 0:
            saldo -= pago_extra
            total_pagado += pago_extra
    
    # Si lo adeudado es mayor al pago mensual, pagamos el total del pago del mes
    if saldo - pago_mensual >= 0:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    # Si lo adeudado es menos que el pago mensual, solo pagamos lo que nos queda de deuda
    else:
        total_pagado += saldo
        saldo -= saldo
        
    
    mes_actual += 1

    print(mes_actual, round(total_pagado, 2), round(saldo, 2))

print('Total pagado:', round(total_pagado, 2))
print('Meses:', mes_actual)


# Ejercicio 1.7

#saldo = 500000.0
#tasa = 0.05
#pago_mensual = 2684.11
#total_pagado = 0.0
#while saldo > 0:
    #saldo = saldo * (1+tasa/12) - pago_mensual
    #total_pagado = total_pagado + pago_mensual

#print('Total pagado', round(total_pagado, 2))


# Ejercicio 1.8

#saldo = 500000.0
#tasa = 0.05
#pago_mensual = 2684.11
#total_pagado = 0.0
#adelanto = 1000
#mes = 0

#while saldo > 0:
    #if mes < 12:
        #saldo -= adelanto
        #total_pagado += adelanto

    #saldo = saldo * (1+tasa/12) - pago_mensual
    #total_pagado = total_pagado + pago_mensual
    #mes += 1

#print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')


# Ejercicio 1.9

#saldo = 500000.0
#tasa = 0.05
#pago_mensual = 2684.11
#total_pagado = 0.0
#mes_actual = 0
#pago_extra_mes_comienzo = 61
#pago_extra_mes_fin = 108
#pago_extra = 1000

#while saldo > 0:
    #if mes_actual >= pago_extra_mes_comienzo and mes_actual <= pago_extra_mes_fin:
          #saldo -= pago_extra
          #total_pagado += pago_extra

    #saldo = saldo * (1+tasa/12) - pago_mensual
    #total_pagado = total_pagado + pago_mensual
    #mes_actual += 1
    

#print('Total pagado', round(total_pagado, 2), 'en', mes_actual, 'meses')


# Ejercicio 1.10

#saldo = 500000.0
#tasa = 0.05
#pago_mensual = 2684.11
#total_pagado = 0.0
#mes_actual = 0
#pago_extra_mes_comienzo = 61
#pago_extra_mes_fin = 108
#pago_extra = 1000

#while saldo > 0:
    #if mes_actual >= pago_extra_mes_comienzo and mes_actual <= pago_extra_mes_fin:
          #saldo -= pago_extra
          #total_pagado += pago_extra

    #saldo = saldo * (1+tasa/12) - pago_mensual
    #total_pagado = total_pagado + pago_mensual
    #mes_actual += 1

    #print(mes_actual, round(total_pagado, 2), round(saldo, 2))

#print('Total pagado:', round(total_pagado, 2))
#print('Meses:', mes_actual)