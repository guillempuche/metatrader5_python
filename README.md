# Entorno reproducible para MetaTrader5 con Python 3.8 usando Nix (Determinate Systems)

## 1. Instalar Nix (Determinate Systems)

Recomendado: usa el instalador de Determinate Systems para una experiencia moderna y segura en macOS/Linux:

```sh
curl -L https://install.determinate.systems/nix | sh -s -- install
```

Más información: <https://docs.determinate.systems/>

## 2. Configurar el archivo de entorno `.env`

Antes de continuar, debes crear tu archivo `.env` con las variables necesarias. Si existe un archivo `.env.example`, cópialo y edítalo:

```sh
cp .env.example .env
```

Luego abre `.env` y cambia los valores según tu configuración (por ejemplo, la ruta de MT5, credenciales, etc). Consulta la guía o README para detalles sobre cada variable.

**Este paso es obligatorio antes de activar el entorno o ejecutar cualquier script.**

## 3. Activar el entorno de desarrollo

Desde la raíz del proyecto:

```sh
nix develop
```

Esto abrirá un shell con Python 3.8, pip, pandas, matplotlib y las variables de entorno necesarias.

## 4. Ejecutar tu script

Asegúrate de tener MetaTrader5 instalado y accesible desde la ruta indicada. Luego ejecuta tu script Python normalmente:

```sh
python main.py
```

## Notas

- Puedes modificar el flake.nix para agregar más dependencias si lo necesitas.
- Consulta la documentación oficial de MetaTrader5 para detalles sobre la integración Python: <https://www.mql5.com/en/docs/python_metatrader5>
