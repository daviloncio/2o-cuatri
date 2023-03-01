import numpy as np

#mundo plot debe encapsular la lógica de impresión 
        
            
    
            
            
            
    
class Celula:
    def __init__(self,estado:int,coord:tuple) -> None:
        self.estado=estado
        self.__i=coord[0]
        self.__j=coord[1]
    def devolver_coordenadas(self):
        return self.__i,self.__j
    def revisar_estado_celula(self):
        return self.estado #porque self.estado es privado 
    def actualización_celula(self):
        if self.estado == 1:
            self.estado = 0
            return self.estado
        self.estado = 1
        return self.estado  
        
        
class CelulaInvBin(Celula):

    def actualización_celula(self):
        super().actualización_celula()

class CelulaSumInvBin(Celula):

    def actualización_celula(self,mapa_actual):
        def comprobación(i,j):
            pass
                
        recorrer_i=self.__i-1
        
class Mundo:
    def __init__(self,m,n,estado_inicial) -> None:
        
        self.__m=m
        self.__n=n
        self.__estado_inicial=estado_inicial
        
        if m*n < len(self.__estado_inicial):
            
            return KeyError('no hay elementos suficientes en la lista del estado inicial para poder asignar a cada célula del mundo uno de ellos')
        
        #self.matriz_celulas=np.array(self.__m)
        l=[]
        for i in range(self.__m):
            l.append([])
            for e in range(self.__n):
                l[i].append(CelulaSumInvBin(self.__estado_inicial.pop(0),(i,e)))
   
        self.__matriz_celulas=np.array(l)
        self.__lista_estados=[]        
    
        for fila in self.__matriz_celulas:
            for element in fila:
                self.__lista_estados.append(element.revisar_estado_celula())
                
    def estado(self):
        return self.__lista_estados
    def actualiza(self):
        
        self.__imagen=[]
        for fila in self.__matriz_celulas:
            for element in fila:
                self.__imagen.append(element.revisar_estado_celula())
        imagenfinal=np.array(self.__imagen)
        self.__mapa=imagenfinal.reshape(self.__m,self.__n)
        
        for fila in self.__matriz_celulas:
            for element in fila:
                pass
                #sacar vecinos de la celula en las coordenadas (fila,element)
                #a la celula con las coordenadas (fila,element) la actualice 
        
mun=Mundo(2,2,[1,0,1,0])
mun.actualiza()


