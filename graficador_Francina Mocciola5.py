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

def graficarFuncionPolinomica():
    limpiarVentana()


def funcionPolinomica():
    polinomio=list()
    i=0
    def leerGrado():
        grado=int (campo1.get())
        funcionPolinomica2(grado)
    limpiarVentana()
    label=tk.Label(ventana, text="Función Polinómica", font=("Arial", 50, "bold"),fg="white", bg="#212934")
    label.place(x=400,y=75)
    label=tk.Label(ventana, text="Ingresar el grado del polinomio", font=("Times New Roman", 35),fg="white", bg="#212934")
    label.place(x=425,y=150)
    campo1=tk.Entry(ventana)
    campo1.place(x=615,y=350, width=200, height=75)

    botonOK = tk.Button(ventana, text="OK", font=("Arial",20,"bold"),width=8,bg="#334257",fg="white", command=leerGrado)
    botonOK.place(x=640, y=500)
    
   
    def funcionPolinomica2(grado):
        nonlocal polinomio, i
        i=grado
        polinomio=[0]*(grado+1)
        def leer ():
            polinomio[i]=float(campo2.get())
        limpiarVentana()
        label=tk.Label(ventana, text="Función Polinómica", font=("Arial", 50, "bold"),fg="white", bg="#212934")
        label.place(x=400,y=75)
        
        
        ##########     
        for i in range (grado,-1):
            label=tk.Label(ventana, text=f"Ingresar el termino del exponente {i}", font=("Times New Roman", 30),fg="white", bg="#212934")
            label.place(x=450, y=300)
            campo2=tk.Entry(ventana)
            campo2.place(x=615, y=400,width=200, height=65)
        
            botonOK = tk.Button(ventana, text="OK", font=("Arial",20,"bold"),width=8,bg="#334257",fg="white", command=leer)
            botonOK.place(x=635, y=550)

            label.destroy()

        botonVolver = tk.Button(ventana, text="Volver", font=("Times New Roman",15,"bold"), width=18,bg="white", fg="black", command=mostrarOpcion1)
        botonVolver.place(x=600,y=750)
    
    

    botonVolver = tk.Button(ventana, text="Volver", font=("Times New Roman",15,"bold"), width=18,bg="white", fg="black", command=mostrarOpcion1)
    botonVolver.place(x=600,y=750)
    
def funcionLogaritmica():
    limpiarVentana()
    label=tk.Label(ventana, text="Función Logaritmica", font=("Arial", 50, "bold"),fg="white", bg="#212934")
    label.place(x=500,y=50)
    label=tk.Label(ventana, text="Ingresar la base", font=("Arial", 35),fg="white", bg="#212934")
    label.place(x=500,y=100)
    campo1=tk.Entry()
    campo1.place(x=500,y=200)
    base=int(campo1.get())
    label=tk.Label(ventana, text="Ingresar el exponente", font=("Arial", 18),fg="white", bg="skyblue")
    label.place(x=500,y=300)
    campo1=tk.Entry()
    campo1.place(x=500,y=400)
    exponente=int(campo1.get())

    botonVolver = tk.Button(ventana, text="Volver", font=("Times New Roman",15,"bold"), width=18,bg="white", fg="black", command=mostrarMenu)
    botonVolver.place(x=600,y=750)
    
    
def funcionExponencial():
    limpiarVentana()

def mostrarOpcion1():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar función", font=("Arial", 50, "bold"),fg="white", bg="#212934")
    label.place(x=450,y=75)
    label=tk.Label(ventana, text="Ingresar función deseada", font=("Times New Roman", 35),fg="white", bg="#212934")
    label.place(x=475,y=175)
    botonP = tk.Button(ventana, text="Función Polinómica", font=("Courier New",20,"bold"),width=20,bg="#334257",fg="white", command=funcionPolinomica)
    botonP.place(x=550,y=325)
    botonL = tk.Button(ventana, text="Función Loragitmica", font=("Courier New",20,"bold"),width=20,bg="#334257",fg="white", command=funcionLogaritmica)
    botonL.place(x=550,y=450)
    botonE = tk.Button(ventana, text="Función Exponencial", font=("Courier New",20,"bold"),width=20,bg="#334257",fg="white", command=funcionExponencial)
    botonE.place(x=550,y=575)
      
    botonVolver = tk.Button(ventana, text="Volver", font=("Times New Roman",15,"bold"), width=18,bg="white", fg="black", command=mostrarMenu)
    botonVolver.place(x=600,y=750)
    
def mostrarOpcion2():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar puntos específicos sobre la función", font=("Arial", 40, "bold"),fg="white", bg="#212934")
    label.place(x=400,y=50)
    
def mostrarOpcion3():
    limpiarVentana()
    label=tk.Label(ventana, text="Encontrar raíces aproximadas de la función", font=("Arial", 40, "bold"),fg="white", bg="#212934")
    label.place(x=400,y=50)
  

    
def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()
    fondoTk=tk.Label(ventana, image=fondo)
    fondoTk.pack()

def mostrarMenu():
    limpiarVentana()
    
    label=tk.Label(ventana, text="Eliga la opción deseada", font=("Arial", 50, "bold"),fg="white", bg="#212934")
    label.place(x=350,y=100)
    
    boton1=tk.Button(ventana, text="Graficar función",font=("Courier New",20,"bold"), width=45,bg="#334257",fg="white", command=mostrarOpcion1)
    boton1.place(x=360,y=300)
    boton2=tk.Button(ventana, text="Graficar puntos específicos sobre la función",font=("Courier New",20,"bold"), width=45,bg="#334257",fg="white",  command=mostrarOpcion2)
    boton2.place(x=360,y=450)
    boton3=tk.Button(ventana, text="Encontrar raíces aproximadas de la función",font=("Courier New",20,"bold"), width=45,bg="#334257",fg="white", command=mostrarOpcion3)
    boton3.place(x=360,y=600)
    
def mostrarInicio():
    
    
    boton1=tk.Button(ventana, text="COMENZAR",font=("Courier New",25,"bold"), width=14,bg="#334257",fg="white", command=mostrarMenu)
    boton1.place(x=570, y=600)
    
    
def main():
    global ventana
    global portada
    global fondo
    global medio
    
    ventana = tk.Tk()
    ancho = ventana.winfo_screenwidth()  
    alto = ventana.winfo_screenheight()  
    ventana.geometry(f"{ancho}x{alto}")
    ventana.title("Graficador de funciones")
    medio=ancho/2




    portadaBin=descargarPortada()
    portadaRedimensionada=portadaBin.resize((ancho, alto), Image.Resampling.LANCZOS)
    portada=ImageTk.PhotoImage(portadaRedimensionada)
    
    ventana.portada=portada
    etiqueta=tk.Label(ventana,image=portada)
    etiqueta.place(x=0, y=0, relwidth=1, relheight=1)

    fondoBin=descargarFondo2()
    fondoRedimensionado=fondoBin.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondo=ImageTk.PhotoImage(fondoRedimensionado)

    

    
    mostrarInicio()
    
    
    
    

    

    ventana.mainloop()


if __name__=="__main__":
    main()
