from modelos import Libro, Usuario, Prestamo

class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, id):
        self.libros = [l for l in self.libros if l.id != id]

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminar_usuario(self, id):
        self.usuarios = [u for u in self.usuarios if u.id != id]

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)