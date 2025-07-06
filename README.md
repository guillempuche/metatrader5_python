# 🐍 Guía Simplificada para Usar MetaTrader5 con Python en Windows y macOS

Esta guía está diseñada para que cualquier persona, incluso sin experiencia en programación, pueda configurar y usar un proyecto de MetaTrader5 con Python en Windows o macOS. Vamos a instalar Python 3.8, Poetry y todo lo necesario de forma sencilla y paso a paso. ¡Empecemos!

## ✅ Requisitos Previos

- Tener **MetaTrader 5** instalado en tu computadora.
- Una carpeta donde guardar el proyecto (te sugerimos usar `Documentos/MT5-Python`).

## 🟦 Paso 1: Instalar Python 3.8

Python es el lenguaje que usaremos para conectar con MetaTrader5. Necesitamos la versión 3.8 porque es la que funciona mejor con este proyecto.

### Para Windows

1. Visita [python.org](https://www.python.org/downloads/release/python-3810/).
2. Descarga el instalador para Windows (busca "Windows x86-64 executable installer").
3. Abre el instalador y **marca la casilla "Add Python 3.8 to PATH"** antes de presionar "Install Now".
4. Cuando termine, abre el "Símbolo del sistema" (busca "cmd" en el menú de inicio) y escribe:

   ```
   python --version
   ```

   Deberías ver algo como "Python 3.8.x". Si no funciona, reinicia tu computadora y prueba de nuevo.

### Para macOS

1. Abre la Terminal (busca "Terminal" en Spotlight o en Launchpad).
2. Necesitamos una herramienta llamada Homebrew para instalar Python fácilmente. Si no la tienes, copia y pega esto en la Terminal:

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Sigue las instrucciones que aparecen.
3. Ahora instala Python 3.8 con:

   ```
   brew install python@3.8
   ```

4. Verifica que se instaló escribiendo:

   ```
   python3.8 --version
   ```

   Deberías ver "Python 3.8.x".

## 🟦 Paso 2: Instalar Poetry

Poetry es una herramienta que nos ayuda a organizar las piezas que necesita el proyecto. Es súper fácil de instalar.

### Para Windows

1. Abre el "Símbolo del sistema" (cmd).
2. Copia y pega este comando:

   ```
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Cierra el "Símbolo del sistema" y ábrelo de nuevo.
4. Escribe:

   ```
   poetry --version
   ```

   Si ves un número de versión, ¡todo está bien!

### Para macOS

1. Abre la Terminal.
2. Copia y pega este comando:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Para asegurarte de que Poetry funcione, añade esta línea (puedes necesitarlo):

   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

4. Verifica con:

   ```
   poetry --version
   ```

   Si aparece un número de versión, ¡listo!

## 📁 Paso 3: Descargar el Proyecto

1. Ve a la página del proyecto en GitHub (donde está el código).
2. Haz clic en el botón verde que dice **"Code"** y luego en **"Download ZIP"**.
3. Descomprime el archivo ZIP en una carpeta fácil de encontrar, como:
   - Windows: `C:\Users\TuUsuario\Documentos\MT5-Python`
   - macOS: `~/Documentos/MT5-Python`

## 🔧 Paso 4: Configurar la Conexión a MetaTrader5

El proyecto necesita saber dónde está MetaTrader5 en tu computadora. Vamos a configurarlo.

1. Dentro de la carpeta del proyecto, busca un archivo llamado `.env.example`.
2. Haz una copia de este archivo y renómbralo como `.env` (elimina el ".example").
3. Abre el archivo `.env` con un editor de texto:
   - Windows: Usa Notepad (clic derecho > "Abrir con" > "Bloc de notas").
   - macOS: Usa TextEdit.
4. Cambia la línea `MT5_PATH` para que apunte a donde está MetaTrader5:
   - **Windows**: Por defecto es:

     ```
     MT5_PATH=C:/Program Files/MetaTrader 5/terminal64.exe
     ```

     Si lo instalaste en otro lugar, ajusta la ruta.
   - **macOS**: Si usas Wine o Parallels para correr MetaTrader5, pon la ruta correcta (por ejemplo, la ruta dentro de Wine).
5. Opcional: Si tienes una cuenta de MetaTrader5, puedes añadir tu `LOGIN` y `PASSWORD` en el archivo `.env`.
6. Guarda el archivo y ciérralo.

## 🧪 Paso 5: Preparar el Entorno

Ahora vamos a instalar las herramientas que el proyecto necesita.

1. Abre una terminal:
   - **Windows**: Busca "cmd" en el menú de inicio.
   - **macOS**: Abre la Terminal.
2. Navega a la carpeta del proyecto:
   - **Windows**:

     ```
     cd C:\Users\TuUsuario\Documentos\MT5-Python
     ```

   - **macOS**:

     ```
     cd ~/Documentos/MT5-Python
     ```

3. Instala todo lo necesario con:

   ```
   poetry install
   ```

   Esto puede tardar un poco, pero solo necesitas hacerlo una vez.

## ▶️ Paso 6: Ejecutar el Script

¡Ya casi terminamos! Vamos a probar el proyecto.

1. En la misma terminal, escribe:

   ```
   poetry run python main.py
   ```

2. Si todo está bien, verás mensajes que dicen que se conectó a MetaTrader5 y algunos datos del mercado (como el RSI de EURUSD).

## 📚 ¿Qué Hace Este Proyecto?

- Se conecta a tu MetaTrader5.
- Toma datos del mercado, como precios de EURUSD.
- Calcula un indicador (RSI) y te dice si el mercado está "barato" (sobreventa), "caro" (sobrecompra) o normal.

## 🧠 Consejos Útiles

- **Error con `.env`**: Si ves un mensaje sobre `.env`, revisa que el archivo exista y que la ruta de `MT5_PATH` sea correcta.
- **Windows**: Si MetaTrader5 está en otra unidad (como D:), cambia la ruta en `.env` a algo como `D:/Program Files/MetaTrader 5/terminal64.exe`.
- **macOS**: Si usas Wine o Parallels, asegúrate de que la ruta en `.env` sea válida para tu setup.
- Si algo no funciona, revisa que los comandos anteriores hayan salido bien.
