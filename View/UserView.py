#3a
from os import system
from Controllers.UserController import UserController
from Model.DTO.UserForCreation import UserForCreation
from Model.DTO.UserForLogin import UserForLogin


class UserView:

    def login_menu(self):
        system("cls")
        print(" Login de usuario ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        input(" Presione enter para continuar ".center(50, "!"))
        user_controller = UserController()#controller
        user_for_login = UserForLogin(username, password) #model
        validation = user_controller.login(user_for_login)# validacion
        return validation

    def add_user_menu(self):
        system("cls")
        print(" Agregar usuario ".center(50, "#"))
        print("-" * 50)
        username = input("Ingrese el nombre de usuario: ")
        print("-" * 50)
        password = input("Ingrese la contraseña: ")
        print("-" * 50)
        email = input("Ingrese el email: ")
        print("-" * 50)
        name = input("Ingrese el nombre: ")
        print("-" * 50)
        surname = input("Ingrese el apellido: ")
        print("-" * 50)
        user_for_creation = UserForCreation(username, password, email, name, surname)#model
        user_controller = UserController()#controller
        user_controller.add_user(user_for_creation)
        input(" Presione enter para continuar ".center(50, "!"))

    def list_users(self):
        system("cls")
        print(" Listado de usuarios ".center(50, "#"))
        user_controller = UserController()
        users = user_controller.get_users()
        for user in users:
            print(user)
        print("#" * 50)
        input(" Presione enter para continuar ".center(50, "!"))

#Agregado
    def baja_de_usuario(self):
        system("cls")
        print (" Para borrar su usuario primero debe iniciar sesion ".center(50), "#")
        print("-" * 50)
        bandera , user = self.login_menu()
        if bandera:
            user_controller = UserController()
            valido = user_controller.darse_de_baja(user)
            if valido:
                print("El usuario fue dado de baja")
            else:
                print("Ocurrio un error al dar de baja el usuario")
        else:
            print("Usuario o contraseña incorrectos.")
            
        input("Precione enter para continuar".center(50, "!"))