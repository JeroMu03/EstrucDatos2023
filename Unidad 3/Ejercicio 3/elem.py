class Elem:
    __valor:int
    def __init__(self,valor):
        self.__valor=valor
    
    def __str__(self):
        print("Valor elemen:",self.__valor)