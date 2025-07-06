# 🐍 Entorno reproducible para MetaTrader5 con Python 3.8 usando Nix (Windows + WSL)

Este proyecto permite ejecutar scripts en Python que se conectan con MetaTrader 5, con un entorno controlado, sin conflictos de dependencias ni configuraciones manuales complicadas.

Está pensado para que personas sin experiencia en programación puedan usarlo fácilmente.

## ✅ Requisitos previos

- Un PC con **Windows 10 o 11**
- Tener instalado **MetaTrader 5**
- Tener habilitado el **Subsistema de Windows para Linux (WSL)**

## 🧩 Paso 1: Instalar WSL (una sola vez)

1. Abre el menú de Windows y busca `Características de Windows`.
2. Activa la opción: **“Subsistema de Windows para Linux”**
3. Reinicia tu equipo si es necesario.
4. Luego ve a la Microsoft Store, busca **Ubuntu** e instálalo.

## 📦 Paso 2: Instalar Nix en Ubuntu (WSL)

1. Abre la aplicación **Ubuntu** desde el menú Inicio.
2. Copia y pega este comando en la ventana que se abre:

   ```bash
   curl -L https://install.determinate.systems/nix | sh

3. Cierra y vuelve a abrir la terminal de Ubuntu para que se activen los cambios.

📁 Paso 3: Descargar este proyecto

 1. Entra a la página del proyecto en GitHub.
 2. Haz clic en el botón verde “Code” → “Download ZIP”
 3. Extrae el archivo ZIP en tu carpeta de documentos (por ejemplo: Documentos/MT5-Python)

No necesitas instalar Git ni usar comandos para esto.

🔧 Paso 4: Configurar la conexión a MetaTrader5

 1. Entra en la carpeta que descomprimiste.
 2. Haz una copia del archivo .env.example y renómbralo como .env
 3. Abre .env con un editor de texto (como Notepad) y modifica la siguiente línea:

MT5_PATH=/mnt/c/Program Files/MetaTrader 5/terminal64.exe

Asegúrate de que la ruta apunte al ejecutable de MetaTrader 5.

🧪 Paso 5: Activar el entorno de desarrollo

 1. Abre la app Ubuntu (WSL)
 2. Navega a la carpeta del proyecto:

cd "/mnt/c/Usuarios/TuUsuario/Documentos/MT5-Python"

 3. Ejecuta este comando para preparar el entorno:

nix develop

Esto configurará Python 3.8, Poetry y las dependencias automáticamente.

▶️ Paso 6: Ejecutar el script

Una vez dentro del entorno Nix, ejecuta:

poetry run python main.py

📄 Estructura del proyecto

mt5-python-project/
├── flake.nix           # Configuración del entorno con Nix
├── pyproject.toml      # Lista de librerías usadas con Poetry
├── main.py             # Script principal que se conecta a MT5
├── .env.example        # Plantilla de configuración
└── README.md           # Esta guía

📚 ¿Qué hace este proyecto?
 • Carga MetaTrader 5 desde el script Python
 • Extrae datos de mercado
 • Puede graficar, analizar o guardar información en Excel
 • Todo dentro de un entorno portátil y reproducible

🧠 Consejos útiles
 • Si al ejecutar ves un error sobre .env, asegúrate de que el archivo .env exista y contenga la ruta correcta a MT5.
 • Si tu MetaTrader está en otro disco o carpeta, ajusta la ruta en .env usando /mnt/d/... o /mnt/c/....

🚀 ¿Y después?

Puedes modificar main.py para hacer análisis, gráficos o automatizaciones con tus datos financieros.

Este entorno está preparado para usarse sin conocimientos técnicos.
