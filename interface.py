import tkinter as tk
from tkinter import INSERT, ttk
from tkinter import filedialog
from tkinter import messagebox
from analizador_lexico import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        #Window config
        self.title("Proyecto 1") # Titulo de ventana
        self.resizable(False, False) #Editable
        self.addWidgets() # Creamos los widgets

    def addWidgets(self):

        #Configuracion ventana
        self.configure(bg="#1c313a") #Color de fondo
        self.file = None

        # Funcion para abrir archivo
        def openFile():

            #Abrimos el archivo
            try:
                self.file = filedialog.askopenfile()

                #Leemos el contenido
                lectura = self.file.read()
                self.file.close() # Cerramos el archivo
                txt_area.insert(INSERT, lectura) #insertamos el contenido en el text area
            
            except Exception:
                messagebox.showerror("Archivo incorrecto", "Abra un archivo valido") 


        # Funcion para guardar archivo
        def saveFile():

            new_file = filedialog.asksaveasfilename(defaultextension="txt", 
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]) #Cuadro de dialogo

            if not new_file: #Validar que se este guardando un archivo
                return messagebox.showerror("Error", "No se ha guardado ningun archivo") # En caos no se guarde

            messagebox.showinfo("Guardar archivo", "Archivo guardado correctamente")
            new_archivo = open(new_file, "w")
            txt_entrada = txt_area.get(1.0, tk.END)

            new_archivo.write(txt_entrada)
            new_archivo.close()

        # Funcion para analizar archivo
        def parseFile():

            estructure = txt_area.get(1.0, tk.END) #Tomamos el texto del area de texto

            if str(estructure).isspace():
                messagebox.showerror("Archivo invalido", "Verifique que haya abierto un archivo, \n           o un archivo adecuado") # Si el text esta vacio
            
            else:
                # Proceso, para el analizador lexico
                variable = parse(estructure)

                getERFalse = False #Para obtener el resultado
                getERTrue = True # Para obtener la expresion regular
                n = 1
                print()
                
                if variable:
                    for var in variable:
                        if isinstance(var, list): # Para obtener las operaciones
                            for var_ in var:
                                print(f"Operacion {n}:")
                                print(str(var_.ejecutar(getERTrue))+" = " + str(var_.ejecutar(getERFalse)))
                                print()
                                n+=1
                        elif isinstance(var, Texto): # Para obtener el texto
                            print(var.ejecutar(getERTrue))
                        elif isinstance(var, Funcion):
                            print(var.ejecutar(getERTrue)) # Para obtener la funcion 

                messagebox.showinfo("Analizador", "Archivo Analizado correctamente")

        # Funcion para verificar errores
        def parse_errores_File():

            estructure = txt_area.get(1.0, tk.END) #Tomamos el texto del area de texto

            if str(estructure).isspace():
                messagebox.showerror("Archivo invalido", "Verifique que haya abierto un archivo, \n           o un archivo adecuado") # Si el text esta vacio

            else:
                #Errores
                print("Errores\n")
                cc = 1
                for var in errores_:
                    print(f"\tError {cc}:")
                    print(var.toString())
                    print()
                    cc+=1
                
                messagebox.showinfo("Errores", "Archivo 'html' generado correctamente")

        #Create buttons
        btn_abrir = tk.Button(self, text="ABRIR", command = openFile ,font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_guardar = tk.Button(self, text="GUARDAR", command=saveFile, font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_analizar = tk.Button(self, text="ANALIZAR", command = parseFile, font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_errores = tk.Button(self, text="ERRORES", command = parse_errores_File,font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_salir = tk.Button(self, text="SALIR", command = lambda: self.quit(),  font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")

        #Create Text area
        txt_area = tk.Text(self, bg="#b0bec5", font=("Calisto MT", 12), padx=20, pady=20)

        #Create combobox
        style = ttk.Style()
        style.theme_create('combostyle', parent='alt',
                                settings = {'TCombobox':
                                            {'configure':
                                            {'selectbackground': '#455a64',
                                            'fieldbackground': '#455a64',
                                            'background': '#455a64'
                                            }}})
        style.theme_use('combostyle') 
        options = ["Ayuda", "Manual de Usuario", "Manual Tecnico", "Autor"] #Lista de opciones
        cmb_ayuda = ttk.Combobox(self, values = options, foreground="White",  font= ("Berlin Sans FB Demi", 13, "bold"), justify = "center", state = "readonly")
        cmb_ayuda.current(0)

        #Ubicacion widgets
        btn_abrir.grid(row=0, column=0, sticky="nsew")
        btn_guardar.grid(row=0, column=1, sticky="nsew")
        btn_analizar.grid(row=0, column=2, sticky="nsew")
        btn_errores.grid(row=0, column=3, sticky="nsew")
        btn_salir.grid(row=2, column=4, sticky="nsew", padx=15, pady=15)
        cmb_ayuda.grid(row=0, column=4, sticky="nsew")
        txt_area.grid(row=1, column=0, columnspan=5, padx=15, pady=15)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()