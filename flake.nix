{
  description = "MT5 + Python + Poetry dev shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python38; # Necesario para MetaTrader5 (https://www.mql5.com/en/docs/python_metatrader5)
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python
            pkgs.poetry
          ];

          shellHook = ''
            export MT5_PATH="/ruta/a/terminal64.exe"

            # Verifica si existe .env
            if [ ! -f .env ]; then
              echo "ERROR: Falta el archivo .env. Lee la guía en el README.md para crear y configurar .env."
              exit 1
            fi

            # Ejecuta Poetry install si es necesario
            if [ ! -d .venv ]; then
              echo "Instalando dependencias Poetry..."
              poetry install
            fi

            echo "Entorno preparado. Puedes ejecutar con 'poetry run python main.py'"
          '';
        };
      }
    );
}