#Definir generador
def contador(maximo):
    conteo = 0
    while conteo < maximo:
        yield conteo
        conteo  += 1
        
#Usar el generador
for numero in contador(6):
    print(numero)