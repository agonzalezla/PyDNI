![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-blue)
# PyDNI

PyDNI es un módulo de Python que permite validar y generar identificadores españoles:
DNI, NIE, CIF y NIF, así como generar personas ficticias válidas para uso en desarrollo y pruebas.

Incluye validación, generación aleatoria y un motor de pruebas completo con pytest.


## Características principales

### Validación
- Verificación de DNI
- Verificación de NIE
- Verificación de CIF
- Verificación de NIF genérico (detecta DNI / NIE / CIF)
- Función unificada `verificar_identificador()` para auto-detección

### Generación
A través de la clase `Generator`:
- Generación de DNI válidos
- Generación de NIE válidos
- Generación de CIF válidos
- Generación de lotes (`generar_varios()`) sin duplicados
- Generación de nombres completos:
  - masculino, femenino o aleatorio
  - compatible con nombres compuestos
  - dos apellidos no repetidos
- Generación de personas completas:
  - nombre completo
  - tipo de documento
  - número de documento válido

### Estructura modular
Código limpio, organizado y fácil de integrar en otros proyectos.

## Instalación desde el repositorio

```bash
pip install .
```

(Ejecuta este comando en la carpeta donde esté el `setup.py` del paquete.)

Si prefieres usarlo directamente sin instalarlo, puedes importarlo desde el directorio:

```python
from PyDNI import verificar_dni, verificar_cif, verificar_identificador
```

## Instalacion con pip desde PyPI
```bash
pip install PyDNI
```
https://pypi.org/project/PyDNI/

## Uso básico

```python
from PyDNI import verificar_dni, verificar_cif, verificar_identificador, Generator

gen = Generator()

# Verificar un DNI
print(verificar_dni("12345678Z"))   # True

# Verificar un CIF
print(verificar_cif("A58818501"))   # True

# Detección automática
print(verificar_identificador("12345678Z"))   # "DNI válido"
print(verificar_identificador("A58818501"))   # "CIF válido"

# Generación de documentos
print("DNI:", gen.generar_dni())
print("NIE:", gen.generar_nie())
print("CIF:", gen.generar_cif())

# Generación múltiple (sin duplicados)
print("AUTO x5:", gen.generar_varios(5, "AUTO"))

# Generación de nombres
print("Nombre masculino:", gen.generar_nombre("masculino"))
print("Nombre femenino:", gen.generar_nombre("femenino"))
print("Nombre aleatorio:", gen.generar_nombre("aleatorio"))

# Generación de personas completas ---
persona = gen.generar_persona()
print("Persona completa:", persona)
```

## Estructura del paquete

```
PyDNI/
├── .gitignore              # Archivos y carpetas que Git debe ignorar (ej. entornos, builds, cache)
├── CHANGELOG.md            # Registro de cambios por versión (historial de mejoras, fixes, nuevas features)
├── LICENSE                 # Licencia del proyecto (MIT)
├── README.md               # Documentación principal: descripción, instalación, uso y ejemplos
├── setup.py                # Script de configuración para instalar el paquete (PyPI)
├── test.py                 # Script rápido/manual para probar funciones básicas del paquete
│
├── PyDNI/                  # Carpeta principal del paquete (código fuente)
│   ├── __init__.py         # Inicializa el paquete y expone funciones principales
│   ├── dni.py              # Lógica de validación de DNI
│   ├── cif.py              # Lógica de validación de CIF
│   ├── nie.py              # Lógica de validación de NIE
│   ├── nif.py              # Lógica de validación de NIF
│   ├── utils.py            # Funciones auxiliares
│   └── generator.py        # Generador de datos aleatorios
│
├── tests/                  # Carpeta con tests unitarios usando pytest
│   ├── test_dni.py         # Tests para verificar la función de DNI
│   ├── test_nie.py         # Tests para verificar la función de NIE
│   ├── test_cif.py         # Tests para verificar la función de CIF
│   ├── test_nif.py         # Tests para verificar la función de NIF genérico
│   ├── test_nombres.py     # Tests generador de nombres y apellidos
│   ├── test_generar_persona.py # Tests generacion de una persona completa
│   └── test_utils.py       # Tests para verificar la función unificada de utils
│
└── tools/                  # Scripts auxiliares (ej. automatización, publicación, CI/CD, utilidades)

```

