class Mundo:
    pass
class Celula:
    def __init__(self,estado) -> None:
        self.estado=estado
    def revisar_estado_celula(self):
        return self.estado
    @property  #porque self.estado es privado 
    def actualización_celula(self,vecinos):
        if self.estado == 1:
            self.estado = 0
            return self.estado
        self.estado = 1
        return self.estado  
        
        
class CelulaInvBin(Celula):
    def __init__(self,estado) -> None:
        self.estado=estado
    def actualización_celula(self):
        super().actualización_celula()

class CelulaSumInvBin(Celula):
    def __init__(self,estado) -> None:
        self.estado=estado
    def actualización_celula(self, vecinos):
        pass
