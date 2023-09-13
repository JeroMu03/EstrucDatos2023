from nodo import Nodo
class Lista:
    __com:Nodo
    __cnt:int
    def __init__(self):
        self.__com=None
        self.__cnt=0

    def agregarDato(self,elem,p):
        if p>=1 and p<=self.__cnt+1:
            i=1
            nodo=Nodo(elem)
            if p==1:
                aux=nodo
                aux.setSig(self.__com)
                self.__com=aux
            else:
                anterior=self.__com
                aux=self.__com
                while aux.getSig()!=None and i<p:
                    anterior=aux
                    aux=aux.getSig()
                    i+=1
                nodo.setSig(anterior.getSig())
                anterior.setSig(nodo)
            self.__cnt=self.__cnt + 1
        else:
            print("Posicion no valida")
    
    def sup(self,p):
        if p>=1 and p<=self.__cnt+1:
            i=1
            if p==1:
                aux=self.__com.getSig()
                self.__com=aux
                del aux
            else:
                anterior=self.__com
                aux=self.__com
                while aux.getSig()!=None and i<p:
                    anterior=aux
                    aux=aux.getSig()
                    i+=1
                anterior.setSig(aux.getSig())
                del aux
            self.__cnt=self.__cnt - 1
        else:
            print("Posicion no valida")

    def recup(self,p):
        if p>=1 and p<=self.__cnt+1:
            aux=self.__com
            i=1
            while aux.getSig()!=None and i!=p:
                aux=aux.getSig()
                i+=1
            return aux.getDato()
        else:
            print("Posicion no valida")
    
    def buscar(self,elem):
        aux=self.__com
        i=1
        while aux.getSig()!=None and aux.getDato()!=elem:
            aux=aux.getSig()
            i+=1
        if aux.getDato()==elem:
            return i
        else:
            print("elemento no encontrado")
        return aux.getDato()



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


