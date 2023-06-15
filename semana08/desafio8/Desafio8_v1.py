import os
import platform

def limpiar_pantalla():
    sistema_operativo = platform.system()
    if sistema_operativo == 'Windows':
        os.system('cls') # Comando para limpiar pantalla en Windows
    elif sistema_operativo == 'Linux' or sistema_operativo == 'Darwin':
        os.system('clear') # Comando para limpiar pantalla en Mac o Linux
    else:
        return None # No hacer nada si es otro sistema operativo

## Clase Usuario
## atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
##métodos: login(), registrar()

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

    def __str__(self):
        return f'Usuario: {self.nombre} {self.apellido} (Id: {self.id} - Username: {self.username})'

    def login(self, username, contrasena):
        if self.username == username and self.contrasena == contrasena:
            print('Login exitoso')
            return True
        else:
            print('Usuario inexistente o contraseña errónea')
            return False

    def registrar1(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
        return 'Registro exitoso'

    def registrar(self, lista_usuarios):
        for usuario in lista_usuarios:
            if usuario == self:
                print(f'Id: {self.id} - Usuario: {self.username} ya existe. Registro inválido.')
                return
        lista_usuarios.append(self)
        print(f'Registro exitoso')


#Clase Publico(Usuario)
#atributo: es_publico
#métodos: registrar(), comentar()

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online)
        self.es_publico = es_publico
    
    def registrar(self):
        # registrarse aqui
        pass

    def comentar(self):
        # comentar aqui
        pass

#clase Colaborador(Usuario)
#atributos: es_colaborador
#métodos: registrar(), comentar(), publicar()

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador
    
    def registrar(self):
        # registrarse aqui
        pass

    def comentar(self):
        # comentar aqui
        pass

    def publicar(self):
        # publicar aqui
        pass


#clase Articulo
#id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado

class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado

#clase Comentario
# id, id_articulo, id_usuario, contenido, fecha_hora, estado

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado


limpiar_pantalla()
# INSTANCIAS
usuario1 = Usuario(1, 'Juan', 'Perez', '3624-223344', 'jperez', 'jperez@correo.com', 'secreto1', '14-06-2023', '/imagenes/avatar1.png', 1, 0)
usuario2 = Usuario(2, 'Maria', 'Gomez', '3624-334455', 'mgomez', 'mgomez@correo.com', 'secreto2', '13-06-2023', '/imagenes/avatar2.png', 0, 1)
usuario3 = Usuario(3, 'Jose', 'Lima', '3624-445566', 'jlima', 'jlima@correo.com', 'secreto3', '12-06-2023', '/imagenes/avatar3.png', 1, 1)
usuario4 = Usuario(4, 'Mariano', 'Fernandez', '3624-556677', 'mfernandez', 'mfernandez@correo.com', 'secreto4', '14-06-2023', '/imagenes/avatar4.png', 0, 0)
usuario3 = Usuario(3, 'Jose', 'Lima', '3624-445566', 'jlima', 'jlima@correo.com', 'secreto3', '12-06-2023', '/imagenes/avatar3.png', 1, 1)

usuarios = list()
usuarios.append(usuario1) # A mano
usuarios.append(usuario3) # A mano

usuario1.login('jperez','secreto1')
print('-'*30)
for u in usuarios:
    print(u)
print('-'*30)
usuario4.registrar(usuarios) # Deberia ser OK
for u in usuarios:
    print(u)
print('-'*30)
usuario2.registrar(usuarios) # Deberia ser OK
for u in usuarios:
    print(u)
print('-'*30)
usuario3.registrar(usuarios) # Deberia fallar
# Bueno hasta aca todo es a mamo, pensndo en objetos anda, 
# pero trabajando con datos individuales capaz no.
# porque yo le estoy poniendo nombre a los objetos, 
# en realidad deberia trabajar con los atributos verdad???
# Creo que me deberia olvidar de los objetos como tales o no se!!!
# Solo sirve para probar rapido.





# Para despues de hacer todos las clases y metodos
# Se puede descomentar el multilinea para probar el menu
"""
# PROGRAMA PRINCIPAL

def mostrar_menu():
    limpiar_pantalla()    
    print('===============================================')
    print('               MENU DE OPCIONES')
    print('===============================================')
    print('1 - Login')
    print('2 - Registrarse')
    print('3 - Salir')
    print('-----------------------------------------------')
    opcion = input('Ingrese la opción: ')
    return opcion

def login():
    pass

def registrarse():
    pass


while True:
    opcion = mostrar_menu()
    if opcion in '123':
        if opcion == '1':
            login()
            continue
        elif opcion == '2':
            registrarse()
            continue
        elif opcion == '3':
            print('Gracias por usar el sistema.')
            break
    print('La opción elegida es inválida.')
    input("Presiona ENTER para continuar...")    
    



id = input('Ingrese Id: ')
nombre = input('Ingrese el nombre : ')
apellido = input('Ingrese el apellido: ')
telefono = input('Ingrese el teléfono: ')
username = input('Ingrese el nombre de usuario: ')
email = input('Ingrese el correo electrónico: ')
contrasena = input('Ingrese la contraseña: ')
fecha_registro = input('Ingrese la fecha de registro (DD-MM-AAAA): ')
avatar = input('Ingrese el nombre del archivo del avatar: ')
estado = input('Ingrese es estado (1 = Habilitado / 0 = Deshabilitado): ')
online = input('Ingrese situacion (1 = Online / 0 = Offline): ')
"""