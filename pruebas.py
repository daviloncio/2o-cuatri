class Prueba:
    def __init__(self,hola) -> None:
        self._hola=hola
g=Prueba('heeey')
g._hola = 'hola'
print(g._hola)