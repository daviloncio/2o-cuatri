
import automata_celular as ac
from PIL import Image


class MundoPlot:
    def __init__(self,mundo:ac.Mundo,cell_size,color0,color1)->None:
        self.__mundo = mundo[0]
        self.__cell_size=cell_size
        self.__color0=color0
        self.__color1=color1
        self.__cols= self.__mundo.getcols()
        self.__rows = self.__mundo.getrows()
        
    def plot_estado(self,filename):
<<<<<<< HEAD
=======
        self.__mundo
>>>>>>> 5772101e44182db987fdc44e83fddc1122df9382

        cell_size = self.__cell_size
        estado = self.__mundo.estado
        image = Image.new(mode='RGB', size=(cell_size*self.__cols, cell_size*self.__rows), color='white')  
        for i in range(self.__rows):
            for j in range(self.__cols):
                state = estado[i*self.__rows+j]
                color = self.__color0 if state == 0 else self.__color1
                x = j * cell_size
                y = i * cell_size
                for dy in range(cell_size):
                    for dx in range(cell_size):
                        image.putpixel((x+dx, y+dy), color)
        image.save(filename + ".png")
<<<<<<< HEAD
    
=======

        
>>>>>>> 5772101e44182db987fdc44e83fddc1122df9382
