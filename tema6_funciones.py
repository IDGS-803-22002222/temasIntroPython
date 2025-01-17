import os


def Suma():
    
    #print("Hola soy funcion 1")
    print("Dame dos numeros para sumar")
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    os.system('cls')
    print("El resultado de la suma es ", (num1+num2))
    


def resta():
    #print("Hola soy funcion 1")
    print("Dame dos numeros para restar")
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    os.system('cls')
    print("El resultado de la resta es ", num1-num2)

def divicion():
    
    #print("Hola soy funcion 1")
    print("Dame dos numeros para dividir")
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    if num2== 0:
        os.system('cls')
        print("No se puede dividir entre 0")
    else:
        os.system('cls')
        print("El resultado de la divicion es ", num1/num2)


def multiplicacion():
    #print("Hola soy funcion 1")
    print("Dame dos numeros a multiplicar")
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    os.system('cls')
    print("El resultado de la multiplicacion es ", num1*num2)

#funcion1()

#funcion2()


def run():
    
    opcion=0
    while(opcion!=5):
        
        print("Menu de opciones: ")
        print("1-Suma \n"+
            "2-Resta \n"+
            "3-Multiplicacion \n"+
            "4-Divicion \n"+
            "5-Salir \n")
        opcion=int(input("Opcion: "))
        if opcion==1:
            Suma()
        elif opcion==2:
            resta()
        elif opcion==3:
            multiplicacion()
        elif opcion==4:
            divicion()
        elif opcion >=5:
            print("bay") 
 
    

if __name__ == "__main__":
    run()