## Requisitos

- Python 3.10 o superior
- No requiere dependencias externas

## Test rápido

Ejecuta el archivo `test.py` incluido:

```bash
python test.py
```

Deberías ver algo como:

```
===== TESTS RÁPIDOS DE VALIDACIÓN =====

DNI 12345678Z (válido): True
NIE X1234567L (válido): True
CIF A58818501 (válido): True

===== TESTS NIF GENÉRICO =====

verificar_nif('12345678Z') → DNI válido
verificar_nif('X1234567L') → NIE válido
verificar_nif('A58818501') → CIF válido

===== TESTS AUTOMÁTICOS =====

Auto (DNI): DNI válido
Auto (CIF): CIF válido
Auto (NIE): NIE válido

===== TESTS GENERACIÓN =====

Generar DNI: 69487115K
Generar NIE: X1696965W
Generar CIF: L1722668I

Generar 10 AUTO: ['06534924A', 'Y2741161N', 'Y5995450P', 'J82715343', '03564494T', '68554386B', 'A74055153', 'Z1300847H', '98083304B', '74821854W']

===== TESTS GENERACIÓN DE NOMBRES =====

Nombre masculino: MOHAMMED REYES DOMINGUEZ
Nombre femenino: SARA LOZANO FLORES
Nombre aleatorio: ENCARNACION MOLINA FERRER
Nombre sin parámetros: LOURDES MUÑOZ CRESPO

===== TESTS GENERACIÓN DE PERSONAS =====

Persona aleatoria: {'nombre': 'EMILIA PEÑA GOMEZ', 'sexo': 'femenino', 'tipo_documento': 'DNI', 'documento': '36131092R'}
Persona masculina: {'nombre': 'FRANCISCO BRAVO NAVARRO', 'sexo': 'masculino', 'tipo_documento': 'CIF', 'documento': 'N4325478H'}
Persona con DNI: {'nombre': 'MARIA ISABEL PRIETO HERNANDEZ', 'sexo': 'femenino', 'tipo_documento': 'DNI', 'documento': '15742334F'}
Persona con NIE femenina: {'nombre': 'SOLEDAD PASTOR FUENTES', 'sexo': 'femenino', 'tipo_documento': 'NIE', 'documento': 'X7092186K'}
```
## Tests unitarios

Este proyecto incluye tests unitarios con pytest.  
Para ejecutarlos, asegúrate de tener instalado `pytest`:

```bash
pip install pytest
```
Luego, desde la raíz del proyecto:
```bash
 python -m pytest tests -v
 ```

