import tkinter as tk

def mostrarOpcion1():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar función", font=("Arial", 20, "bold"))
    label.pack(pady=20)
    
def mostrarOpcion2():
    limpiarVentana()
    label=tk.Label(ventana, text="Graficar puntos específicos sobre la función", font=("Arial", 20, "bold"))
    label.pack(pady=20)
def mostrarOpcion3():
    limpiarVentana()
    label=tk.Label(ventana, text="Encontrar raíces aproximadas de la función", font=("Arial", 20, "bold"))
    label.pack(pady=20)
  

    


def limpiarVentana():
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrarMenu():
    limpiarVentana()
    label=tk.Label(ventana, text="Eliga la opción deseada", font=("Arial", 20, "bold"))
    label.pack(pady=20)
    
    boton1=tk.Button(ventana, text="Graficar función",font=("Arial",14), width=40, command=mostrarOpcion1)
    boton1.pack(pady=10)
    boton2=tk.Button(ventana, text="Graficar puntos específicos sobre la función",font=("Arial",14), width=40, command=mostrarOpcion2)
    boton2.pack(pady=10)
    boton3=tk.Button(ventana, text="Encontrar raíces aproximadas de la función",font=("Arial",14), width=40,command=mostrarOpcion3)
    boton3.pack(pady=10)
   
    
def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry ("600x500")
    ventana.title("Graficador de funciones")

    mostrarMenu()

    

    ventana.mainloop()


if __name__=="__main__":
    main()
