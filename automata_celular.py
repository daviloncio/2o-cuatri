import numpy as np

#mundo plot debe encapsular la lógica de impresión  (parte2)
        
            
    
            

class Celula:
    def __init__(self,estado:int,coord:tuple) -> None:
        
        self._estado=estado
        self._i=coord[0]
        self._j=coord[1]
        
    def devolver_coordenadas(self):
        
        return self._i,self._j
    
    def revisar_estado_celula(self):
        
        return self._estado #porque self.estado es privado 
    
    def actualización_celula(self,i):  
        if i == 0:
            self._estado = 0
        elif i == 1:
            self._estado = 1
        elif i == "i":
            if self._estado== 1:
                self._estado = 0
            else:
                self._estado = 1
        return self._estado  
        
        
class CelulaInvBin(Celula):
    def __init__(self, estado: int, coord: tuple) -> None:
        super().__init__(estado, coord)

    def actualización_celula(self,mapa): 
        #en esta clase el mapa no lo usaremos para nada pero como la clase mundo no va a distinguir qué tipo de célula vamos a actualizar pues simepre recibirá el parámetro de las coordenadas
        super().actualización_celula('i')

class CelulaSumInvBin(Celula):
    def __init__(self, estado: int, coord: tuple) -> None:
        super().__init__(estado, coord)

    def actualización_celula(self,mapa_actual):
        
        x,y=self._i-1,self._j-1
        
        contador_vecinos_0 = 0  
        contador_vecinos_1 = 0 
        
        for e in range(x,x+3):  #si usamos continue, deja todo lo que este haciendo y pasa a la siguiente iteración del bucle
            for r in range(y,y+3):
                
                if (e,r) == (self._i,self._j):
                    continue
                
                if e < 0 or r < 0 :
                    continue
                
                try:

                    estado_vecino = mapa_actual[e][r]

                    if estado_vecino == 0:
                        contador_vecinos_0 += 1
                        
                    elif estado_vecino == 1:

                        contador_vecinos_1 += 1
                except:
                    continue
                       #saltará except solo cuando las coordenadas indicadas en el bucle no coincidan con las coordenadas de ninguna celula del mundo.
        
        if contador_vecinos_0 > contador_vecinos_1:

            super().actualización_celula(1)
            
        elif contador_vecinos_1 > contador_vecinos_0:

            super().actualización_celula(0)
        elif contador_vecinos_0 == contador_vecinos_1:
            
            super().actualización_celula("i")
            
            
class Mundo:
    def __init__(self,m,n,estado_inicial) -> None:
        
        self.__m=m
        self.__n=n
        self.estado=estado_inicial
                
        if m*n < len(self.estado):
            
            return KeyError('no hay elementos suficientes en la lista del estado inicial como para poder asignar a cada célula del mundo uno de ellos')

        l=[]
        for i in range(self.__m):
    
            for e in range(self.__n):
                
                l.append(CelulaSumInvBin(self.estado[i*self.__m+e],(i,e)))  

        self.matriz_celulas=np.array(l) #realmente hay que usarlo?
        self.matriz_celulas=self.matriz_celulas.reshape(self.__m,self.__n)
        
        self.array_estados=[]      
    
        for fila in self.matriz_celulas:  
            
            for element in fila:
                
                self.array_estados.append(element.revisar_estado_celula()) #habra que cambiarlo por cada actualización
                
        self.array_estados = np.array(self.array_estados)        
        self.array_estados = self.array_estados.reshape(self.__m,self.__n)  #asi tenemos coordenadas
        
    def getrows(self):
        return self.__m
    def getcols(self):
        return self.__n
    def estado_(self):
        return self.estado
    def actualiza(self):  
        
        for fila in self.matriz_celulas:
            
            for element in fila:
                    
                    element.actualización_celula(self.array_estados) #clase mundo no sabe qué tipo de celula vamos a actualizar, pòr lo que siempre pasamos el mapa con los estados
                
                 #después de actualizar cada celula, toca actualizar self.array_estados
                
        self.estado = [] #olvidamos la captura anterior una vez actualizada toda célula.
                
        for fila in self.matriz_celulas:  #repetimos codigo del init para actualizar
            
            for element in fila:
                
                self.estado.append(element.revisar_estado_celula()) 
        
        self.array_estados=np.array(self.estado)        
        self.array_estados=self.array_estados.reshape(self.__m,self.__n) 
        
        
mun=Mundo(6,6, [1,0,1,1,0,1,
                    0,0,1,1,0,0,
                    1,0,0,0,0,1,
                    1,0,1,1,0,1,
                    0,0,0,0,0,0,
                    0,1,1,1,1,0])
print(mun.estado_())
mun.actualiza()
print(mun.estado_())


