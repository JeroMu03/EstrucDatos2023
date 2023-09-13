from pila import Pila

if __name__=='__main__':
    pila=Pila()
    num=int(input("Ingrese numero a convertir:"))
    while num!=0:
        elem=num%2
        num=num//2
        pila.agregarDato(elem)
    pila.mostrarDatos()