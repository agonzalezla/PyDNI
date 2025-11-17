from PyDNI import verificar_dni, verificar_cif, verificar_identificador, verificar_nie, verificar_nif
from PyDNI import Generator

print("DNI 12345678Z:", verificar_dni("12345678Z"))
print("CIF A58818501:", verificar_cif("A58818501"))
print("Auto (DNI):", verificar_identificador("12345678Z"))
print("Auto (CIF):", verificar_identificador("A58818501"))


print(verificar_dni("12345678Z"))   # True
print(verificar_nie("X1234567L"))   # True
print(verificar_cif("B12345678"))   # True
print(verificar_nif("X1234567L"))   # NIE válido
print(verificar_nif("12345678Z"))   # DNI válido
print(verificar_nif("A58818501"))   # CIF válido

# Pruebas generacion documentos
gen = Generator()
print(gen.generar_dni())
print(gen.generar_nie())
print(gen.generar_cif())
print(gen.generar_varios(100, "AUTO"))