import matplotlib.pyplot as plt

def grafico_libros():

    libros = ["Gran Gatsby", "1984", "Orgullo y Prejuicio"]
    cantidad = [8,5,3]

    plt.bar(libros, cantidad)
    plt.title("Libros más prestados")
    plt.ylabel("Cantidad")
    plt.show()


def grafico_usuarios():

    usuarios = ["Juan Perez","Maria Gomez","Ana Torres"]
    prestamos = [7,5,3]

    plt.bar(usuarios, prestamos)
    plt.title("Usuarios más activos")
    plt.ylabel("Prestamos")
    plt.show()