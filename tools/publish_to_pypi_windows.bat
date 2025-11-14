@echo off
echo Creando entorno virtual: pydni-env
python -m venv pydni-env

echo Activando entorno virtual
call pydni-env\Scripts\activate

echo Actualizando pip
pip install --upgrade pip

echo Instalando build y twine
pip install build twine

echo Eliminando carpeta dist si existe
IF EXIST dist (
    rmdir /S /Q dist
)

echo Construyendo paquete PyDNI
python -m build

echo Subiendo paquete a PyPI
twine upload dist/*

echo.
echo Publicación finalizada correctamente.
echo Para salir del entorno virtual, escribe: deactivate
pause