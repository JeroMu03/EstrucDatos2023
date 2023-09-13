from pila import Pila

if __name__=='__main__':
    pila=Pila()
    num=int(input("Ingrese numero a convertir:"))
    for i in range(1,num):
        num=i*num
        pila.agregarDato(num)
    pila.mostrarDatos()
