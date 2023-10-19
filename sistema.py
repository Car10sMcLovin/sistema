import tkinter as tk
from tkinter import Menu
import mysql.connector

def volver():
    label_resultado.config(text="Mes que un club")

def opcion1():
    label_resultado.config(text="Plantilla Actual")
    try:
        # Conectar a la base de datos MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Messi2009",
            database="Barcelona"
        )
        cursor = conexion.cursor()

        # Ejecutar una consulta SQL para seleccionar todos los datos de la tabla futbolistas
        cursor.execute("SELECT * FROM futbolistas")
        datos = cursor.fetchall()

        # Cerrar la conexión a la base de datos
        conexion.close()

        # Crear una nueva ventana para mostrar los datos de forma estética
        ventana_plantilla = tk.Toplevel(ventana)
        ventana_plantilla.title("Plantilla Actual")

        # Crear un widget Text para mostrar los datos
        texto_plantilla = tk.Text(ventana_plantilla)
        texto_plantilla.pack()

        # Construir un mensaje con los datos
        resultado = "Plantilla Actual:\n"
        for fila in datos:
            resultado += f"Nombre: {fila[1]}\n"
            resultado += f"Apellido: {fila[2]}\n"
            resultado += f"Posición: {fila[3]}\n"
            resultado += f"País: {fila[4]}\n"
            resultado += f"Fecha de Nacimiento: {fila[5]}\n"
            resultado += f"Dorsal: {fila[6]}\n"
            resultado += f"Altura: {fila[7]}\n"
            resultado += f"Peso: {fila[8]}\n\n"

        # Insertar el resultado en el widget Text
        texto_plantilla.insert(tk.END, resultado)

    except mysql.connector.Error as error:
        print(f"Error: {error}")


    

def opcion2():
    label_resultado.config(text="Altas")
    # Crear una nueva ventana para ingresar datos
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Futbolista")

    # Campos de entrada para los datos del futbolista
    label_nombre = tk.Label(ventana_inscribir, text="Nombre:")
    entry_nombre = tk.Entry(ventana_inscribir)
    label_apellido = tk.Label(ventana_inscribir, text="Apellido:")
    entry_apellido = tk.Entry(ventana_inscribir)
    label_posicion = tk.Label(ventana_inscribir, text="Posición:")
    entry_posicion = tk.Entry(ventana_inscribir)
    label_pais = tk.Label(ventana_inscribir, text="País:")
    entry_pais = tk.Entry(ventana_inscribir)
    label_fecha_nacimiento = tk.Label(ventana_inscribir, text="Fecha de Nacimiento:")
    entry_fecha_nacimiento = tk.Entry(ventana_inscribir)
    label_dorsal = tk.Label(ventana_inscribir, text="Dorsal:")
    entry_dorsal = tk.Entry(ventana_inscribir)
    label_altura = tk.Label(ventana_inscribir, text="Altura:")
    entry_altura = tk.Entry(ventana_inscribir)
    label_peso = tk.Label(ventana_inscribir, text="Peso:")
    entry_peso = tk.Entry(ventana_inscribir)

    # Función para insertar datos en la tabla futbolistas
    def insertar_futbolista():
        try:
            # Conectar a la base de datos MySQL
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Messi2009",
                database="Barcelona"
            )
            cursor = conexion.cursor()

            # Obtener los datos de los campos de entrada
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            posicion = entry_posicion.get()
            pais = entry_pais.get()
            fecha_nacimiento = entry_fecha_nacimiento.get()
            dorsal = entry_dorsal.get()
            altura = entry_altura.get()
            peso = entry_peso.get()

            # Ejecutar una consulta SQL para insertar un nuevo registro en la tabla futbolistas
            consulta = "INSERT INTO futbolistas (nombre, apellido, posicion, pais, fecha_nacimiento, dorsal, altura, peso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            datos = (nombre, apellido, posicion, pais, fecha_nacimiento, dorsal, altura, peso)
            cursor.execute(consulta, datos)

            # Confirmar los cambios en la base de datos
            conexion.commit()

            # Cerrar la conexión a la base de datos
            conexion.close()

            # Cerrar la ventana de inscripción y mostrar un mensaje de éxito
            ventana_inscribir.destroy()
            tk.messagebox.showinfo("Éxito", "Futbolista inscrito correctamente.")

        except mysql.connector.Error as error:
            tk.messagebox.showerror("Error", f"Error al inscribir futbolista: {error}")

    # Botón para insertar el futbolista
    boton_insertar = tk.Button(ventana_inscribir, text="Inscribir Futbolista", command=insertar_futbolista)

    # Colocar widgets en la ventana de inscripción
    label_nombre.grid(row=0, column=0)
    entry_nombre.grid(row=0, column=1)
    label_apellido.grid(row=1, column=0)
    entry_apellido.grid(row=1, column=1)
    label_posicion.grid(row=2, column=0)
    entry_posicion.grid(row=2, column=1)
    label_pais.grid(row=3, column=0)
    entry_pais.grid(row=3, column=1)
    label_fecha_nacimiento.grid(row=4, column=0)
    entry_fecha_nacimiento.grid(row=4, column=1)
    label_dorsal.grid(row=5, column=0)
    entry_dorsal.grid(row=5, column=1)
    label_altura.grid(row=6, column=0)
    entry_altura.grid(row=6, column=1)
    label_peso.grid(row=7, column=0)
    entry_peso.grid(row=7, column=1)
    boton_insertar.grid(row=8, columnspan=2, pady=10)



