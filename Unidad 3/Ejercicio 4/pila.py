from nodo import Nodo
class Pila:
    __ult:Nodo
    __cnt:int
    def __init__(self):
        self.__ult=None
        self.__cnt=0

    def agregarDato(self,elem):
        nodo=Nodo(elem)
        if self.__ult == None:
            self.__ult=nodo
        else:
            aux=nodo
            aux.setSig(self.__ult)
            self.__ult=aux
            del aux
        self.__cnt=+1
    
    def suprimirDato(self):
        if self.__ult == None:
            None
        else:
            aux=self.__ult
            self.__ult=self.__ult.getSig()
            self.__cnt-=1
        return aux

    def mostrarDatos(self):
        aux=self.__ult
        while self.__ult.getSig()!=None:
            print(self.__ult.getDato())
            self.__ult=self.__ult.getSig()
        print(self.__ult.getDato())
        self.__ult=aux

    def vacia(self):
        if self.__ult==None:
            return True


