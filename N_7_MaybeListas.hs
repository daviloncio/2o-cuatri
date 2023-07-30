module N_7_MaybeListas  where

-- Notación do en listas (son las listas por comprensión)
--    "return 3" devuelve [3]
--    "do" usa "concat" (concat :: [[a]]->[a]) para el resultado final
triangulos :: [(Integer, Integer, Integer)]
triangulos = do c <- [1..10] 
                b <- [1..c] 
                a <- [1..b] 
                if a^2 + b^2 == c^2 
                    then return (a,b,c)
                    else []

-- Notación do en maybes
--    "return 3" devuelve "Just 3"
--    "do" devuelve Nothing cuando algo no es posible 
calculos :: Maybe Integer -> Maybe Integer -> Maybe [Char]
calculos m1 m2 = do x <- m1
                    y <- m2
                    m1 -- _ <- m1        (equivalente)
                    if x<y 
                        then return "caso A"
                        else return "caso B"

main :: IO ()
main = do print triangulos
          print (calculos (Just 1) (Just 2))
          print (calculos (Just 1) Nothing)

{-- RESULTADO DEL PROGRAMA:      
[(3,4,5),(6,8,10)]
Just "caso A"
Nothing
--}
