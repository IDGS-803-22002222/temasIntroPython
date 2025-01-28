import os
from io import open

class Diccionario:
    
    opcionMenu=0
    palabraEspa=""
    palabraIngles=""
    busqueda=""
    lectura=""
    resultadoEspañol=""
    resultadoIngles=""

    def menuCapturar(self):
        self.palabraEspa=input("palabra en español: ")
        self.palabraIngles=input("palabra en ingles: ")
        archivo=open("archivo.txt","a")
        #archivo.write(self.palabraEspa,":",self.palabraIngles)
        archivo.write("{} : {}\n".format(self.palabraEspa,self.palabraIngles))
        os.system('cls')    
        print("Palabra guardada")
        
                    
    
    def menuBuscar(self):
        print("Buscar en: ")
        print("1. Español")
        print("2. Inglés")
        opcionBusqueda = input("Opción: ")

        self.busqueda = input("Palabra a buscar: ")
        
    
        archivo = open("archivo.txt", "r")
        lineas = archivo.readlines()
        print(lineas)
        archivo.close()
        

        
        for linea in lineas:
            partes = linea.split(":")
            #print(partes)
            self.resultadoEspañol = partes[0].strip()
            self.resultadoIngles = partes[1].strip()
            #print(self.resultadoEspañol)
            #print(self.resultadoIngles)
            if opcionBusqueda == "1":
                if self.busqueda.lower() == self.resultadoEspañol.lower():
                    os.system('cls')
                    print("palabra encontrada: {}".format(self.resultadoIngles))
                    return  

           
            elif opcionBusqueda == "2":
                if self.busqueda.lower() == self.resultadoIngles.lower():
                    os.system('cls')
                    print("palabra encontrada: {}".format(self.resultadoEspañol))
                    return  

        
        os.system('cls')
        print("palabra no encontrada.")


    def menuPrincipal(self):
        while(self.opcionMenu!=3):
            print("---Diccionario---")
            print("1-Capturar palabra")
            print("2-Buscar Palabra")
            print("3-salir")
            self.opcionMenu=int(input("Opcion: "))
            if self.opcionMenu==1:
                self.menuCapturar()
            elif self.opcionMenu ==2:
                self.menuBuscar()
            elif self.opcionMenu >=3:
                print("bay") 



def main():
    obj=Diccionario()
    obj.menuPrincipal()

if __name__=="__main__":
    main()