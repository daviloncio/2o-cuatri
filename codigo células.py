
class Celula:
    def __init__(self,estado) -> None:
        self.__estado=estado
    def revisar_estado_célula(self):
        return self.__estado
    def actualización_célula(self,):#vecinos,estado
        if self.__estado == 0:
            self.__estado = 1
            return self.__estado
        self.__estado = 0
        return self.__estado
        
class CelulaSumInvBinario:
    pass
class CelulaiNversorBinario:
    pass
class Mundo:
    pass

x=Celula(0)
x.actualización_célula()
print(x.revisar_estado_célula())

