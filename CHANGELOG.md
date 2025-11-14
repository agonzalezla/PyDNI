# Changelog

Todas las versiones importantes de este proyecto se documentan aquí.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/)
y el proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

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