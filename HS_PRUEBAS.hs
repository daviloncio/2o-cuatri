--Función recursiva invertir que, a partir de una lista de booleanos, crea otra
--lista de booleanos cambiando True por False y False por True.

invertir::[Bool]->[Bool]
invertir []=[]
invertir (element:xs) =
    if element==True then
        False : invertir xs
    else 
        True : invertir xs

--Función recursiva polimórfica sumar que suma una lista de números. 
suma::[Integer]->Integer
suma [] = 0
suma (numero:xs)= numero + suma xs
--Función recursiva polimórfica contar que, a partir de una lista de booleanos,
--cuenta las apariciones del valor True.
contar::[Bool]->Integer
contar []=0
contar (element:xs) =
    if element==True then
        1 + contar xs
    else 
        0 + contar xs

--Función contar’, equivalente a la función contar, pero usando una lista por
--comprensión.

contar2::[]Bool->Integer
contar2 lista=
    let list_unos=[1 | element <- lista, element==True]
    in suma list_unos

f :: Integer->Integer->Integer
f x y = x + y

-- Función sin currificar
suma1 :: Int -> Int -> Int
suma1 x y = x + y

-- Función currificada
sumaCurrificada :: Int -> (Int -> Int)
sumaCurrificada x y = x + y

suma_error :: Int -> Int
suma_error x = suma1 x 2

suma_ezito:: Int->Int
suma_ezito x = sumaCurrificada x 3

esMayorCurrificada :: Int -> (Int -> Bool)
esMayorCurrificada x y = x > y

esMayorA10 :: Int -> Bool
esMayorA10 = esMayorCurrificada 10

impares:: Int -> Int -> [Int]
impares x y = [a | a<-[1..],a `mod` 2 == 1,a>=x,a<=y]


