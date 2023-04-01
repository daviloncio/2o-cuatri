class baraja_francesa:

    def __init__(self,num_barajas) -> None:
        numeros=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        palos=["\u2665","\u2666","\u2660","\u2663"]
        self.baraja = []
        for palo in palos:
            for num in numeros:
                print(palo)
                self.baraja.append(num+' '+palo)
        for i in range(num_barajas-1):
            self.baraja += self.baraja
            
    def __str__(self) -> str:
        return str(self.baraja)
uno = baraja_francesa(1)
print(uno)
                
                