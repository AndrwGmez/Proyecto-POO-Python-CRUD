from tkinter import * 
from PIL import ImageTk, Image
import sys
from subprocess import call
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class Recuperar():

		db_name = ("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/db2503319.db")

		#db_name = "C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/3/db2503319.db"


		def __init__(self, ventana_recuperar):

			self.window = ventana_recuperar
			self.window.title("Recuperar Contraseña")
			self.window.geometry("550x450")

			#self.window.iconbitmap("C:/Users/Aprendiz/Documents/Veri No Tocar/Inter/login/calcu.ico")
			
			self.window.iconbitmap("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/calcu.ico")

			self.window.resizable(0,0)
			self.window.config(bd=10)

			titulo = Label(ventana_recuperar, text="RECUPERAR CONTRASEÑA", fg="black", font=("Comic Sans MS", 13, "bold"), pady=5).pack()



			#imagen_registrar = Image.open("C:/Users/Aprendiz/Documents/Veri No Tocar/Inter/login/editar.png")

			imagen_registrar = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/editar.png")

			nueva_imagen = imagen_registrar.resize((70,70))

			render = ImageTk.PhotoImage(nueva_imagen)

			label_imagen = Label(ventana_recuperar, image=render)

			label_imagen.image = render

			label_imagen.pack(pady=5)



			marco = LabelFrame(ventana_recuperar, text="Datos de recuperación del password", font=("Comic Sans MS", 10 , "bold"), bd=2, pady=10)#.pack()
			marco.pack()

			label_usuario = Label(marco, text="Usuario:", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0 , sticky='s', pady=0)
			self.usuario = Entry(marco, width=25)
			self.usuario.focus()
			self.usuario.grid(row=0, column=1, padx=5 ,pady=5)

			marco = LabelFrame(ventana_recuperar, text="Preguntas de Seguridad", font=("Comic Sans MS", 10, "bold"), pady=10)
			marco.config(bd=2, pady=5)
			marco.pack()

			label_nota = Label(marco, text="Seleccione una pregunta y digite la respuesta correcta.",  fg="red",).grid(row=6, column=0, sticky='s')


			label_pregunta = Label(marco, text="Pregunta:", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0, sticky='s', padx=10, pady=8)
			self.combo_pregunta = ttk.Combobox(marco, values=["Nombre de la primera masaco","Nombre de la segunda masaco","Cuidad de nacimiento","Nombre de papa"], width=23, state="readonly") 
			self.combo_pregunta.current(0)
			self.combo_pregunta.grid(row=0, column=1, padx=10, pady=8)		


			label_respuesta = Label(marco, text="Respuesta", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=0, sticky='s', padx=0)
			self.respuesta = Entry(marco, width=25)	
			self.respuesta.grid(row=1, column=1, padx=5, pady=5)


			label_nuevo_password = Label(marco, text="Nuevo Password", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=0, sticky='s', padx=0)
			self.nuevo_password = Entry(marco, width=25)	
			self.nuevo_password.grid(row=2, column=1, padx=5, pady=5)


			label_recuperar_password1 = Label(marco, text="Repetir Password", font=("Comic Sans MS", 10, "bold")).grid(row=3, column=0, sticky='s', padx=0)
			self.recuperar_password1 = Entry(marco, width=25)
			self.recuperar_password1.grid(row=3, column=1, padx=5, pady=5)

			frame_botones = Frame(ventana_recuperar)
			frame_botones.pack()

			boton_recuperar = Button(frame_botones, text="RECUPERAR", command=self.recuperar_password, height=2, width=9, bg="orange", fg="white", font=("Comic Sans MS", 8, "bold")).grid(row=1, column=1, padx=10, pady=10)
			boton_login = Button(frame_botones, text="LOGIN", height=2, width=9 , command=self.llamar_registro, bg="green", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=2, padx=10, pady=10)
			boton_cancelar = Button(frame_botones, text="CANCELAR", height=2, width=9, command=ventana_recuperar.quit ,bg="red", fg="white", font=("Comic Sans MS",8,"bold")).grid(row=1, column=3, padx=10, pady=10)


		def llamar_registro(self):
			ventana_recuperar.destroy()
			call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/login.py'])


		def recuperar_password(self):
			if self.validar_formulario_completo() and self.validar_datos_usuario() and self.validar_password():
				query = 'UPDATE Usuarios SET password=(?) WHERE usuario=(?)'
				parameters = (self.nuevo_password.get(), self.usuario.get())
				self.ejecutar_consulta(query, parameters)
				messagebox.showinfo("CONTRASEÑA RECUPERADA", f"Contraseña actualizada correctamente")
				self.limpiar_formulario()

		def validar_formulario_completo(self):
			if len(self.usuario.get()) !=0 and len(self.nuevo_password.get()) !=0 and len(self.respuesta.get()) !=0 and len(self.recuperar_password1.get()) !=0:
				return True
			else:
				messagebox.showerror("Error",f"Diligencie todos los campos")

		def validar_password(self):
			if (str(self.nuevo_password.get()) == str(self.recuperar_password1.get())):
				return True
			else:
				messagebox.showerror("ERROR DE RECUPERACION", f"Contraseña no coiciden")

		def validar_datos_usuario(self):
			usuario = self.usuario.get()
			respuesta = self.respuesta.get()
			busquedad = self.buscar_usuario(usuario, respuesta)
			if (busquedad !=[]):
				return True	

			else:
				messagebox.showerror("ERROR DE RECUPERACION", f"Datos de recuperación no son correctos")


		def buscar_usuario(self, usuario, respuesta):
			with sqlite3.connect(self.db_name) as conexion:
				cursor = conexion.cursor()
				query = f"SELECT * FROM Usuarios WHERE usuario={usuario} AND respuesta='{respuesta}'"
				cursor.execute(query)
				busquedad = cursor.fetchall()
				cursor.close()
				return busquedad


		def ejecutar_consulta(self, query, parameters=()):
			with sqlite3.connect(self.db_name) as conexion:
				cursor = conexion.cursor()
				result = cursor.execute(query, parameters)
				conexion.commit()
				return result


		def limpiar_formulario(self):
			self.usuario.delete(0, END)
			self.respuesta.delete(0, END)
			self.nuevo_password.delete(0, END)
			self.recuperar_password1.delete(0, END)



if __name__ == '__main__':
	ventana_recuperar = Tk()
	aplication = Recuperar(ventana_recuperar)
	ventana_recuperar.mainloop()