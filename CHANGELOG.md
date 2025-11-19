# Changelog

Todas las versiones importantes de este proyecto se documentan aquí.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/)
y el proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [0.5.1] - 2025-11-14
### Fixed
- Corrección de los tests unitarios para soportar nombres compuestos (ej. “Ana María”, “María del Carmen”).
- Actualización del script de tests rápidos para incluir generación de nombres y personas completas.

## [0.5.0] - 2025-11-19
### Added
- Nueva función `generar_nombre()` dentro de la clase `Generator`, capaz de:
  - Generar nombres masculinos, femeninos o aleatorios.
  - Añadir automáticamente dos apellidos.
  - Manejar apellidos aleatorios sin repetición.
- Integración total en `Generator` para uso unificado junto a la generación de DNI/NIE/CIF.
- Nueva función `generar_persona()` que construye una persona completa:
  - nombre completo
  - tipo de documento
  - número de documento válido
  - metadatos básicos del individuo

### Notes
- Los datos personales son falsos y no corresponden con personas reales, se generan de manera aleatoria y son válidos para pruebas y entornos de desarrollo.

## [0.4.0] - 2025-11-17
### Added
- Nueva clase `Generator` para crear números válidos de DNI, NIE y CIF con fines de prueba.
- Soporte para generación masiva sin documentos duplicados.
- Agregados los tests con pytest para el generador.

## [0.3.0] - 2025-11-14
### Added
- Tests unitarios con pytest (17 casos) cubriendo DNI, NIE, CIF, NIF y utilidades.

### Changed
- Actualización de versión del paquete a `0.3.0`.
- Reordenada la lógica en `utils.py` para detectar NIE antes que CIF.
- Mejora en la estructura del repositorio con carpeta `tests/` dedicada.

### Fixed
- Corrección en validación de CIF para organismos públicos (`Q`).
- Inclusión de excepciones conocidas en `cif.py` (ej. `Q2816003A` Ayuntamiento de Madrid).
- Todos los tests unitarios pasan correctamente (17/17).

## [0.2.0] - 2025-11-14
### Added
- Implementación de verificacion para NIE (Número de Identificación de Extranjeros).
- Nueva función `verificar_nie` para validar NIE con prefijo X/Y/Z y letra de control.
- Validación de NIF genérico:
- Nueva función `verificar_nif` que detecta y valida automáticamente DNI, NIE y CIF.
- Exportación de nuevas funciones en `__init__.py`.
- Extensión de `utils.py` para soportar los nuevos tipos de identificadores.

### Changed
- Actualización de versión del paquete a `0.2.0`.
- Ajustes menores en la estructura del repositorio para incluir `nie.py` y `nif.py`.

### Fixed
- Corrección en ejemplos de test: se añadieron casos válidos de CIF, DNI y NIE para evitar falsos negativos.

## [0.1.0] - 2025-11-13
### Version inicial
- Creación del paquete PyDNI
- Implementación de verificación de DNI español
- Implementación de verificación de CIF español
- Función unificada `verificar_identificador()` que detecta el tipo automáticamente
- Estructura de paquete Python con `setup.py`
- Añadido `test.py` para pruebas rápidas de validación