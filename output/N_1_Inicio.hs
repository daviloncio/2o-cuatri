module N_1_Inicio where

-----------------------------------------------------------------------
-- Sumar, producto escalar, multiplicar, con varias versiones
-----------------------------------------------------------------------

-- Sumar 2 números, con 3 versiones--------------------------

-- sumar con 2 argumentos patrón
sumar :: Integer -> Integer -> Integer
sumar 1 2 = 3
sumar 1 y = 1+y
sumar x y = x + y

-- sumar con 1 argumento patrón
sumar' :: Integer -> (Integer -> Integer) 
sumar' 3 = (+) 3
sumar' x = (+) x

-- sumar sin argumentos
sumar'' :: Integer -> Integer -> Integer 
sumar'' = (+)  

-- Producto escalar, con 3 versiones---------------------------

-- prodEscalar con 2 argumentos patrón
prodEscalar :: (Integer, Integer) -> (Integer, Integer) -> Integer 
prodEscalar (2,y1) (x2,y2) = 2*x2+y1*y2
prodEscalar v1 v2 = case (v1,v2) of
                        ((x1,7),(x2,y2))-> x1*x2+7*y2
                        ((x1,y1),(9,y2)) -> x1*9+y1*y2
                        ((x1,y1),(x2,y2))-> x1*x2+y1*y2

-- prodEscalar con 1 argumento patrón
prodEscalar' :: (Integer, Integer) -> ((Integer, Integer) -> Integer)
prodEscalar' (2,y1) = prodEscalar (2,y1)
prodEscalar' (x1,y1) = f
        where f (x2,y2) = x1*x2+y1*y2

-- prodEscalar sin argumentos
prodEscalar'' :: (Integer, Integer) -> (Integer, Integer) -> Integer
prodEscalar'' = prodEscalar

-- Multiplicar 4 números, con 5 versiones---------------------------

-- prod con 4 argumentos patrón
prod :: Integer -> Integer -> Integer -> Integer -> Integer
prod 1 x2 2 x4 = 1*x2*2*x4
prod x1 x2 x3 x4 = let v=x1*x2*x3*x4 in
                        if x1<0 then v else flip (-) 0 v
            where flip f x y = f y x 
                  -- "shadowing" de Prelude.flip, con la misma definición
                  -- Pelude.flip predefinido
                  -- https://hackage.haskell.org/package/base-4.14.3.0/docs/GHC-Base.html#v:flip 

-- prod con 3 argumentos patrón
prod' :: Integer -> Integer -> Integer -> (Integer -> Integer)
prod' 1 1 1 = prod 1 1 1 
prod' 2 3 4 = (*) 24
prod' x1 x2 x3
        | x1<0 = f
        | x1>3 = id f
        | otherwise = prod x1 x2 x3
     where f x = x1*x2*x3*x
           id x = x   -- "shadowing" de Prelude.id, con la misma definición
                      -- Pelude.id predefinido
                      -- https://hackage.haskell.org/package/base-4.14.3.0/docs/GHC-Base.html#v:id
prod' x1 x2 x3 = prod x1 x2 x3 -- Esta definicion no se ejecuta nunca

-- prod con 2 argumentos patrón
prod'' :: Integer -> Integer -> (Integer -> Integer -> Integer)
prod'' 1 1 = (*)
prod'' 2 3 = f
        where f x y = 6*x*y
prod'' x1 x2 = f
        where f x3 x4= x1*x2*x3*x4

-- prod con 1 argumentos patrón
prod''' :: Integer -> (Integer -> Integer -> Integer -> Integer)
prod''' x1 = f
        where f = \ x2 x3 x4 -> x1*x2*x3*x4 -- función anónima (lambda)

-- prod sin argumentos
prod'''' :: Integer -> (Integer -> Integer -> Integer -> Integer)
prod'''' = \ x1  x2 x3 x4 -> x1*x2*x3*x4 -- función anónima (lambda)

-- Funciones de comprobación------------------------------

-- comprobar si sumar, sumar' y sumar'' son equivalentes
comprobarSumar:: (Integer,Integer)->Bool
comprobarSumar (x1,x2) = 
        sumar x1 x2 == sumar' x1 x2 && 
        sumar' x1 x2 == sumar'' x1 x2

-- comprobar si prodEscalar, prodEscalar' y prodEscalar'' son equivalentes
comprobarProdEscalar :: ((Integer, Integer),(Integer, Integer)) -> Bool
comprobarProdEscalar (v1,v2) = 
        prodEscalar v1 v2 == prodEscalar' v1 v2 && 
        prodEscalar' v1 v2 == prodEscalar'' v1 v2

