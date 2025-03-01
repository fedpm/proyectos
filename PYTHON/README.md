python -m nombre_del_modulo [argumentos]

# Creo el ambiente

python -m venv nombre_del_entorno

Crea un entorno virtual en la carpeta nombre_del_entorno


# Para activar un entorno virtual

nombre_del_entorno\Scripts\activate

# Para desactivar un entorno virtual

deactivate

# Con el entorno crado puedo instalar paquetes con 

pip install nombre_del_paquete


# También se pueden crear entornos con pipenv

- primero hay que instalar pipenv

pip install pipenv


pipenv install                             // creao entorno virtual
pipenv shell                               // activo entorno virtual
pipenv install langchain                   // instalo langchain 
pipenv install black                       // instalo Code Formater
exit                                       // salgo entorno virtual


# Ver paquetes instalados en entorno virtual o global segun este activado o no

pip list

pip show nombre_del_paquete                // veo donde esta instalado el paquete y con la ruta puedo saber si es un entorno global o no


# Ver paquetes con pipenv

pipenv graph                              // Muestra todos los paquetes instalados y sus dependencias.
pipenv run pip list                       // Muestra una lista simple de los paquetes instalados (solo los principales)
cat Pipfile                               // Muestra las dependencias principales definidas en el Pipfile.
cat Pipfile.lock                          // Muestra las versiones exactas de todas las dependencias instaladas.


# Entorno virtual en python

- Verificar que exista el entorno virtual
- Abrir la carpeta
- Elegir el interprete python que esta bajo 

Abre la Paleta de comandos:

Presiona Ctrl + Shift + P (Windows/Linux) o Cmd + Shift + P (macOS).

Escribe y selecciona Python: Select Interpreter.

Busca el intérprete asociado a tu entorno virtual. Este suele tener un nombre como:

nombre_del_entorno\Scripts\python.exe (Windows).

Selecciona el intérprete correcto.

para activarlo abrir una terminal dentro de vscode y activarlo


# Que quede seteado automaticamente en visual studio code

Si quieres que VS Code active automáticamente el entorno virtual cada vez que abras el proyecto, puedes agregar una configuración en el archivo .vscode/settings.json:

Abre la Paleta de comandos (Ctrl + Shift + P o Cmd + Shift + P).

Escribe y selecciona Preferences: Open Workspace Settings.

Busca la opción Python: Terminal Activate Environment y asegúrate de que esté habilitada.

También puedes agregar manualmente la ruta del intérprete en el archivo .vscode/settings.json:

json
Copy
{
  "python.pythonPath": "ruta/al/entorno/virtual/bin/python"
}
En Windows, la ruta sería algo como: nombre_del_entorno\Scripts\python.exe.

Nota : 

Pipenv almacena los entornos virtuales en una ubicación centralizada por defecto.
Usa pipenv --venv para encontrar la ruta del entorno virtual.
Selecciona el intérprete correcto en VS Code usando Python: Select Interpreter.
Activa el entorno virtual en la terminal integrada con pipenv shell.
Si prefieres tener el entorno virtual dentro del proyecto, configura PIPENV_VENV_IN_PROJECT.


# Hay otro entorno de ambientes que es anaconda


# Luego cree el archivo .env con las variables de ambiente que voy a necesitar
# Posteriormente presionando el debbuger de vscode cree un archivo launch.json para el proyecto python activo
# en el archivo lauch.json le agregue el archivo de enviroment agregando al json 
# "envFile": "${workspaceFolder}/.env"
# Luego cambie el nombre del proyecto por uno mas apropiado

#Luego instale load_dotenv para leer .env
from dotenv import load_dotenv

#Prompt Template

from langchain.prompts import PromptTemplate

# Sirve para crear un wrapper alrededor de un prompt de forma de pasar variables

pip install chromadb
pip install pypdf
