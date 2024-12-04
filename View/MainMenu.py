#2
from os import system
from .ContactView import ContactView
from .UserView import UserView
#El "." despues del from indica que está en el mismo directorio que el archivo actual.

class MainMenu:

    def menu(self):
        while True:
            system("cls")
            print(" Bienvenido a la agenda de contactos ".center(50, "#"))
            print("1. Login de usuario")
            print("2. Registro de usuario")
            print("3. Listar Usuarios")
            print("4. Darse de baja")
            print("5. Salir del programa")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                user_view = UserView()
                validation = user_view.login_menu()
                if validation[0] == True:
                    user = validation[1]#dos valores
                    ContactView(user).menu()
                else:
                    print(" Usuario o contraseña incorrecta ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "2":
                user_view = UserView()
                validation = user_view.add_user_menu()
            elif option == "3":
                user_view = UserView()
                validation = user_view.list_users()
            elif option =="4":
                user_view =UserView()
                validation = user_view.baja_de_usuario()

            elif option == "5":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))


if __name__ == "_main_":
    main_menu = MainMenu()
    main_menu.menu()