-- comprobar si prod, prod', prod'' y prod'''son equivalentes
comprobarProd :: (Integer, Integer, Integer, Integer) -> Bool
comprobarProd (x1,x2,x3,x4) =
        prod x1 x2 x3 x4 == prod' x1 x2 x3 x4 &&
        prod' x1 x2 x3 x4 == prod'' x1 x2 x3 x4 &&
        prod'' x1 x2 x3 x4 == prod''' x1 x2 x3 x4 &&
        prod''' x1 x2 x3 x4 == prod'''' x1 x2 x3 x4

-- Función de orden superior de cuantificación universal "para todo"
-- Prelude.all es la definición nativa
paraTodo :: (t -> Bool) -> [t] -> Bool
paraTodo _ [] = True
paraTodo p (x:xs) | not(p x) = False
                  | otherwise = paraTodo p xs

-- ejecución de comprobarSumar para varios casos
comp :: [((Integer, Integer), Bool)]
comp=[((x,y),comprobarSumar (x,y)) 
                | x<-[1..10], 
                  y<-[1..x], 
                  mod x y == 0]
-- ejecución usando "paraTodo" de comprobarSumar para varios casos
comp' :: Bool
comp' = paraTodo comprobarSumar valores
    where valores = [(x,y) | x<-[1..10], 
                             y<-[1..x]]

-- ejecución de comprobarProdEscalar para varios casos
comp'' :: Bool
comp'' = paraTodo comprobarProdEscalar valores
    where valores = [((x,y),(y,x)) | x<-[1..10], 
                                     y<-[1..x]]

-- ejecución usando "all" de comprobarProd 
comp''' :: Bool
comp'''= all comprobarProd valores -- función para todo nativa
    where valores = [(x,x+1,x+2,x+3) | x<-[1..10]] 

------------------------------------------------------
-- Geometría
------------------------------------------------------    

type Vector = (Double, Double) -- tipo sinónimo
v1, v2 :: Vector
v1 = (1,2)
v2 = (3,4)
vectores :: [Vector]
vectores = [v1,v2]
modulo :: Vector -> Double
modulo (x, y) = sqrt(x^2+y^2) -- el argumento es patrón

modulos :: [Double]
modulos = mimap modulo vectores

-- Función que aplica una función a una lista
-- Los argumentos son patrones
-- En Haskell no hay bucles, solo recursión
mimap :: (t -> a) -> [t] -> [a] 
mimap f [] = [] 
mimap f (x:xs) = f x : mimap f xs

data Vector' = V' Double Double -- tipo algebraico
v1', v2' :: Vector'
v1' = V' 1 2
v2' = V' 3 4

vectores' :: [Vector']
vectores' = [v1',v2']

modulo' :: Vector' -> Double
modulo' (V' x y) = sqrt(x^2+y^2) -- el argumento es patrón

modulos' :: [Double]
modulos' = map modulo' vectores' 
-- Pelude.map predefinido
-- https://hackage.haskell.org/package/base-4.14.3.0/docs/GHC-Base.html#v:map

data Vector'' a = V'' a a -- tipo algebraico polimórfico
v1'' :: Vector'' Double
v1'' = V'' 1 2
v2'' :: Vector'' Double
v2'' = V'' 3 4

------------------------------------------------------
-- LISTAS POR COMPRENSIÓN
------------------------------------------------------   

-- Ordenación de números (recursivamente)
ordenar :: [Integer] -> [Integer]
ordenar [] = [] 
ordenar (x:xs) = ordenar  [ y | y <- xs, y <= x ] 
                 ++ [x] 
                 ++  ordenar  [ z | z <- xs, z  > x ]
ordenar' :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
ordenar' numeros = undefined  -- undefined :: a
        -- Útil para dejar algo pendiente
        -- Semejante a "pass" de Python

-- [((3,4,5),12),((6,8,10),24)]
triangulos :: [((Integer, Integer, Integer), Integer)]
triangulos = [((a,b,c),suma2) |
                  c <- [1..10], 
                  b <- [1..c], 
                  let suma1=b+c,  
                  a <- [1..b], 
                  let suma2=suma1+a, 
                  a^2 + b^2 == c^2] 

------------------------------------------------------
-- Ejecución de main. Notación "do" en tipo IO
------------------------------------------------------    

main :: IO ()
main = do putStrLn "Como te llamas?"
          nombre <- getLine -- leer de teclado
          putStrLn ("Hola " ++ nombre ++ ". Comencemos ...")
          putStrLn ("Comprobacion 0: " 
                     ++ show (let p (_,b)= b in all p comp)) -- True
          putStrLn ("Comprobacion 1: " ++ show comp') -- True           
          putStrLn ("Comprobacion 2: " ++ show comp'') -- True           
          putStrLn ("Comprobacion 3: " ++ show comp''') -- True                      
          putStrLn ("Ordenacion de numeros: "  
                    ++ show (ordenar [4,5,1,7,0])) -- [0,1,4,5,7]
          putStrLn "Calculo de modulos"
          print modulos -- [2.23606797749979,5.0]
          print modulos' -- [2.23606797749979,5.0]         
          print triangulos -- [((3,4,5),12),((6,8,10),24)]
          print triangulos' -- [((3,4,5),12),((6,8,10),24)]

------------------------------------------------------
-- Notación "do" en listas por compresión
------------------------------------------------------
-- La notación "do" se puede aplicar también sobre listas por comprensión
-- Veremos más adelante la razón: el tipo IO y el tipo lista son mónadas
-- triangulos y triangulos' son equivalentes
triangulos' :: [((Integer, Integer, Integer), Integer)]
triangulos' = do c <- [1..10] 
                 b <- [1..c] 
                 let suma1=b+c  
                 a <- [1..b] 
                 let suma2=suma1+a 
                 if a^2 + b^2 == c^2 
                        then [((a,b,c),suma2)]
                        else []
---------------------------------------------------------                 

{-- RESULTADO DEL PROGRAMA:      
Como te llamas?
yo
Hola yo. Comencemos ...
Comprobacion 0: True
Comprobacion 1: True
Comprobacion 2: True
Comprobacion 3: True
Ordenacion de numeros: [0,1,4,5,7]
Calculo de modulos
[2.23606797749979,5.0]
[2.23606797749979,5.0]
[((3,4,5),12),((6,8,10),24)]
[((3,4,5),12),((6,8,10),24)]
--}