# Modelo (Model)
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


# Vista (View)
class VistaUsuario:
    def mostrar_detalles_usuario(self, usuario):
        print("Detalles del usuario:")
        print(f"Nombre: {usuario.nombre}")
        print(f"Email: {usuario.email}")


# Controlador (Controller)
class ControladorUsuario:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def actualizar_usuario(self, nombre, email):
        self.modelo.nombre = nombre
        self.modelo.email = email

    def mostrar_detalles_usuario(self):
        self.vista.mostrar_detalles_usuario(self.modelo)


# Uso del patrón MVC
modelo_usuario = Usuario("Jaqueline godoy", "godoyjaqueline31@gmail.com")
vista_usuario = VistaUsuario()
controlador_usuario = ControladorUsuario(modelo_usuario, vista_usuario)

controlador_usuario.mostrar_detalles_usuario()

# Actualizar los datos del usuario
controlador_usuario.actualizar_usuario("Jaqueline Morataya", "jaquelineg13@hotmail.com")

controlador_usuario.mostrar_detalles_usuario()
