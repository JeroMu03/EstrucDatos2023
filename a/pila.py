from nodo import Nodo
class Pila:
    __tope:Nodo
    __cnt:int
    def __init__(self):
        self.__tope=None
        self.__top=0

    def agregarDato(self,elem):
        nodo=Nodo(elem)
        if self.__ult == None:
            self.__ult=nodo
        else:
            aux=nodo
            aux.setSig(self.__ult)
            self.__ult=nodo
            del aux
        self.__cnt=+1
    
    def suprimirDato(self):
        if self.__ult == None:
            None
        else:
            self.__ult=self.__ult.getSig()
            self.__cnt-=1
        del aux

    # def recorrer(self):
    #     lista=[]
    #     aux=self.__comienzo
    #     if aux.getSig()==None:
    #         print(aux.getDato)
    #     else:
    #         for i in int(self.__tope):
    #             while aux.getSig()!=None:
    #                 aux=aux.getSig()
    #             lista.append(aux)
    #             self.suprimirDato()


