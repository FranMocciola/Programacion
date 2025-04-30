import tkinter as tk
from urllib.request import urlopen  
from PIL import Image, ImageTk 
from io import BytesIO  

def descargarPortada():
    urlImagen = "https://github.com/FranMocciola/Programacion/blob/main/Portada%20Graficador%20de%20funciones.png?raw=true"
    datosImagen = urlopen(urlImagen)
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarFondo2():
    urlImagen = "https://github.com/FranMocciola/Programacion/blob/main/Fondo2%20Graficador%20de%20funciones.png?raw=true"
    datosImagen = urlopen(urlImagen)
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
    

def funcionPolinomica():
    limpiarVentana()
    label=tk.Label(ventana, text="Función Polinómica", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.pack(pady=20)
    label=tk.Label(ventana, text="Ingresar el grado del polinomio", font=("Times New Roman", 18),fg="white", bg="skyblue")
    label.pack(pady=20)
    campo1=tk.Entry(ventana)
    campo1.pack(pady=10)
    
    def funcionPolinomica2():
        grado=int(campo1.get())
        limpiarVentana()
        label=tk.Label(ventana, text="Función Polinómica", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
        label.pack(pady=20)
        
        
        polinomio=list()
        i=grado
        for i in range(i,-1,-1):
            label=tk.Label(ventana, text=f"Ingresar el termino de {i}", font=("Times New Roman", 18),fg="white", bg="skyblue")
            label.pack(pady=5)
            campo2=tk.Entry(ventana)
            campo2.pack(pady=5)
            


        botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarOpcion1)
        botonVolver.pack(pady=50)
    botonOK = tk.Button(ventana, text="OK", font=("Arial",8,"bold"),width=5,bg="#334257",fg="white", command=funcionPolinomica2)
    botonOK.pack(pady=10)
    


    botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarOpcion1)
    botonVolver.pack(pady=50)
    
def funcionLogaritmica():
    limpiarVentana()
    label=tk.Label(ventana, text="Función Logaritmica", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.pack(pady=20)
    label=tk.Label(ventana, text="Ingresar la base", font=("Arial", 18),fg="white", bg="skyblue")
    label.pack(pady=10)
    campo1=tk.Entry()
    campo1.pack(pady=10)
    base=int(campo1.get())
    label=tk.Label(ventana, text="Ingresar el exponente", font=("Arial", 18),fg="white", bg="skyblue")
    label.pack(pady=10)
    campo1=tk.Entry()
    campo1.pack(pady=10)
    exponente=int(campo1.get())

    botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarMenu)
    botonVolver.pack(pady=50)
    
    
def funcionExponencial():
    limpiarVentana()

def mostrarOpcion1():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar función", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.pack(pady=20)
    label=tk.Label(ventana, text="Ingresar función deseada", font=("Times New Roman", 18),fg="white", bg="skyblue")
    label.pack(pady=10)
    botonP = tk.Button(ventana, text="Función Polinómica", font=("Courier New",12,"bold"),width=20,bg="#334257",fg="white", command=funcionPolinomica)
    botonP.pack(pady=10)
    botonL = tk.Button(ventana, text="Función Loragitmica", font=("Courier New",12,"bold"),width=20,bg="#334257",fg="white", command=funcionLogaritmica)
    botonL.pack(pady=10)
    botonE = tk.Button(ventana, text="Función Exponencial", font=("Courier New",12,"bold"),width=20,bg="#334257",fg="white", command=funcionExponencial)
    botonE.pack(pady=10)
      
    botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarMenu)
    botonVolver.pack(pady=50)
    
def mostrarOpcion2():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar puntos específicos sobre la función", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.pack(pady=20)
    
def mostrarOpcion3():
    limpiarVentana()
    label=tk.Label(ventana, text="Encontrar raíces aproximadas de la función", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.pack(pady=20)
  

    
def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()
    eFondo=tk.Label(ventana, image=fondoTk)
    eFondo.pack()

def mostrarMenu():
    limpiarVentana()
    fondo2=descargarFondo2()
    fondo2Redimensionado=fondo2.resize((ancho, alto), Image.Resampling.LANCZOS)
    label=tk.Label(ventana, text="Eliga la opción deseada", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.pack(pady=20)
    
    boton1=tk.Button(ventana, text="Graficar función",font=("Courier New",12,"bold"), width=50,bg="#334257",fg="white", command=mostrarOpcion1)
    boton1.pack(pady=10)
    boton2=tk.Button(ventana, text="Graficar puntos específicos sobre la función",font=("Courier New",12,"bold"), width=50,bg="#334257",fg="white",  command=mostrarOpcion2)
    boton2.pack(pady=10)
    boton3=tk.Button(ventana, text="Encontrar raíces aproximadas de la función",font=("Courier New",12,"bold"), width=50,bg="#334257",fg="white", command=mostrarOpcion3)
    boton3.pack(pady=10)

def mostrarInicio():
    ePortada=tk.Label(ventana, image=portadaTk)
    ePortada.pack()
    botonComenzar=tk.Button(ventana, text="COMENZAR",font=("Courier New",10,"bold"), width=20,bg="#334257",fg="white", command=mostrarMenu)
    boton1.pack(pady=10)
    
    
def main():
    global ventana
    global portada
    global fondo
    
    ventana = tk.Tk()
    ancho = ventana.winfo_screenwidth()  
    alto = ventana.winfo_screenheight()  
    ventana.geometry(f"{ancho}x{alto}")
    ventana.title("Graficador de funciones")





    portada=descargarPortada()
    portadaRedimensionada=portada.resize((ancho, alto), Image.Resampling.LANCZOS)
    portadaTk=ImageTk.PhotoImage(portadaRedimensionada)

    fondoTk=ImageTk.PhotoImage(fondoRedimensionado)

    fondo=descargarFondo2()
    
    fondoRedimensionado=fondo.resize((ancho, alto), Image.Resampling.LANCZOS)

    
    mostrarInicio()
    
    
    
    

    

    ventana.mainloop()


if __name__=="__main__":
    main()
