class Libro:

    def __init__(self, id, titulo, autor, anio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio


class Usuario:

    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo


class Prestamo:

    def __init__(self, id, libro, usuario, fecha):
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha