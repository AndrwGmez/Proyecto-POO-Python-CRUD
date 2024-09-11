from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sys
from subprocess import call
import sqlite3

class Clientes():

	db_name = ("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/db2503319.db")

	def __init__(self, ventana_producto):	
		menubar = Menu(ventana_producto)
		ventana_producto.title("Clientes")
		ventana_producto.geometry("900x800")	
		ventana_producto.iconbitmap("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/fondos2/servicio-al-cliente.ico")
		ventana_producto.resizable(0,0)

		
		ventana_producto.config(bd=10, menu=menubar)
		productos = Menu(menubar, tearoff=0)
		clientes = Menu(menubar, tearoff=0)
		ventas = Menu(menubar, tearoff=0)
		informacion = Menu(menubar, tearoff=0)
		cerrar_sesion = Menu(menubar, tearoff=0)


		menubar.add_cascade(label="Productos", menu=productos)
		menubar.add_cascade(label="Clientes", menu=clientes)
		menubar.add_cascade(label="Ventas", menu=ventas)
		menubar.add_cascade(label="Ayuda", menu=informacion)
		menubar.add_cascade(label="Opciones", menu=cerrar_sesion)


	
		#self.img_registrar = PhotoImage(file="C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/7/fondos2/clasificacion.png", width=20, height=20)
		#self.img_buscar = PhotoImage(file="C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/7/fondos2/companero-de-negocios.png", width=20, height=20)
		#self.img_informacion = PhotoImage(file="C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/7/fondos2/objetivo.png", width=20, height=20)


		self.boton_registrar = clientes.add_command(label="Registrar", command=self.widgets_crud, compound=LEFT)
		self.boton_buscar = clientes.add_command(label="Buscar", command=self.widgets_buscador, compound=LEFT)
		self.boton_informacion = informacion.add_command(label="Informacion del sistema", command=self.widgets_informacion, compound=LEFT)
		self.cerrar_sesion = cerrar_sesion.add_command(label="Cerrar Sesion", command=self.llamar_login, compound=LEFT)

		
		self.label_titulo_crud = LabelFrame(ventana_producto)
		self.frame_logos_productos = LabelFrame(ventana_producto)
		self.frame_registro = LabelFrame(ventana_producto, text="Informacion del Cliente", font=("Comic Sans MS", 10, "bold"), pady=5)
		self.frame_botones_registro = LabelFrame(ventana_producto)
		self.frame_tabla_crud = LabelFrame(ventana_producto)


		self.label_titulo_buscador = LabelFrame(ventana_producto)
		self.frame_buscar_producto = LabelFrame(ventana_producto, text="Buscar cliente", font=("Comic Sans MS", 10, "bold"), pady=5)
		self.frame_boton_buscar = LabelFrame(ventana_producto)

		self.label_informacion = LabelFrame(ventana_producto)


		self.widgets_crud()


		titulo = Label(self.frame_registro, text="LISTA DE CLIENTES", fg="black", font=("Comic Sans MS", 13, "bold"), pady=5)#.pack()


		imagen_1 = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/fondos2/comprador.png")
		nueva_imagen_1 = imagen_1.resize((90,90))
		render_1 = ImageTk.PhotoImage(nueva_imagen_1)
		label_imagen_1 = Label(self.frame_logos_productos, image=render_1)
		label_imagen_1.image = render_1
		label_imagen_1.grid(row=0, column=0, padx=5, pady=5)
		


		imagen_2 = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/fondos2/objetivo.png")
		nueva_imagen_2 = imagen_2.resize((90,90))
		render_2 = ImageTk.PhotoImage(nueva_imagen_2)
		label_imagen_2 = Label(self.frame_logos_productos, image=render_2)
		label_imagen_2.image = render_2
		label_imagen_2.grid(row=0, column=1, padx=5, pady=5)



		imagen_3 = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/fondos2/companero-de-negocios.png")
		nueva_imagen_3 = imagen_3.resize((90,90))
		render_3 = ImageTk.PhotoImage(nueva_imagen_3)
		label_imagen_3 = Label(self.frame_logos_productos, image=render_3)
		label_imagen_3.image = render_3
		label_imagen_3.grid(row=0, column=2, padx=5, pady=5)



		imagen_4 = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/fondos2/clasificacion.png")
		nueva_imagen_4 = imagen_4.resize((90,90))
		render_4 = ImageTk.PhotoImage(nueva_imagen_4)
		label_imagen_4 = Label(self.frame_logos_productos, image=render_4)
		label_imagen_4.image = render_4
		label_imagen_4.grid(row=0, column=3, padx=5, pady=5)



		marco_producto = LabelFrame(ventana_producto, text="Informacion de los cliente", font=("Comic Sans MS", 13, "bold"), bd=5, pady=5)



		label_codigo_producto = Label(self.frame_registro, text="Código de cliente: ", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0, sticky='s', padx=3, pady=3)
		self.codigo_producto = Entry(self.frame_registro, width=20)
		self.codigo_producto.grid(row=0, column=1, padx=3, pady=3)
		self.codigo_producto.focus()


		label_categoria_producto = Label(self.frame_registro, text="Categoria", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=3, sticky='s', padx=3, pady=3)
		self.categoria_producto = ttk.Combobox(self.frame_registro, values=["Baja", "Media", "Alta","Otro"], width=17, state="readonly")
		self.categoria_producto.current(0)
		self.categoria_producto.grid(row=0, column=4, padx=3, pady=3)


		label_nombre_producto = Label(self.frame_registro, text="Nombre del cliente: ", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=0, sticky='s', padx=3, pady=3)
		self.nombre_producto = Entry(self.frame_registro, width=20)
		self.nombre_producto.grid(row=1, column=1, padx=3, pady=3)


		label_categoria = Label(self.frame_registro, text="Celular:", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=3, sticky='s', padx=3, pady=3)
		self.descripcion_producto = Entry(self.frame_registro, width=20)
		self.descripcion_producto.grid(row=1, column=4, padx=3, pady=3)


		label_cantidad = Label(self.frame_registro, text="Apellido de cliente: : ", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=0, sticky='s', padx=3, pady=3)
		self.cantidad = Entry(self.frame_registro, width=20)
		self.cantidad.grid(row=2, column=1, padx=3, pady=3)



		label_precio = Label(self.frame_registro, text="C.C: ", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=3, sticky='s', padx=3, pady=3)
		self.precio = Entry(self.frame_registro, width=20)
		self.precio.grid(row=2, column=4, padx=3, pady=3)




		frame_botones = Frame(ventana_producto)

		boton_registrar = Button(self.frame_botones_registro, text="Registrar", command=self.agregar_producto ,height=2, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=0, padx=10, pady=10)
		boton_editar = Button(self.frame_botones_registro, text="Editar", command=self.editar_producto, height=2, width=9, bg="orange", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=1, padx=10, pady=10)
		boton_limpiar= Button(self.frame_botones_registro, text="Limpiar", command=self.limpiar_formulario, height=2, width=9, bg="blue", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
		boton_eliminar = Button(self.frame_botones_registro, text="Eliminar", command=self.eliminar_producto, height=2, width=9, bg="red", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=3, padx=10, pady=10)
		boton_salir= Button(self.frame_botones_registro, text="Cancelar", command=ventana_producto.quit, height=2, width=9, bg="purple", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=4, padx=10, pady=10)

		boton_clientes = Button(self.frame_botones_registro, text="Clientes", command=self.llamar_clientes, height=2, width=9, bg="brown", fg="white", font=("Comic Sans MS",12,"bold")).grid(row=2, column=3, padx=10, pady=10)
		boton_ventas= Button(self.frame_botones_registro, text="Ventas", command=self.llamar_ventas, height=2, width=9, bg="fuchsia", fg="white", font=("Comic Sans MS",12,"bold")).grid(row=2, column=2, padx=10, pady=10)
		boton_productos= Button(self.frame_botones_registro, text="Productos", command=self.llamar_productos, height=2, width=9, bg="gray", fg="white", font=("Comic Sans MS",12,"bold")).grid(row=2, column=1, padx=10, pady=10)



	def agregar_producto(self):
		if self.validar_formulario_completo() and self.validar_registrar():
			query = 'INSERT INTO Clientes VALUES (NULL, ?, ?, ?, ?, ?, ?)'
			parameters = (self.codigo_producto.get(), self.nombre_producto.get(), self.categoria_producto.get(), self.descripcion_producto.get(), self.cantidad.get(), self.precio.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("REGISTRO EXITOSO", f'Cliente resgistrado')
		self.limpiar_formulario()
		self.listar_productos()



	def validar_formulario_completo(self):
		if len(self.codigo_producto.get()) != 0 and len(self.categoria_producto.get()) != 0 and len(self.nombre_producto.get()) != 0 and len(self.descripcion_producto.get()) != 0 and len(self.cantidad.get()) != 0 and len(self.precio.get()) != 0:
			return True
		else:
			messagebox.showerror("ERROR PARA AGREGAR", 'Digite todos los campos')



	def ejecutar_consulta(self, query, parameters=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			conexion.commit()
			return result



	def limpiar_formulario(self):
		self.codigo_producto.delete(0, END)
		self.categoria_producto.delete(0, END)
		self.nombre_producto.delete(0, END)
		self.descripcion_producto.delete(0, END)
		self.cantidad.delete(0, END)
		self.precio.delete(0, END)



	def listar_productos(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)

		query = 'SELECT * FROM Clientes ORDER BY nombre DESC'
		db_rows = self.ejecutar_consulta(query)
		for  row in db_rows:
			self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))



	def editar_producto(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un cliente de la tabla")

		codigo = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		categoria = self.tree.item(self.tree.selection())['values'][1]
		apellido = self.tree.item(self.tree.selection())['values'][2]
		celular = self.tree.item(self.tree.selection())['values'][3]
		c_c = self.tree.item(self.tree.selection())['values'][4]

		self.ventana_editar = Toplevel()
		self.ventana_editar.title("EDITAR CLIENTE")
		self.ventana_editar.iconbitmap("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/calcu.ico")
		self.ventana_editar.resizable(0,0)

		label_codigo = Label(self.ventana_editar, text="Código del cliente:", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), width=25)
		nuevo_codigo.grid(row=0, column=1, padx=5, pady=8)

		label_categoria = Label(self.ventana_editar, text="Categoria:", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_combo_categoria = ttk.Combobox(self.ventana_editar, values=["Baja", "Media", "Alta"], width=22, state="readonly")
		nuevo_combo_categoria.set(categoria)
		nuevo_combo_categoria.grid(row=0, column=3, padx=5, pady=0)

		label_nombre = Label(self.ventana_editar, text="Nombre cliente:", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nuevo_nombre = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre), width=25)
		nuevo_nombre.grid(row=1, column=1, padx=5, pady=0)

		label_descripcion = Label(self.ventana_editar, text="Apellido:", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		nuevo_descripcion = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=apellido), width=25)
		nuevo_descripcion.grid(row=1, column=3, padx=5, pady=0)

		label_cantidad = Label(self.ventana_editar, text="Celular:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nuevo_cantidad = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=celular), width=25)
		nuevo_cantidad.grid(row=2, column=1, padx=5, pady=0)

		label_precio = Label(self.ventana_editar, text="C.C:", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		nuevo_precio = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=c_c), width=25)
		nuevo_precio.grid(row=2, column=3, padx=5, pady=0)

		boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR", command=lambda:self.actualizar(nuevo_codigo.get(), nuevo_nombre.get(), nuevo_combo_categoria.get(), nuevo_cantidad.get(), nuevo_precio.get(), nuevo_descripcion.get(), codigo), height=2, width=20, bg="green", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar.mainloop()


	def actualizar(self, nuevo_codigo, nuevo_nombre, nuevo_combo_categoria, nuevo_descripcion, nuevo_cantidad, nuevo_precio, codigo):
		query = 'UPDATE Clientes SET codigo=?, nombre=?, categoria=?, apellido=?,  celular=?, c_c=? WHERE codigo=?'
		parameters = (nuevo_codigo, nuevo_nombre, nuevo_combo_categoria, nuevo_descripcion, nuevo_cantidad, nuevo_precio, codigo)


		self.ejecutar_consulta(query, parameters)

		messagebox.showinfo("EXITO", f'Cliente Actualizado: {nuevo_nombre}')
		self.ventana_editar.destroy()
		self.listar_productos()



	def eliminar_producto(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un cliente de la tabla")
		dato = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM Clientes WHERE codigo = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Está seguro de eliminar el cliente: {nombre}?")
		if respuesta == 'yes':
			self.ejecutar_consulta(query, (dato,))
			self.listar_productos()
			messagebox.showinfo('EXITO', f'Cliente eliminado: {nombre}')
		else:
			messagebox.showerror('ERROR', f'Error al eliminar el cliente: {nombre}')



	def buscar_productos(self):
		if (self.validar_busqueda()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			
			if (self.combo_buscar.get() == 'codigo'):
				query = ("SELECT * FROM Clientes WHERE codigo LIKE ?")
				parameters = (self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query, (parameters,))

				for row in db_rows:
					self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))		
				if (list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR", "Cliente no encontrado")

			else:
				query = ("SELECT * FROM Clientes WHERE nombre LIKE ?")		
				parameters = ("%"+self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query, (parameters,))
				for row in db_rows:
					self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))
				if (list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR", "Cliente no encontrado")



	def validar_busqueda(self):
		if len(self.codigo_nombre.get()) != 0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR", "Complete todos los campos para la busqueda")




	def validar_registrar(self):
		parameters = self.codigo_producto.get()
		query = "SELECT * FROM Clientes WHERE codigo = ?"
		dato = self.ejecutar_consulta(query, (parameters,))
		if (dato.fetchall() == []):
			return True
		else:
			messagebox.showerror("Error de Registro", "Codigo registrado anteriormente")



	def widgets_crud(self):
		self.label_titulo_crud.config(bd=0)
		self.label_titulo_crud.grid(row=0, column=0, padx=5, pady=5)


		self.titulo_crud = Label(self.label_titulo_crud, text="LISTA DE CLIENTES", fg="black", font=("Comic Sans MS", 17, "bold"), pady=10)
		self.titulo_crud.grid(row=0, column=0)
		

	
		self.frame_tabla_crud.config(bd=2)
		self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_crud, height=13, columns=("columna1", "columna2", "columna3", "columna4", "columna5"))
		self.tree.heading("#0", text='Codigo', anchor=CENTER)
		self.tree.column("#0", width=90, minwidth=50, stretch=False)

		self.tree.heading("columna1", text='Codigo', anchor=CENTER)
		self.tree.column("columna1", width=150, minwidth=50, stretch=False)

		self.tree.heading("columna1", text='Nombre', anchor=CENTER)
		self.tree.column("columna1", width=150, minwidth=50, stretch=False)

		self.tree.heading("columna2", text='Categoria', anchor=CENTER)
		self.tree.column("columna2", width=150, minwidth=50, stretch=False)

		self.tree.heading("columna3", text='C.C', anchor=CENTER)
		self.tree.column("columna3", width=150, minwidth=50, stretch=False)

		self.tree.heading("columna4", text='Celular', anchor=CENTER)
		self.tree.column("columna4", width=150, minwidth=50, stretch=False)

		self.tree.heading("columna5", text='Apellido', anchor=CENTER)
		self.tree.column("columna5", width=150, minwidth=50, stretch=False)


		self.tree.grid(row=0, column=0, sticky=E)


		self.listar_productos()

		self.widgets_buscador_remove()
		self.label_informacion.grid_remove()


		self.frame_logos_productos.config(bd=0)
		self.frame_logos_productos.grid(row=1, column=0, padx=5, pady=5)

		self.frame_registro.config(bd=2)
		self.frame_registro.grid(row=2, column=0, padx=5, pady=5)


		self.frame_botones_registro.config(bd=0)
		self.frame_botones_registro.grid(row=3, column=0, padx=5, pady=5)





	def widgets_buscador(self):
		self.label_titulo_buscador.config(bd=0)
		self.label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)

		self.titulo_buscador = Label(self.label_titulo_buscador, text="BUSCAR CLIENTE", fg="black", font=("Comic Sans MS", 17, "bold"))
		self.titulo_buscador.grid(row=0, column=0)

		self.frame_buscar_producto.config(bd=2)
		self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)


		self.label_buscar = Label(self.frame_buscar_producto, text="Buscar por: ", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=5)
		self.combo_buscar = ttk.Combobox(self.frame_buscar_producto, values=["codigo", "nombre"], width=22, state="readonly")
		self.combo_buscar.current(0)
		self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)


		label_codigo_codigo = Label(self.frame_buscar_producto, text="Codigo / Nombre del producto: ", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=5)
		self.codigo_nombre = Entry(self.frame_buscar_producto, width=25)
		self.codigo_nombre.focus()
		self.codigo_nombre.grid(row=0, column=3, padx=5, pady=5)


		self.frame_boton_buscar.config(bd=0)
		self.frame_boton_buscar.grid(row=3, column=0, padx=5, pady=5)

		self.boton_buscar = Button(self.frame_boton_buscar, text="BUSCAR", command=self.buscar_productos, height=2, width=20, bg="green", fg="white", font=("Comic Sans MS", 10, "bold"))
		self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

		self.tree.delete(*self.tree.get_children())


		self.widgets_crud_remove()
		self.label_informacion.grid_remove()



	def widgets_crud_remove(self):
		
		self.label_titulo_crud.grid_remove()
		self.frame_registro.grid_remove()
		self.frame_botones_registro.grid_remove()



	def widgets_buscador_remove(self):
		self.label_titulo_buscador.grid_remove()
		self.frame_buscar_producto.grid_remove()
		self.frame_boton_buscar.grid_remove()



	def widgets_informacion(self):

		self.frame_logos_productos.grid_forget()
		self.frame_tabla_crud.grid_forget()
		self.label_informacion.config(bd=0)
		self.label_informacion.grid(row=0,column=0)

		self.label_titulo = Label(self.label_informacion, text="APLICACION DE ESCRITORIO", fg="white", bg="black", font=("Comic Sans MS", 25, "bold"), padx=137, pady=20)
		self.label_titulo.grid(row=0,column=0)

		imagen_soporte = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/fondos2/comprador.png")
		nueva_imagen = imagen_soporte.resize((170,170))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.label_informacion, image = render)
		label_imagen.image = render
		label_imagen.grid(row=1, column=0, padx=10, pady=15)


		self.label_titulo = Label(self.label_informacion,text="<< Codigo de Tienda de Tecnologia",fg="black",font=("Comic Sans", 18,"bold"))
		self.label_titulo.grid(row=2,column=0,sticky=W,padx=30,pady=10)


		self.label_titulo = Label(self.label_informacion, text=">> En esta tienda se encuentra producto de Tecnologia",fg="black",font=("Comic Sans",18,"bold"))
		self.label_titulo.grid(row=3,column=0,sticky=W,padx=30,pady=10)


		self.label_titulo = Label(self.label_informacion, text="<< YO ARG",fg="black",font=("Comic Sans",18,"bold"))
		self.label_titulo.grid(row=4,column=0,sticky=W,padx=30,pady=10)

		self.label_titulo = Label(self.label_informacion, text=">> MEGANSOFT",fg="black",font=("Comic Sans",18,"bold"))
		self.label_titulo.grid(row=5,column=0,sticky=W,padx=30,pady=10)


		self.label_titulo = Label(self.label_informacion, text=">> Desarrollado Por Yuly Sáenz ",fg="black",font=("Comic Sans",18,"bold"))
		self.label_titulo.grid(row=6,column=0,pady=60)


		self.widgets_buscador_remove()
		self.widgets_crud_remove()


	def llamar_productos(self):
		ventana_producto.destroy()
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/productos.py'])


	def llamar_clientes(self):
		ventana_producto.destroy()
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/cliente.py'])


	def llamar_ventas(self):
		ventana_producto.destroy()
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/venta.py'])


	def llamar_login(self):
		ventana_producto.destroy()
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/login.py'])



if __name__ == '__main__':
	ventana_producto = Tk()
	applicacion = Clientes(ventana_producto)
	ventana_producto.mainloop()