# 🐍 Guía para Usar MetaTrader5 con Python en Windows (PowerShell)

Esta guía está diseñada para que cualquier persona, incluso sin experiencia en programación, pueda configurar y usar un proyecto de MetaTrader5 con Python en Windows usando PowerShell. Instalaremos Python 3.8, Poetry y todo lo necesario de forma sencilla y paso a paso. ¡Empecemos!

## ✅ Requisitos Previos

- Tener **MetaTrader 5** instalado en tu computadora.
- Una carpeta para guardar el proyecto (sugerimos `Documentos\MT5-Python`).

## 🟦 Paso 1: Instalar Python 3.8

Python es el lenguaje que usaremos para conectar con MetaTrader5. Necesitamos la versión 3.8 porque es la más compatible con este proyecto.

1. Visita [python.org](https://www.python.org/downloads/release/python-3810/).
2. Descarga el instalador para Windows (busca "Windows x86-64 executable installer").
3. Ejecuta el instalador y **marca la casilla "Add Python 3.8 to PATH"** antes de hacer clic en "Install Now".
4. Cuando termine, abre PowerShell (busca "PowerShell" en el menú de inicio) y escribe:

   ```powershell
   python --version
   ```

   Deberías ver algo como "Python 3.8.x". Si no funciona, reinicia tu computadora y prueba de nuevo.

## 🟦 Paso 2: Instalar Poetry

Poetry es una herramienta que organiza las dependencias del proyecto. Es muy fácil de instalar.

1. Abre PowerShell.
2. Ejecuta este comando para instalar Poetry:

   ```powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Cierra PowerShell y abre una nueva ventana de PowerShell.
4. Verifica que Poetry esté instalado escribiendo:

   ```powershell
   poetry --version
   ```

   Si aparece un número de versión, ¡todo está listo!

## 📁 Paso 3: Descargar el Proyecto

1. Ve a la página del proyecto en GitHub (donde está el código).
2. Haz clic en el botón verde **"Code"** y selecciona **"Download ZIP"**.
3. Descomprime el archivo ZIP en una carpeta fácil de encontrar, como:
   - `C:\Users\TuUsuario\Documentos\MT5-Python`

## 🔧 Paso 4: Configurar la Conexión a MetaTrader5

El proyecto necesita saber dónde está MetaTrader5 en tu computadora. Vamos a configurarlo.

1. En la carpeta del proyecto, busca un archivo llamado `.env.example`.
2. Haz una copia de este archivo y renómbralo como `.env` (elimina el ".example").
3. Abre el archivo `.env` con un editor de texto:
   - Usa Notepad (clic derecho > "Abrir con" > "Bloc de notas").
4. Cambia la línea `MT5_PATH` para que apunte a donde está MetaTrader5:
   - Por defecto en Windows:

     ```env
     MT5_PATH=C:/Program Files/MetaTrader 5/terminal64.exe
     ```

     Si lo instalaste en otro lugar, ajusta la ruta.
5. Opcional: Si tienes una cuenta de MetaTrader5, puedes añadir tu `LOGIN` y `PASSWORD` en el archivo `.env`.
6. Guarda el archivo y ciérralo.

## 🧪 Paso 5: Preparar el Entorno

Ahora instalaremos las herramientas que el proyecto necesita.

1. Abre PowerShell.
2. Navega a la carpeta del proyecto:

   ```powershell
   cd C:\Users\TuUsuario\Documentos\MT5-Python
   ```

3. Instala las dependencias con:

   ```powershell
   poetry install
   ```

   Esto puede tardar unos minutos, pero solo lo harás una vez.

## ▶️ Paso 6: Ejecutar el Script

¡Ya casi terminamos! Vamos a probar el proyecto.

1. En la misma ventana de PowerShell, ejecuta:

   ```powershell
   poetry run python main.py
   ```

2. Si todo está bien, verás mensajes que indican que se conectó a MetaTrader5 y algunos datos del mercado (como el RSI de EURUSD).

## 🧠 Consejos Útiles

- **Error con `.env`**: Si aparece un error sobre `.env`, verifica que el archivo exista y que la ruta de `MT5_PATH` sea correcta.
- Si MetaTrader5 está en otra unidad (como D:), actualiza la ruta en `.env`, por ejemplo, `D:/Program Files/MetaTrader 5/terminal64.exe`.
- Si algo no funciona, revisa que todos los comandos anteriores se ejecutaron correctamente.
- Si los comandos de Poetry fallan, asegúrate de haber reiniciado PowerShell después de instalar Poetry.
