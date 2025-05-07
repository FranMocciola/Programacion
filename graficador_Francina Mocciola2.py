import tkinter as tk
from urllib.request import urlopen
import requests
from PIL import Image, ImageTk 
from io import BytesIO  

def descargarPortada():
    
    urlImagen = "https://github.com/FranMocciola/Programacion/blob/main/Portada%20Graficador%20de%20funciones.png?raw=true"
    datosImagen = urlopen(urlImagen)
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    
    return imagen

def descargarFondo2():
    urlImagen = "https://github.com/FranMocciola/Programacion/blob/b46591816533d7b5959665797cd143c384fdbc4a/Fondo2%20Graficador%20de%20funciones.png?raw=true"
    datosImagen = urlopen(urlImagen)
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
    

def funcionPolinomica():
    limpiarVentana()
    label=tk.Label(ventana, text="Función Polinómica", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.place(x=500,y=50)
    label=tk.Label(ventana, text="Ingresar el grado del polinomio", font=("Times New Roman", 18),fg="white", bg="skyblue")
    label.place(x=500,y=200)
    campo1=tk.Entry(ventana)
    campo1.place(x=500,y=300)
    
    def funcionPolinomica2():
        grado=int(campo1.get())
        limpiarVentana()
        label=tk.Label(ventana, text="Función Polinómica", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
        label.place(x=500,y=50)
        
        
        polinomio=list()
        i=grado
        for i in range(i,-1,-1):
            label=tk.Label(ventana, text=f"Ingresar el termino de {i}", font=("Times New Roman", 18),fg="white", bg="skyblue")
            label.pack(pady=5)
            campo2=tk.Entry(ventana)
            campo2.pack(pady=5)
            polinomio[i]=int(campo2.get())


        botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarOpcion1)
        botonVolver.place(x=500,y=600)
    botonOK = tk.Button(ventana, text="OK", font=("Arial",8,"bold"),width=5,bg="#334257",fg="white", command=funcionPolinomica2)
    botonOK.pack(pady=10)
    


    botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarOpcion1)
    botonVolver.place(x=500,y=600)
    
def funcionLogaritmica():
    limpiarVentana()
    label=tk.Label(ventana, text="Función Logaritmica", font=("Arial", 20, "bold"),fg="white", bg="skyblue")
    label.place(x=500,y=50)
    label=tk.Label(ventana, text="Ingresar la base", font=("Arial", 18),fg="white", bg="skyblue")
    label.place(x=500,y=100)
    campo1=tk.Entry()
    campo1.place(x=500,y=200)
    base=int(campo1.get())
    label=tk.Label(ventana, text="Ingresar el exponente", font=("Arial", 18),fg="white", bg="skyblue")
    label.place(x=500,y=300)
    campo1=tk.Entry()
    campo1.place(x=500,y=400)
    exponente=int(campo1.get())

    botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarMenu)
    botonVolver.place(x=500,y=600)
    
    
def funcionExponencial():
    limpiarVentana()

def mostrarOpcion1():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar función", font=("Arial", 40, "bold"),fg="white", bg="#212934")
    label.place(x=500,y=50)
    label=tk.Label(ventana, text="Ingresar función deseada", font=("Times New Roman", 20),fg="white", bg="#212934")
    label.place(x=500,y=100)
    botonP = tk.Button(ventana, text="Función Polinómica", font=("Courier New",15,"bold"),width=20,bg="#334257",fg="white", command=funcionPolinomica)
    botonP.place(x=500,y=200)
    botonL = tk.Button(ventana, text="Función Loragitmica", font=("Courier New",15,"bold"),width=20,bg="#334257",fg="white", command=funcionLogaritmica)
    botonL.place(x=500,y=300)
    botonE = tk.Button(ventana, text="Función Exponencial", font=("Courier New",15,"bold"),width=20,bg="#334257",fg="white", command=funcionExponencial)
    botonE.place(x=500,y=400)
      
    botonVolver = tk.Button(ventana, text="Volver", font=("Courier New",12,"bold"), width=20,bg="white", fg="black", command=mostrarMenu)
    botonVolver.place(x=500,y=600)
    
def mostrarOpcion2():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar puntos específicos sobre la función", font=("Arial", 40, "bold"),fg="white", bg="#212934")
    label.place(x=500,y=100)
    
def mostrarOpcion3():
    limpiarVentana()
    label=tk.Label(ventana, text="Encontrar raíces aproximadas de la función", font=("Arial", 40, "bold"),fg="white", bg="#212934")
    label.place(x=500,y=100)
  

    
def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()
    fondoTk=tk.Label(ventana, image=fondo)
    fondoTk.pack()

def mostrarMenu():
    limpiarVentana()
    
    label=tk.Label(ventana, text="Eliga la opción deseada", font=("Arial", 40, "bold"),fg="white", bg="#212934")
    label.place(x=500,y=100)
    
    boton1=tk.Button(ventana, text="Graficar función",font=("Courier New",12,"bold"), width=50,bg="#334257",fg="white", command=mostrarOpcion1)
    boton1.place(x=500,y=300)
    boton2=tk.Button(ventana, text="Graficar puntos específicos sobre la función",font=("Courier New",12,"bold"), width=50,bg="#334257",fg="white",  command=mostrarOpcion2)
    boton2.place(x=500,y=400)
    boton3=tk.Button(ventana, text="Encontrar raíces aproximadas de la función",font=("Courier New",12,"bold"), width=50,bg="#334257",fg="white", command=mostrarOpcion3)
    boton3.place(x=500,y=500)

def mostrarInicio():
    portadaTk=tk.Label(ventana, image=portada)
    portadaTk.place(x=0, y=0, relwidth=1, relheight=1)
    boton1=tk.Button(ventana, text="COMENZAR",font=("Courier New",25,"bold"), width=14,bg="#334257",fg="white", command=mostrarMenu)
    boton1.place(x=570, y=625)
    
    
def main():
    global ventana
    global portada
    global fondo
    
    ventana = tk.Tk()
    ancho = ventana.winfo_screenwidth()  
    alto = ventana.winfo_screenheight()  
    ventana.geometry(f"{ancho}x{alto}")
    ventana.title("Graficador de funciones")





    portadaBin=descargarPortada()
    portadaRedimensionada=portadaBin.resize((ancho, alto), Image.Resampling.LANCZOS)
    portada=ImageTk.PhotoImage(portadaRedimensionada)

    

    fondoBin=descargarFondo2()
    fondoRedimensionado=fondoBin.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondo=ImageTk.PhotoImage(fondoRedimensionado)

    

    
    mostrarInicio()
    
    
    
    

    

    ventana.mainloop()


if __name__=="__main__":
    main()
