"""
Clase Usuario
 atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
 métodos: login(), registrar()

Clase Publico(Usuario)
 atributo: es_publico
 métodos: registrar(), comentar()

clase Colaborador(Usuario)
 atributos: es_colaborador
 métodos: registrar(), comentar(), publicar()

clase Articulo
 id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado

clase Comentario
 id, id_articulo, id_usuario, contenido, fecha_hora, estado

Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y logueado, código que permita comentar al Publico y además publicar al Colaborador.
"""

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasenia = contrasenia
        self.fecha_de_registro = fecha_de_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

    def login(self, username, contrasenia):
        if self.username == username and self.contrasenia == contrasenia:
            return True
        else:
            return False
        


 métodos: login(), registrar()
