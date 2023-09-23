''' En cada tirada cada jugador dispone de varias opciones.

Pedir carta: el jugador recibe una carta más. Si las cartas suman más de 21 puntos, pierde automáticamente y pasa el turno.

Plantarse: el jugador se queda con las cartas que tiene y pasa el turno al siguiente.

Rendirse: el jugador se puede rendir antes de realizar cualquier otra acción. Esto le permite recuperar la mitad de lo apostado.

Doblar: pueden doblarse las apuestas si se tienen 9, 10 u 11 puntos. 
Si se dobla, el crupier reparte una carta más al jugador y termina el turno.

Lo más importante que debemos saber es que no hay una regla universal que reúna los requisitos para poder doblar en el blackjack.
Cada casino tiene sus propias normas que debemos conocer cuando comenzamos a jugar,
tanto de manera física como online, aunque lo normal es que se permita doblar cuando el jugador tiene 9, 10 u 11 puntos.

Dividir: cuando las 2 primeras cartas valen lo mismo, 
se pueden dividir en 2 jugadas independientes con su propia apuesta para cada una.

Seguro: cuando la carta descubierta por el crupier es un As se puede apostar a que éste tiene blackjack. 
El jugador debe realizar una apuesta adicional de la mitad de lo que ha apostado. Esta jugada se resuelve en el momento. 
En caso de acertar, la banca pagará dicha apuesta 2 a 1; en caso contrario se pierde el seguro y sigue el orden normal de juego.'''

import sys
import random
sys.stdout.reconfigure(encoding='utf-8')

class baraja_francesa:  #crear clase carta, que tenga la opción de poner en la mesa la carta cubierta o descubierta.
    los_doce=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    valores = [(1,11),2,3,4,5,6,7,8,9,10,10,10,10]
    palos= ['\u2665','\u2666','\u2660','\u2663'] #corazon rombo pica trebol

    class Carta:
        
        def __init__(self,doce,palo,oculta=1) -> None:  
            #ese 1 quiere decir que tengo que especificar el cero si quiero sacar una carta tapada
            self.__palo = palo
            self.__doce = doce
            self.__valor = baraja_francesa.valores[baraja_francesa.los_doce.index(self.__doce)] 
            self.__oculta = oculta #0 o 1
        @property
        def valor(self):
            return self.__valor
        def __str__(self) -> str:
            if self.__oculta == 0:
                return '##carta tapada##'
            return f'{self.__doce} {self.__palo}'

    def __init__(self,num_barajas) -> None:
        self.__baraja = []
        for palo in baraja_francesa.palos:
            for num in baraja_francesa.los_doce:
                
                self.__baraja.append(self.Carta(num,palo))
        for i in range(num_barajas-1):
            self.__baraja += self.__baraja
            
    @property
    def baraja(self):
        return self.__baraja
    def __str__(self) -> str:
        return str(self.__baraja)
    
    
    
monton = baraja_francesa(1)  
#Para jugar Black Jack se utilizan 6 barajas de 52 cartas cada una, tres de un color y tres de otro,
# o bien barajas de un mismo color, siempre y cuando se alternen los colores de mesa en mesa.

def ace_en_mesa_o_no(contador,valor):
    if type(valor)==tuple:
        for i in range(len(contador)-1):
            contador[i]+=1
        for i in range(len(contador)-1):
            if contador[i]+10<=21:
                contador.append(contador[i]+10)   
    else:
        for i in range(len(contador)-1):
            contador[i]+=valor
def combi_menor_que_21(contador):
    for element in contador:
        if element<21:
            return True
    else:
        return False    #en este caso,todas nuestras combinaciones se han pasado de 21.
def puntos_pa_doblar(contador):
    for element in contador:
        if element in [9,10,11]:
            return True
    return False
    
def main():
        
    input('Bienvenido al Blackjack de Daviloncio,seré el dealer en esta partida, empezamos cuando le des al enter\n')
    #print('   Pass:0    Hit:1    Double:2   Surrender:3    ')
    
    x = monton.baraja;random.shuffle(x)
    
    contador=[0];mis_cartas=[]
    
    input('te paso dos cartas\n')
    
    c1=x.pop() ; c2=x.pop()
    
    valor1=c1.valor ; valor2=c2.valor   #ojo con los valores cuanbdo tenemos una A
    mis_cartas.extend([c1,c2])
    
    ace_en_mesa_o_no(contador,valor1) ; ace_en_mesa_o_no(contador,valor2)
    
    if valor1==valor2: key_split=True
    else: key_split=False
    
    if puntos_pa_doblar(contador): key_double=True 
    else: key_double=False
    
    while combi_menor_que_21(contador):
        if key_split and key_double:
            x=input('qué quieres hacer? Puedes plantarte(0)\n, pedir carta(1)\n,doblar(2)\n,rendirte(3)\n,dividir(4)\n o asegurar(5)\n')
        elif key_split:
            x=input('qué quieres hacer? Puedes plantarte(0)\n,pedir carta(1)\n,rendirte(3)\n,dividir(4)\n o asegurar(5)\n')
        elif key_double:
            x=input('qué quieres hacer? Puedes plantarte(0)\n, pedir carta(1)\n,doblar(2)\n,rendirte(3)\n o asegurar(5)\n')
        else:
            x=input('qué quieres hacer? Puedes plantarte(0)\n, pedir carta(1)\n,rendirte(3)\n o asegurar(5)\n')
            
        if x=='0': break
        elif x=='1': 
        
main()
    
    


                
                