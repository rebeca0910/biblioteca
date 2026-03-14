import tkinter as tk
from tkinter import ttk
from gestor import Biblioteca
from modelos import Libro, Usuario
import graficos

biblioteca = Biblioteca()

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Biblioteca")
ventana.geometry("900x600")

tabs = ttk.Notebook(ventana)
tabs.pack(fill="both", expand=True)

# -------- PESTAÑA LIBROS --------

tab_libros = tk.Frame(tabs)
tabs.add(tab_libros, text="Libros")

tabla_libros = ttk.Treeview(tab_libros, columns=("ID","Titulo","Autor","Año"), show="headings")

tabla_libros.heading("ID", text="ID")
tabla_libros.heading("Titulo", text="Titulo")
tabla_libros.heading("Autor", text="Autor")
tabla_libros.heading("Año", text="Año")

tabla_libros.pack(fill="x")

frame_inputs = tk.Frame(tab_libros)
frame_inputs.pack(pady=10)

entry_id = tk.Entry(frame_inputs)
entry_titulo = tk.Entry(frame_inputs)
entry_autor = tk.Entry(frame_inputs)
entry_anio = tk.Entry(frame_inputs)

entry_id.grid(row=0,column=0)
entry_titulo.grid(row=0,column=1)
entry_autor.grid(row=0,column=2)
entry_anio.grid(row=0,column=3)

def agregar_libro():

    libro = Libro(
        entry_id.get(),
        entry_titulo.get(),
        entry_autor.get(),
        entry_anio.get()
    )

    biblioteca.agregar_libro(libro)

    tabla_libros.insert(
        "",
        "end",
        values=(libro.id, libro.titulo, libro.autor, libro.anio)
    )
def editar_libro():

    seleccionado = tabla_libros.selection()

    if not seleccionado:
        return

    item = tabla_libros.item(seleccionado)
    valores = item["values"]

    entry_id.delete(0, tk.END)
    entry_id.insert(0, valores[0])

    entry_titulo.delete(0, tk.END)
    entry_titulo.insert(0, valores[1])

    entry_autor.delete(0, tk.END)
    entry_autor.insert(0, valores[2])

    entry_anio.delete(0, tk.END)
    entry_anio.insert(0, valores[3])

    tabla_libros.delete(seleccionado)

def eliminar_libro():

    seleccionado = tabla_libros.selection()

    if seleccionado:
        tabla_libros.delete(seleccionado)

frame_botones = tk.Frame(tab_libros)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Añadir", command=agregar_libro, width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Editar", command=editar_libro, width=10).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Eliminar", command=eliminar_libro, width=10).grid(row=0, column=2, padx=5)
    
# -------- PESTAÑA USUARIOS --------

tab_usuarios = tk.Frame(tabs)
tabs.add(tab_usuarios, text="Usuarios")

tabla_usuarios = ttk.Treeview(tab_usuarios, columns=("ID","Nombre","Correo"), show="headings")

tabla_usuarios.heading("ID", text="ID")
tabla_usuarios.heading("Nombre", text="Nombre")
tabla_usuarios.heading("Correo", text="Correo")

tabla_usuarios.pack(fill="x")

frame_user = tk.Frame(tab_usuarios)
frame_user.pack(pady=10)

entry_uid = tk.Entry(frame_user)
entry_nombre = tk.Entry(frame_user)
entry_correo = tk.Entry(frame_user)

entry_uid.grid(row=0,column=0)
entry_nombre.grid(row=0,column=1)
entry_correo.grid(row=0,column=2)

def agregar_usuario():

    usuario = Usuario(
        entry_uid.get(),
        entry_nombre.get(),
        entry_correo.get()
    )

    biblioteca.agregar_usuario(usuario)

    tabla_usuarios.insert(
        "",
        "end",
        values=(usuario.id, usuario.nombre, usuario.correo)
    )

tk.Button(tab_usuarios, text="Agregar Usuario", command=agregar_usuario).pack()

# -------- PESTAÑA GRAFICOS --------

tab_graficos = tk.Frame(tabs)
tabs.add(tab_graficos, text="Estadísticas")

tk.Button(tab_graficos,
          text="Libros más prestados",
          command=graficos.grafico_libros).pack(pady=20)

tk.Button(tab_graficos,
          text="Usuarios más activos",
          command=graficos.grafico_usuarios).pack(pady=20)

ventana.mainloop()