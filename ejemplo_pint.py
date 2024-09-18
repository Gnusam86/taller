from pint import UnitRegistry
ureg = UnitRegistry()
longitud = 5 * ureg.meter
longitud_en_pies = longitud.to('feet')

velocidad = 10 * ureg.meter / ureg.second
tiempo = 30 * ureg.second
distancia = velocidad * tiempo
ureg.define('manzana = 100 * meter * meter')
area= 2 * ureg.manzana
print(area.to('kilometer**2'))

print(distancia)
print(longitud_en_pies)