def opcion3():
    label_resultado.config(text="Bajas")
    # Crear una nueva ventana para borrar un futbolista
    ventana_borrar = tk.Toplevel(ventana)
    ventana_borrar.title("Borrar Futbolista")

    # Obtener la lista de futbolistas desde la base de datos
    try:
        # Conectar a la base de datos MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Messi2009",
            database="Barcelona"
        )
        cursor = conexion.cursor()

        # Ejecutar una consulta SQL para obtener la lista de futbolistas
        cursor.execute("SELECT id, nombre, apellido FROM futbolistas")
        futbolistas = cursor.fetchall()

        # Cerrar la conexión a la base de datos
        conexion.close()

        if not futbolistas:
            tk.messagebox.showinfo("Información", "No hay futbolistas para borrar.")
            ventana_borrar.destroy()
            return

    except mysql.connector.Error as error:
        tk.messagebox.showerror("Error", f"Error al obtener la lista de futbolistas: {error}")
        ventana_borrar.destroy()
        return

    # Crear una variable de Tkinter para la selección
    seleccion = tk.StringVar(ventana_borrar)
    seleccion.set(futbolistas[0])  # Establecer el primer futbolista como predeterminado

    # Etiqueta para mostrar la lista de futbolistas
    label_lista = tk.Label(ventana_borrar, text="Selecciona un futbolista para borrar:")
    label_lista.pack()

    # Menú desplegable con la lista de futbolistas
    lista_futbolistas = tk.OptionMenu(ventana_borrar, seleccion, *futbolistas)
    lista_futbolistas.pack()

    # Función para borrar el futbolista seleccionado
    def borrar_futbolista():
        futbolista_seleccionado = seleccion.get()
        futbolista_id = int(futbolista_seleccionado.split()[0])

        try:
            # Conectar a la base de datos MySQL
            conexion = mysql.connector.connect(
                host="tu_host",
                user="tu_usuario",
                password="tu_contraseña",
                database="tu_base_de_datos"
            )
            cursor = conexion.cursor()

            # Ejecutar una consulta SQL para eliminar el futbolista seleccionado
            cursor.execute("DELETE FROM futbolistas WHERE id = %s", (futbolista_id,))

            # Confirmar los cambios en la base de datos
            conexion.commit()

            # Cerrar la conexión a la base de datos
            conexion.close()

            tk.messagebox.showinfo("Éxito", "Futbolista borrado correctamente.")
            ventana_borrar.destroy()

        except mysql.connector.Error as error:
            tk.messagebox.showerror("Error", f"Error al borrar futbolista: {error}")

    # Botón para borrar el futbolista seleccionado
    boton_borrar = tk.Button(ventana_borrar, text="Borrar Futbolista", command=borrar_futbolista)
    boton_borrar.pack(pady=10)


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("FC Barcelona")
ventana.geometry("400x300")

# Menú de opciones
menu = Menu(ventana)
ventana.config(menu=menu)

menu_opciones = Menu(menu)
menu.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Plantilla", command=opcion1)
menu_opciones.add_command(label="Inscribir", command=opcion2)
menu_opciones.add_command(label="Borrar", command=opcion3)

# Etiqueta para mostrar el resultado de la opción seleccionada
label_resultado = tk.Label(ventana, text="mes que un club", padx=20, pady=20)
label_resultado.pack()

# Botón de retorno
boton_retorno = tk.Button(ventana, text="Volver al Inicio", command=volver)
boton_retorno.pack(pady=10)

ventana.mainloop()

