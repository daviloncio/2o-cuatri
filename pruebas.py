class Papa:
    def __init__(self,años,hijos) -> None:
        self.__hijos=hijos
        self.__años=años
    def saberedad(self):
        return self.__años
juanje=Papa(53,2)
print(juanje.saberedad())