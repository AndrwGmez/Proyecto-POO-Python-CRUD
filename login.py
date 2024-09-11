#Importar la libreria 
from tkinter import * 
from PIL import ImageTk, Image
import sys
from subprocess import call
import sqlite3
from tkinter import messagebox

#pip install pillow

class Login():

	db_name = ("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/db2503319.db")
	
	#db_name = "C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/3/db2503319.db"


	def __init__(self, ventana_login):
		'''------------- Atributos de la ventana ------------- '''
		self.window = ventana_login
		#Titulo ventana 

		self.window.title("Ingreso")

		self.window.geometry("350x420")
		#Tamaño ventana 

		self.window.iconbitmap("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/calcu.ico")
		
		#self.window.iconbitmap("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/3/calcu.ico")
		#Ruta  icono 

		self.window.resizable(0,0)
		#Tamaño de ventana 

		self.window.config(bd=10) 	
		#Para no haber cambios en el tamaño ventana 

		titulo = Label(ventana_login, text="INICIAR SESION", fg="black", font=("Comic Sans MS", 13, "bold"), pady=10).pack()



		'''------------- Logo del login ------------- '''

		#imagen_login = Image.open("C:/Users/Aprendiz/Documents/Veri No Tocar/Inter/login/registrarse.png")

		imagen_login = Image.open("C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/registrarse.png")

		#Tamaño de la imagen 
		nueva_imagen = imagen_login.resize((40,40))

		#Renderizar imagen
		render = ImageTk.PhotoImage(nueva_imagen)

		#
		label_imagen = Label(ventana_login, image=render)

		label_imagen.image = render

		label_imagen.pack(pady=5)


		'''------------- Marco del login ------------- '''

		marco = LabelFrame(ventana_login, text="Ingrese sus datos", font=("Comic Sans MS", 10, "bold"))
		marco.pack()

		'''------------- Formulario del login ------------- '''

		label_usuario = Label(marco, text ="Usuario :", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=10)
		#label de usuario
		
		self.usuario = Entry(marco, width=25)


		self.usuario.focus()
		#Focus ubica el cursor  en el entre de self usuario

		self.usuario.grid(row=0, column=1, padx=5, pady=10)

		label_password = Label(marco, text="Contraseña", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=0, sticky="s", pady=5)

		self.password = Entry(marco, width=25, show="*")
		self.password.grid(row=1, column=1, padx=5, pady=10)


		'''-------------  Botones del login ------------- '''

		frame_botones = Frame(ventana_login)
		frame_botones.pack()

		boton_ingresar = Button(frame_botones, text="Ingresar", command=self.login, height=2, width=12, bg="green", fg="white", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=1, padx=10, pady=15)
		boton_registrar = Button(frame_botones, text="Registrar", command=self.llamar_login, height=2, width=12, bg="blue", fg="white", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=2, padx=10, pady=15)
		label_olvido = Label(frame_botones, text="Olvidó Contraseña",  font=("Comic Sans Ms", 10 , "bold")).grid(row=1, column=1, columnspan=2, sticky='s')
		boton_recuperar = Button(frame_botones, text="Recuperar Contraseña", command=self.llamar_recuperar,height=2, width=24, bg="orange", fg="white", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=1, columnspan=2, padx=10, pady=15)


	def llamar_recuperar(self):
		ventana_login.destroy()
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/recuperar.py'])


	def llamar_login(self):
		ventana_login.destroy()
		#call([sys.executable, 'C:/Users/Aprendiz/Documents/Veri No Tocar/Inter/login/registro.py'])
		call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/registro.py'])


	def login(self):
		if (self.validar_formulario_completo()):
			usuario = self.usuario.get()
			password = self.password.get()
			dato = self.validar_login(usuario, password)
			if (dato != []):
				messagebox.showinfo("Bienvenido", "Los Datos Ingresados son correctos")
				ventana_login.destroy()
				call([sys.executable, 'C:/Users/jhefe/Downloads/SENA ADSO 2022/Trimestre 5/YULY/Interfaz/Forms - Data Base/9/productos.py'])

			else:
				messagebox.showerror("Error de ingreso","Los datos fueron ingresados incorrectamente")

	def validar_formulario_completo(self):
		if len(self.usuario.get()) !=0 and len(self.password.get()) !=0:
			return True

		else:
			messagebox.showerror("Error de ingreso","Ingrese los datos requeridos")


	def validar_login(self, usuario, password):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = f"SELECT * FROM Usuarios WHERE usuario={usuario} AND password ={password}"
			cursor.execute(sql)
			validacion = cursor.fetchall()
			cursor.close()
			return validacion



if __name__ == '__main__':
	ventana_login = Tk()
	aplication = Login(ventana_login)
	ventana_login.mainloop()