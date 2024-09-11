from tkinter import * 
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
from subprocess import call



class Registro:


	db_name = ("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/db2503319.db")


	def __init__(self, ventana_registro):

		self.window = ventana_registro
		self.window.title("Formulario de Registro")
		self.window.geometry("520x700")


		self.window.iconbitmap("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/calcu.ico")

		self.window.resizable(0,0)
		self.window.config(bd=10)

		titulo = Label(ventana_registro, text="REGISTRO DE USUARIO", fg="black", font=("Comic Sans MS", 13, "bold"), pady=5).pack()

		

		imagen_registrar = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/editar.png")

		nueva_imagen = imagen_registrar.resize((70,70))

		render = ImageTk.PhotoImage(nueva_imagen)

		label_imagen = Label(ventana_registro, image=render)

		label_imagen.image = render

		label_imagen.pack(pady=5)


		marco = LabelFrame(ventana_registro, text="Datos personales", font=("Comic Sans MS", 14 , "bold"), bd=2, pady=5)#.pack()
		marco.pack()

		label_usuario = Label(marco, text="Usuario", font=("Comic Sans MS", 12)).grid(row=0, column=0 , sticky='s', pady=0)
		self.usuario = Entry(marco, width=25)
		self.usuario.focus()
		self.usuario.grid(row=0, column=1, padx=5 ,pady=5)




		label_nombre = Label(marco, text="Nombre", font=("Comic Sans MS", 12)).grid(row=1, column=0, sticky='s', pady=0)
		self.nombre = Entry(marco, width=25)
		self.nombre.grid(row=1, column=1, padx=5 ,pady=5)

		label_apellido = Label(marco, text="Apellido", font=("Comic Sans MS", 12)).grid(row=2, column=0, sticky='s', pady=0)
		self.apellido = Entry(marco, width=25)
		self.apellido.grid(row=2, column=1, padx=5 ,pady=5)




		label_genero = Label(marco, text="Genero", font=("Comic Sans MS", 12)).grid(row=3, column=0, sticky='s', pady=0)
		self.combo_genero = ttk.Combobox(marco, values=["Masculino","Femenino"],width=22, state="readonly")
		self.combo_genero.current(0)
		self.combo_genero.grid(row=3, column=1, padx=10, pady=10)

		label_correo = Label(marco, text="Correo", font=("Comic Sans MS", 12)).grid(row=4, column=0, sticky='s', pady=0)
		self.correo = Entry(marco, width=25)
		self.correo.grid(row=4, column=1, padx=5 ,pady=5)

		label_edad = Label(marco, text="Edad", font=("Comic Sans MS", 12)).grid(row=5, column=0, sticky='s', pady=0)
		self.edad = Entry(marco, width=25)
		self.edad.grid(row=5, column=1, padx=5, pady=5)

		label_contrasena = Label(marco, text="Contraseña", font=("Comic Sans MS",12)).grid(row=6, column=0, sticky='s', pady=0)
		self.contrasena = Entry(marco, width=25, show="*")
		self.contrasena.grid(row=6, column=1, padx=5, pady=5)

		label_validar_password = Label(marco, text="Repetir Contraseña", font=("Comic Sans MS",12,)).grid(row=7, column=0, sticky='s', pady=0)
		self.validar_passwordd123 = Entry(marco, width=25, show="*")
		self.validar_passwordd123.grid(row=7, column=1, padx=5, pady=5)

		

		marco_pregunta = LabelFrame(ventana_registro, text="Preguntas de Seguridad", font=("Comic Sans MS", 14, "bold"), pady=10)
		marco_pregunta.config(bd=2, pady=5)
		marco_pregunta.pack()

		label_pregunta = Label(marco_pregunta, text="Preguntas", font=("Comic Sans MS", 12)).grid(row=0, column=0, sticky='s', padx=10, pady=8)
		self.combo_pregunta = ttk.Combobox(marco_pregunta, values=["Nombre de mascota","Nombre de mi perro","Cuidad de nacimiento","Nombre de papa"], width=30, state="readonly") 
		self.combo_pregunta.current(0)
		self.combo_pregunta.grid(row=0, column=1, padx=10, pady=8)


		label_res = Label(marco_pregunta, text="Responde", font=("Comic Sans MS",12)).grid(row=1, column=0, sticky='s', padx=10, pady=5)
		self.res = Entry(marco_pregunta, width=33)
		self.res.grid(row=1, column=1, padx=10, pady=10) 


		label_nota = Label(marco_pregunta, text="Es esta respuesta permite recuperar la contraseña",  fg="red",).grid(row=2, column=1, sticky='s')

		frame_botones = Frame(ventana_registro)
		frame_botones.pack()

		

		
		boton_registrar = Button(frame_botones, text="Registrar", command=self.registrar_usuario, height=2, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=1, padx=10, pady=10)
		boton_login = Button(frame_botones, text="Ingresar", height=2, command=self.llamar_login, width=9, bg="orange", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
		boton_limpiar = Button(frame_botones, text="Limpiar", height=2, command=self.limpiar_formulario, width=9, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=3, padx=10, pady=10)
		boton_cancelar= Button(frame_botones, text="Cancelar", height=2, command=ventana_registro.quit, width=9, bg="orange", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=4, padx=10, pady=10)



	def registrar_usuario(self):
		if self.validar_formulario() and self.validar_password() and self.validar_usuario():
			query = 'INSERT INTO Usuarios VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
			parameters = (self.usuario.get(), self.nombre.get(), self.apellido.get(), self.combo_genero.get(), self.edad.get(), self.correo.get(), self.contrasena.get(), self.res.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("Registro Exitoso", f'Bienvenido {self.nombre.get()} {self.apellido.get()}')
			self.limpiar_formulario()


	def validar_formulario(self):
		if len(self.usuario.get()) != 0 and len(self.nombre.get()) !=0 and len(self.apellido.get()) != 0 and len(self.combo_genero.get()) != 0 and len(self.edad.get()) != 0 and len(self.correo.get()) != 0 and len(self.contrasena.get()) != 0 and  len(self.res.get()) != 0:
			return True 
		else:
			messagebox.showerror("Error De Ingreso", "Diligencie todo el formulario")


	def validar_password(self):
		if (str(self.contrasena.get()) == str(self.validar_passwordd123.get())):
			return True 
		else:
			messagebox.showerror("Error de Registro", "El password no coinciden")


	def validar_usuario(self):
		usuario = self.usuario.get()
		dato = self.buscar_usuario(usuario)
		if (dato == []):
			return True
		else:
			messagebox.showerror("Error en registro", "El usuario ya existe")


	def buscar_usuario(self, usuario):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = "SELECT * FROM Usuarios WHERE usuario = {}".format(usuario)
			cursor.execute(sql)
			usuario_consulta = cursor.fetchall()
			cursor.close()
			return usuario_consulta


	def ejecutar_consulta(self, query, parameters=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			#comiit actuali de la bd
			conexion.commit()
			return result

	def llamar_login(self):
		ventana_registro.destroy()
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/login.py'])

	


	def limpiar_formulario(self):
		self.usuario.delete(0, END)
		self.nombre.delete(0, END)
		self.apellido.delete(0, END)
		self.combo_genero.delete(0, END)
		self.edad.delete(0, END)
		self.correo.delete(0, END)
		self.contrasena.delete(0, END)
		self.validar_passwordd123.delete(0, END)
		self.res.delete(0, END)




if __name__ == '__main__':
	ventana_registro = Tk()
	aplication = Registro(ventana_registro)
	ventana_registro.mainloop()