Ejemplo de salida:
```bash
collected 46 items

tests/test_cif.py::test_cif_valido_telefonica PASSED                                                                                                 [  2%]
tests/test_cif.py::test_cif_valido_ayuntamiento_madrid PASSED                                                                                        [  4%]
tests/test_cif.py::test_cif_invalido PASSED                                                                                                          [  6%]
tests/test_dni.py::test_dni_valido PASSED                                                                                                            [  8%]
tests/test_dni.py::test_dni_invalido_letra PASSED                                                                                                    [ 10%]
tests/test_dni.py::test_dni_invalido_formato PASSED                                                                                                  [ 13%]
tests/test_generar_persona.py::test_generar_persona_estructura PASSED                                                                                [ 15%]
tests/test_generar_persona.py::test_generar_persona_nombre_valido PASSED                                                                             [ 17%]
tests/test_generar_persona.py::test_generar_persona_documento_valido PASSED                                                                          [ 19%]
tests/test_generar_persona.py::test_generar_persona_masculina PASSED                                                                                 [ 21%]
tests/test_generar_persona.py::test_generar_persona_femenina PASSED                                                                                  [ 23%]
tests/test_generar_persona.py::test_generar_persona_con_dni PASSED                                                                                   [ 26%]
tests/test_generar_persona.py::test_generar_persona_con_nie PASSED                                                                                   [ 28%]
tests/test_generar_persona.py::test_generar_persona_con_cif PASSED                                                                                   [ 30%]
tests/test_generar_persona.py::test_generar_persona_sexo_aleatorio PASSED                                                                            [ 32%]
tests/test_generar_persona.py::test_generar_persona_tipo_aleatorio PASSED                                                                            [ 34%]
tests/test_generar_persona.py::test_generar_persona_sexo_invalido PASSED                                                                             [ 36%]
tests/test_generar_persona.py::test_generar_persona_tipo_documento_invalido PASSED                                                                   [ 39%]
tests/test_generator.py::test_generar_dni_formato PASSED                                                                                             [ 41%]
tests/test_generator.py::test_generar_dni_valido PASSED                                                                                              [ 43%]
tests/test_generator.py::test_generar_nie_formato PASSED                                                                                             [ 45%]
tests/test_generator.py::test_generar_nie_valido PASSED                                                                                              [ 47%]
tests/test_generator.py::test_generar_cif_formato PASSED                                                                                             [ 50%]
tests/test_generator.py::test_generar_cif_valido PASSED                                                                                              [ 52%]
tests/test_generator.py::test_generar_varios_dni_sin_repetidos PASSED                                                                                [ 54%]
tests/test_generator.py::test_generar_varios_nie_sin_repetidos PASSED                                                                                [ 56%]
tests/test_generator.py::test_generar_varios_cif_sin_repetidos PASSED                                                                                [ 58%]
tests/test_generator.py::test_generar_varios_auto_varios_tipos PASSED                                                                                [ 60%]
tests/test_nie.py::test_nie_valido PASSED                                                                                                            [ 63%]
tests/test_nie.py::test_nie_invalido_letra_control PASSED                                                                                            [ 65%]
tests/test_nie.py::test_nie_invalido_formato PASSED                                                                                                  [ 67%]
tests/test_nif.py::test_nif_dni_valido PASSED                                                                                                        [ 69%]
tests/test_nif.py::test_nif_nie_valido PASSED                                                                                                        [ 71%]
tests/test_nif.py::test_nif_cif_valido PASSED                                                                                                        [ 73%]
tests/test_nif.py::test_nif_invalido PASSED                                                                                                          [ 76%]
tests/test_nombres.py::test_generar_nombre_masculino PASSED                                                                                          [ 78%]
tests/test_nombres.py::test_generar_nombre_femenino PASSED                                                                                           [ 80%]
tests/test_nombres.py::test_generar_nombre_aleatorio PASSED                                                                                          [ 82%]
tests/test_nombres.py::test_generar_nombre_sin_parametro_es_aleatorio PASSED                                                                         [ 84%]
tests/test_nombres.py::test_generar_nombre_formato_correcto PASSED                                                                                   [ 86%]
tests/test_nombres.py::test_generar_nombre_apellidos_distintos PASSED                                                                                [ 89%]
tests/test_nombres.py::test_generar_nombre_sexo_invalido PASSED                                                                                      [ 91%]
tests/test_utils.py::test_identificador_dni PASSED                                                                                                   [ 93%]
tests/test_utils.py::test_identificador_nie PASSED                                                                                                   [ 95%]
tests/test_utils.py::test_identificador_cif PASSED                                                                                                   [ 97%]
tests/test_utils.py::test_identificador_formato_invalido PASSED                                                                                      [100%]

=================================================================== 46 passed in 0.11s ====================================================================
```

## Autor

**Alberto Gonzalez**  
agonzalezla@protonmail.com  

## Licencia

Este proyecto se distribuye bajo la licencia MIT.  
Consulta el archivo `LICENSE`