print('\u2660')

class baraja_francesa:

    def __init__(self,num_barajas) -> None:
        numeros=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#{'Corazones':chr(3), 'Diamantes':chr(4), 'Picas':chr(6), 'Treboles': chr(5)}
        palos= ['\x03','\x06','\x05','\x04']
        self.baraja = []
        for palo in palos:
            for num in numeros:
                
                self.baraja.append(num+' '+palo)
        for i in range(num_barajas-1):
            self.baraja += self.baraja
            
    def __str__(self) -> str:
        return str(self.baraja)
uno = baraja_francesa(1)

                
                