import tkinter as tk
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox as mb
from project import main


class FormularioArticulos:
    def __init__(self):
        self.consultasBD = main.DataBase()
        self.ventana = tk.Tk()
        self.ventana.title("Gestion de usuarios")
        self.ventana.iconbitmap("user.ico")
        self.ventana.config(width="1000", height="700")
        self.consulta_por_codigo()
        self.listar()
        self.ventana.mainloop()

    def listar(self):
        self.tabla.delete(*self.tabla.get_children())

        respuesta = self.consultasBD.select_all()
        for fila in respuesta:
            self.tabla.insert("", tk.END, text=fila[0],
                              values=(fila[1], fila[2], fila[3], fila[4], fila[5]))

    def agregar(self):
        if len(self.documento.get()) > 0:
            self.consultasBD.insert_user(self.documento.get(), self.nombres.get(), self.apellidos.get(), self.ciudad.get(),
                                     self.telefono.get(), self.email.get())

            self.listar()
        else:
            mb.showerror("Error", "Por favor llenar todos los campos")

        self.limpiar()

    def consulta_por_codigo(self):
        style = ttk.Style()
        style.configure('Red.TLabelframe.Label', font=('Calibri', 13, 'bold'))
        self.labelframe2 = ttk.LabelFrame(self.ventana, text="Usuario", style="Red.TLabelframe")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=0)

        self.label1 = ttk.Label(self.labelframe2, text="Documento:")
        self.label1.config(font=('Calibri', 13, 'bold'))
        self.label1.grid(column=0, row=0, padx=1, pady=4)
        self.documento = tk.StringVar()
        self.entrydocumento = ttk.Entry(self.labelframe2, textvariable=self.documento)
        self.entrydocumento.grid(column=1, row=0, padx=1, pady=4)

        self.label2 = ttk.Label(self.labelframe2, text="Nombres:")
        self.label2.config(font=('Calibri', 13, 'bold'))
        self.label2.grid(column=2, row=0, padx=1, pady=4)
        self.nombres = tk.StringVar()
        self.entrynombres = ttk.Entry(self.labelframe2, textvariable=self.nombres)
        self.entrynombres.grid(column=3, row=0, padx=1, pady=4)

        self.label3 = ttk.Label(self.labelframe2, text="Apellidos:")
        self.label3.config(font=('Calibri', 13, 'bold'))
        self.label3.grid(column=4, row=0, padx=4, pady=4)
        self.apellidos = tk.StringVar()
        self.entryapellidos = ttk.Entry(self.labelframe2, textvariable=self.apellidos)
        self.entryapellidos.grid(column=5, row=0, padx=4, pady=4)

        self.label4 = ttk.Label(self.labelframe2, text="Ciudad:")
        self.label4.config(font=('Calibri', 13, 'bold'))
        self.label4.grid(column=0, row=2, padx=1, pady=4)
        self.ciudad = tk.StringVar()
        self.entryciudad = ttk.Entry(self.labelframe2, textvariable=self.ciudad)
        self.entryciudad.grid(column=1, row=2, padx=1, pady=4)

        self.label5 = ttk.Label(self.labelframe2, text="Telefono:")
        self.label5.config(font=('Calibri', 13, 'bold'))
        self.label5.grid(column=2, row=2, padx=4, pady=4)
        self.telefono = tk.StringVar()
        self.entrytelefono = ttk.Entry(self.labelframe2, textvariable=self.telefono)
        self.entrytelefono.grid(column=3, row=2, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe2, text="Email:")
        self.label6.config(font=('Calibri', 13, 'bold'))
        self.label6.grid(column=4, row=2, padx=4, pady=4)
        self.email = tk.StringVar()
        self.entryemail = ttk.Entry(self.labelframe2, textvariable=self.email)
        self.entryemail.grid(column=5, row=2, padx=4, pady=4)

        self.boton1 = self.createButton("Ingresar", "deep sky blue", self.agregar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        self.boton2 = self.createButton("Consultar", "deep sky blue", self.consultar)
        self.boton2.grid(column=2, row=3, padx=4, pady=4)

        self.boton3 = self.createButton("Modificar", "springgreen3", self.modificar)
        self.boton3.grid(column=3, row=3, padx=4, pady=20)

        self.boton4 = self.createButton("Eliminar", "red2", self.eliminar)
        self.boton4.grid(column=4, row=3, padx=1, pady=1)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tabla = ttk.Treeview(self.labelframe2, columns=("#1", "#2", "#3", "#4", "#5"), style="mystyle.Treeview")
        self.tabla.grid(row=4, columnspan=7, padx=7)
        self.tabla.heading("#0", text="Documento", anchor=tk.CENTER)
        self.tabla.heading("#1", text="Nombres", anchor=tk.CENTER)
        self.tabla.heading("#2", text="Apellidos", anchor=tk.CENTER)
        self.tabla.heading("#3", text="Ciudad", anchor=tk.CENTER)
        self.tabla.heading("#4", text="Telefono", anchor=tk.CENTER)
        self.tabla.heading("#5", text="Email", anchor=tk.CENTER)

        self.boton4 = self.createButton("Cancelar", "red2", self.limpiar)
        self.boton4.grid(column=6, row=6, padx=4, pady=10)

    def createButton(self, text, color, event):
        return Button(self.labelframe2, text=text, command=event, background=color, font=
        ('calibri', 13, 'bold'), foreground="white", width="10")

    def limpiar(self):
        self.documento.set('')
        self.nombres.set('')
        self.apellidos.set('')
        self.ciudad.set('')
        self.telefono.set('')
        self.email.set('')

    def eliminar(self):
        if len(self.documento.get()) > 0:
            self.consultasBD.delete_user(self.documento.get())
            mb.showinfo("Información", "Se eliminó el usuario con éxito")
            self.listar()

        else:
            mb.showerror("Error", "Por favor llenar el campo documento")

        self.limpiar()

    def consultar(self):
        datos = (self.documento.get())
        if len(datos) > 0:
            respuesta = self.consultasBD.select_user(datos)
            if len(respuesta) > 0:
                self.nombres.set(respuesta[1])
                self.apellidos.set(respuesta[2])
                self.ciudad.set(respuesta[3])
                self.telefono.set(respuesta[4])
                self.email.set(respuesta[5])
            else:
                self.limpiar()
                mb.showinfo("Información", "No existe un artículo con dicho código")
        else:
            mb.showerror("Error", "Por favor llenar el campo documento")
            self.limpiar()

    def modificar(self):
        if len(self.documento.get()) > 0:
            self.consultasBD.update_user(self.documento.get(), self.nombres.get(), self.apellidos.get(), self.ciudad.get(),
                                     self.telefono.get(), self.email.get())

            mb.showinfo("Información", "Se modificó el usuario con éxito")
            self.listar()
        else:
            mb.showerror("Error", "Por favor llenar el campo documento")
        self.limpiar()

aplicacion1 = FormularioArticulos()
