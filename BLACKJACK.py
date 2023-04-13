

class baraja_francesa:  #crear clase carta, que tenga la opción de poner en la mesa la carta cubierta o descubierta.
    los_doce=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    valores = [(1,11),2,3,4,5,6,7,8,9,10,10,10,10]
    palos= ['Corazones','Diamantes','Picas','Tréboles']
    
    class Carta:
        
        def __init__(self,doce,palo,oculta) -> None:
            self.__palo = palo
            self.__doce = doce
            self.__valor = baraja_francesa.valores[baraja_francesa.los_doce.index(self.__doce)] 
            self.__oculta = oculta #0 o 1
        def __str__(self) -> str:
            if self.__oculta == 0:
                return '##carta tapada##'
            return f'{self.__valor} de {self.__palo}'

    def __init__(self,num_barajas) -> None:
        
#{'Corazones':chr(3), 'Diamantes':chr(4), 'Picas':chr(6), 'Treboles': chr(5)}
        
        self.__baraja = []
        for palo in baraja_francesa.palos:
            for num in baraja_francesa.los_doce:
                
                self.__baraja.append(num+' '+palo)
        for i in range(num_barajas-1):
            self.__baraja += self.__baraja
            
    @property
    def baraja(self):
        return self.__baraja
    def __str__(self) -> str:
        return str(self.__baraja)
una_baraja = baraja_francesa(1)
x = una_baraja.baraja#object not callable
print(una_baraja)


                
                