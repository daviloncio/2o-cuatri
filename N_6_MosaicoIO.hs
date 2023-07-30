module N_6_MosaicoIO  where
import N_2_Mosaico
    ( Cuadrado(..),
      mosaicoInicial,
      incluirCuadrados,
      dibujarMosaico,
      mostrarSeparador )

introducirCuadrados :: IO [Cuadrado]
introducirCuadrados = introducirCuadrados' []

introducirCuadrados' :: [Cuadrado] -> IO [Cuadrado]
introducirCuadrados' cuadrados =
        do putStrLn "Introduce un cuadrado"
           cuadrado<-getLine
           let cuadradosNuevos=read cuadrado : cuadrados
           putStrLn "Pulsa s para introducir otro cuadrado"
           teclado<-getLine
           if teclado=="s" 
                 then introducirCuadrados' cuadradosNuevos
                 else return cuadradosNuevos

cambiarColores :: [Cuadrado] -> IO [Cuadrado]
cambiarColores cuadrados =
        do putStrLn $ "Cuadrados: " ++ show cuadrados
           putStrLn "Introduce el color para reemplazar"
           color<-getLine
           putStrLn "Introduce el color nuevo"
           colorNuevo<-getLine
           let cuadradosNuevos = 
                map (cambiar (head color) (head colorNuevo)) 
                    cuadrados
           putStrLn "Pulsa s para cambiar otro color"
           teclado<-getLine
           if teclado=="s" 
                then cambiarColores cuadradosNuevos
                else return cuadradosNuevos
     where cambiar color colorNuevo (Cuad borX borY a c) =
                if color==c then Cuad borX borY a colorNuevo
                            else Cuad borX borY a c

main :: IO ()
main = do dibujarMosaico mosaicoInicial
          cuadrados<-introducirCuadrados
          mostrarSeparador
          dibujarMosaico $ incluirCuadrados mosaicoInicial cuadrados
          cuadrados' <- cambiarColores cuadrados
          mostrarSeparador
          dibujarMosaico $ incluirCuadrados mosaicoInicial cuadrados'

{-- RESULTADO DEL PROGRAMA:      
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
Introduce un cuadrado
Cuad 2 3 2 'a'
Pulsa s para introducir otro cuadrado
s
Introduce un cuadrado
Cuad 1 5 2 'b'
Pulsa s para introducir otro cuadrado
s
Introduce un cuadrado
Cuad 4 2 3 'c'
Pulsa s para introducir otro cuadrado
n
--------------------
....bb....
..aabb....
..aa......
.ccc......
.ccc......
.ccc......
..........
..........
..........
..........
Cuadrados: [Cuad 4 2 3 'c',Cuad 1 5 2 'b',Cuad 2 3 2 'a']
Introduce el color para reemplazar
a
Introduce el color nuevo
m
Pulsa s para cambiar otro color
s
Cuadrados: [Cuad 4 2 3 'c',Cuad 1 5 2 'b',Cuad 2 3 2 'm']
Introduce el color para reemplazar
c
Introduce el color nuevo
n
Pulsa s para cambiar otro color
n
--------------------
....bb....
..mmbb....
..mm......
.nnn......
.nnn......
.nnn......
..........
..........
..........
..........
--}