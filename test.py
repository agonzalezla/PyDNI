from PyDNI import (
    verificar_dni,
    verificar_cif,
    verificar_identificador,
    verificar_nie,
    verificar_nif,
    Generator
)

print("\n===== TESTS RÁPIDOS DE VALIDACIÓN =====\n")

print("DNI 12345678Z (válido):", verificar_dni("12345678Z"))
print("NIE X1234567L (válido):", verificar_nie("X1234567L"))
print("CIF A58818501 (válido):", verificar_cif("A58818501"))

print("\n===== TESTS NIF GENÉRICO =====\n")
print("verificar_nif('12345678Z') →", verificar_nif("12345678Z"))
print("verificar_nif('X1234567L') →", verificar_nif("X1234567L"))
print("verificar_nif('A58818501') →", verificar_nif("A58818501"))

print("\n===== TESTS AUTOMÁTICOS =====\n")
print("Auto (DNI):", verificar_identificador("12345678Z"))
print("Auto (CIF):", verificar_identificador("A58818501"))
print("Auto (NIE):", verificar_identificador("X1234567L"))

print("\n===== TESTS GENERACIÓN =====\n")
gen = Generator()

print("Generar DNI:", gen.generar_dni())
print("Generar NIE:", gen.generar_nie())
print("Generar CIF:", gen.generar_cif())

print("\nGenerar 10 AUTO:", gen.generar_varios(10, "AUTO"))

print("\n===== TESTS GENERACIÓN DE NOMBRES =====\n")
print("Nombre masculino:", gen.generar_nombre("masculino"))
print("Nombre femenino:", gen.generar_nombre("femenino"))
print("Nombre aleatorio:", gen.generar_nombre("aleatorio"))
print("Nombre sin parámetros:", gen.generar_nombre())

print("\n===== TESTS GENERACIÓN DE PERSONAS =====\n")
print("Persona aleatoria:", gen.generar_persona())
print("Persona masculina:", gen.generar_persona(sexo="masculino"))
print("Persona con DNI:", gen.generar_persona(tipo_doc="DNI"))
print("Persona con NIE femenina:", gen.generar_persona(sexo="femenino", tipo_doc="NIE"))

print("\n===== TESTS GENERACIÓN DE EMAILS =====\n")
print(gen.email_gen.generar_email_aleatorio())
print(gen.email_gen.generar_email_aleatorio("midominio.com"))
print(gen.email_gen.generar_email_nombre("María Ruiz Gómez", "empresa.com"))
print(gen.email_gen.generar_email("Ana García Fernández"))