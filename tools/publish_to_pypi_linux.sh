#!/bin/bash

echo "Creando entorno virtual: pydni-env"
python3 -m venv pydni-env

echo "Activando entorno virtual"
source pydni-env/bin/activate

echo "Actualizando pip"
pip install --upgrade pip

echo "Instalando build y twine"
pip install build twine

echo "Eliminando carpeta dist/ antigua si existe"
rm -rf dist

echo "Construyendo paquete PyDNI"
python -m build

echo "Subiendo paquete a PyPI (se te pedirá usuario y contraseña)"
twine upload dist/*

echo ""
echo "Publicación finalizada correctamente."
echo "Puedes desactivar el entorno virtual con: deactivate"