def main():
    print ("1.Sumar")
    print ("2.Restar")
    print ("3.Multiplicar")
    print ("4.Dividir")
    opcion=int (input("Ingresar opción deseada"))
    n1=int(input("Ingresar un número"))
    n2=int (input("Ingresar otro número"))
    match opcion:
        case 1:
            print(n1+n2)
        case 2:
            print (n1-n2)
        case 3:
            print (n1*n2)
        case 4:
            if n2==0:
                print("La operación no es valida")
            else:
                print (n1/n2)

if __name__=="__main__":
    main()
