from pila import Pila

if __name__=='__main__':
    pila1=Pila()
    pila2=Pila()
    pila3=Pila()
    n=int(input("Ingrese numero a convertir:"))
    pila1.agregarDato(n)
    b=n
    while b>1:
        b=b-1
        print(b)
        pila1.agregarDato(b)
    for i in range(0,n):
        pila2.agregarDato(0)
        pila3.agregarDato(0)
    mn=True
    while mn!=False:
        print(pila1.mostrarDatos())
        #print("Pila 2:",pila2.mostrarDatos())
        #print("Pila 3:",pila3.mostrarDatos())
        op1=int(input("Seleccione pila de donde mover:"))
        op2=int(input("Seleccione pila hacia donde se movera:"))
        if op1==1 and op2==2:
            if pila2.vacia():
                pila2.agregarDato(pila1.recuperar())
                pila1.suprimirDato()
            else:
                if pila1.recuperar() > pila2.recuperar():
                    pila2.agregarDato(pila1.recuperar())
                    pila1.suprimirDato()
                else:
                    print("No se puede realizar el movimiento porque la Torre 2 Tiene un numero mayor que la Torre1")
        if op1==1 and op2==3:
            if pila3.vacia():
                pila3.agregarDato(pila1.recuperar())
                pila1.suprimirDato()
            else:
                if pila1.recuperar() > pila3.recuperar():
                    pila3.agregarDato(pila1.recuperar())
                    pila1.suprimirDato()
                else:
                    print("No se puede realizar el movimiento porque la Torre 3 Tiene un numero mayor que la Torre1")
        if op1==2 and op2==1:
            if pila1.vacia():
                pila1.agregarDato(pila2.recuperar())
                pila2.suprimirDato()
            else:
                if pila2.recuperar() > pila1.recuperar():
                    pila1.agregarDato(pila2.recuperar())
                    pila2.suprimirDato()
                else:
                    print("No se puede realizar el movimiento porque la Torre 1 Tiene un numero mayor que la Torre2")
        if op1==2 and op2==3:
            if pila3.vacia():
                pila3.agregarDato(pila2.recuperar())
                pila2.suprimirDato()
            else:
                if pila2.recuperar() > pila3.recuperar():
                    pila3.agregarDato(pila2.recuperar())
                    pila2.suprimirDato()
                else:
                    print("No se puede realizar el movimiento porque la Torre 3 Tiene un numero mayor que la Torre2")
        if op1==3 and op2==1:
            if pila1.vacia():
                pila1.agregarDato(pila3.recuperar())
                pila3.suprimirDato()
            else:
                if pila3.recuperar() > pila1.recuperar():
                    pila1.agregarDato(pila3.recuperar())
                    pila3.suprimirDato()
                else:
                    print("No se puede realizar el movimiento porque la Torre 1 Tiene un numero mayor que la Torre3")
        if op1==3 and op2==2:
            if pila2.vacia():
                pila2.agregarDato(pila3.recuperar())
                pila3.suprimirDato()
            else:
                if pila3.recuperar() > pila2.recuperar():
                    pila2.agregarDato(pila3.recuperar())
                    pila3.suprimirDato()
                else:
                    print("No se puede realizar el movimiento porque la Torre 2 Tiene un numero mayor que la Torre3")

