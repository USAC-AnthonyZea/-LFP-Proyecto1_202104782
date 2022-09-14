import tkinter as tk
from tkinter import INSERT, ttk
from tkinter import filedialog

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

        # Funcion para abrir archivo
        def openFile():

            #Abrimos el archivo
            try:
                file = filedialog.askopenfile()
            except TypeError:
                print("Archivo incorrecto")
            
            #Leemos el contenido
            lectura = file.read()
            file.close() # Cerramos el archivo

            txt_area.insert(INSERT, lectura) #insertamos el contenido en el text area
            
        # Funcion para guardar archivo
        def saveFile():

            new_file = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

            if not new_file:
                return 
            new_archivo = open(new_file, "w")
            txt_entrada = txt_area.get(1.0, tk.END)

            new_archivo.write(txt_entrada)
            new_archivo.close()

        #Create buttons
        btn_abrir = tk.Button(self, text="ABRIR", command = openFile ,font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_guardar = tk.Button(self, text="GUARDAR", command=saveFile, font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_analizar = tk.Button(self, text="ANALIZAR", font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
        btn_errores = tk.Button(self, text="ERRORES", font=("Berlin Sans FB Demi", 13, "bold"), bg="#455a64", fg="white")
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