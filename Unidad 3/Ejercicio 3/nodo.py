from elem import Elem
class Nodo:
    __elem: Elem
    __sig:object
    def __init__(self,elem):
        self.__elem=elem
        self.__sig=None
    def setSig(self,siguiente):
        self.__sig=siguiente
    def getSig(self):
        return self.__sig
    def getDato(self):
        return self.__elem
    