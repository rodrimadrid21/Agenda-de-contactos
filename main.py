#1
import os
import sys


################################################

# configura el entorno para que pueda encontrar e importar módulos desde el directorio raíz del proyecto. 

PROJECT_ROOT = os.path.abspath( #4. Convierte en ruta absoluta.
    os.path.join( #3. UNION
        os.path.dirname(__file__), #1. directorio del archivo actual HIJO (cod)
        os.pardir #2. directorio PADRE
    )
)

sys.path.append(PROJECT_ROOT)

################################################


from View.MainMenu import MainMenu 

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()

