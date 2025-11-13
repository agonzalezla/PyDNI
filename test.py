from PyDNI import verificar_dni, verificar_cif, verificar_identificador

print("DNI 12345678Z:", verificar_dni("12345678Z"))
print("CIF A58818501:", verificar_cif("A58818501"))
print("Auto (DNI):", verificar_identificador("12345678Z"))
print("Auto (CIF):", verificar_identificador("A58818501"))
