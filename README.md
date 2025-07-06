# 🐍 Entorno reproducible para MetaTrader5 con Python 3.8

## 🖥️ Paso previo: Preparar WSL en Windows

1. Abre el menú de Windows y busca **"Características de Windows"**.
2. Activa la opción **"Subsistema de Windows para Linux (WSL)"**.
3. Reinicia tu equipo si es necesario.
4. Ve a la Microsoft Store, busca **Ubuntu** e instálalo.
5. Abre Ubuntu desde el menú Inicio y deja que termine la configuración inicial.

## ✅ Requisitos previos

- Un PC con **Windows 10 o 11**
- Tener instalado **MetaTrader 5**

## 🟦 Paso 1: Instalar Nix en Windows

Antes de continuar, necesitas instalar Nix en tu PC con Windows. La forma más sencilla y recomendada es usando **Determinate Nix**.

1. Abre una terminal (por ejemplo, Ubuntu en WSL).
2. Ejecuta el siguiente comando:

   ```sh
   curl -fsSL https://install.determinate.systems/nix | sh -s -- install --determinate
   ```

3. Sigue las instrucciones que aparecen en pantalla.
4. Una vez instalado, abre una terminal nueva para asegurarte de que Nix está disponible.

> Más información y guía oficial: [https://docs.determinate.systems/](https://docs.determinate.systems/)

## 📁 Paso 2: Descargar este proyecto

1. Entra a la página del proyecto en GitHub.
2. Haz clic en el botón verde "Code" → "Download ZIP".
3. Extrae el archivo ZIP en tu carpeta de documentos (por ejemplo: `Documentos/MT5-Python`).

No necesitas instalar Git ni usar comandos para esto.

## 🔧 Paso 3: Configurar la conexión a MetaTrader5

1. Entra en la carpeta que descomprimiste.
2. Haz una copia del archivo `.env.example` y renómbralo como `.env`.
3. Abre `.env` con un editor de texto (como Notepad) y modifica la siguiente línea:

   ```env
   MT5_PATH=/mnt/c/Program Files/MetaTrader 5/terminal64.exe
   ```

   Asegúrate de que la ruta apunte al ejecutable de MetaTrader 5.

## 🧪 Paso 4: Activar el entorno de desarrollo

1. Abre la terminal de tu preferencia (por ejemplo, CMD o PowerShell).
2. Navega a la carpeta del proyecto:

   ```sh
   cd "C:\Usuarios\TuUsuario\Documentos\MT5-Python"
   ```

3. Ejecuta el comando para preparar el entorno (ajusta según tu gestor de entornos preferido, por ejemplo, con Poetry o pip):

   ```sh
   poetry install
   ```

## ▶️ Paso 5: Ejecutar el script

Una vez dentro del entorno, ejecuta:

```sh
poetry run python main.py
```

## 📄 Estructura del proyecto

```
mt5-python-project/
├── flake.nix           # Configuración del entorno con Nix
├── pyproject.toml      # Lista de librerías usadas con Poetry
├── main.py             # Script principal que se conecta a MT5
├── .env.example        # Plantilla de configuración
└── README.md           # Esta guía
```

## 📚 ¿Qué hace este proyecto?

- Carga MetaTrader 5 desde el script Python
- Extrae datos de mercado
- Puede graficar, analizar o guardar información en Excel
- Todo dentro de un entorno portátil y reproducible

## 🧠 Consejos útiles

- Si al ejecutar ves un error sobre `.env`, asegúrate de que el archivo `.env` exista y contenga la ruta correcta a MT5.
- Si tu MetaTrader está en otro disco o carpeta, ajusta la ruta en `.env` usando la letra de tu unidad correspondiente.

## 🚀 ¿Y después?

Puedes modificar `main.py` para hacer análisis, gráficos o automatizaciones con tus datos financieros.

Este entorno está preparado para usarse sin conocimientos técnicos.
