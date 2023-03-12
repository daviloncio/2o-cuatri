
from PIL import Image


class MundoPlot:
    def __init__(self,mundo,cell_size,color0,color1)->None:
        self.__mundo = mundo
        self.__cell_size=cell_size
        self.__color0=color0
        self.__color1=color1
        
    def plot_estado(self,filename):
        #num_rows, num_cols, estado, filename
        cell_size = self.cell_size
        num_rows = self.__mundo.getrows()
        num_cols=  self.__mundo.getcols()
        estado= self._mundo.estado()
        image = Image.new(mode='RGB', size=(cell_size*num_cols, cell_size*num_rows), color='white')
        
        for i in range(num_rows):
            for j in range(num_cols):
                state = estado[i*num_rows+j]
                color = self.__color0 if state == 0 else self.__color1
                x = j * cell_size
                y = i * cell_size
                for dy in range(cell_size):
                    for dx in range(cell_size):
                        image.putpixel((x+dx, y+dy), color)
        image.save(filename + ".png")
        
    
