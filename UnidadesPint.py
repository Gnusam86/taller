from pint import UnitRegistry

ureg = UnitRegistry()

# Imprimir todas las unidades definidas en el registro
for dimension, units in ureg._units.items():
    print(f"Dimensión: {dimension}")
    for unit_name, unit in units.items():
        print(f"  - {unit_name}: {unit.definition}")