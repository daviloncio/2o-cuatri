-- Para eliminar algunos warnings sobre uso de mónadas:
    {-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
    {-# HLINT ignore "Use >>" #-}
    {-# HLINT ignore "Redundant return" #-}

module N_8_EquivalenciasDo  where
import N_7_MaybeListas ( triangulos, calculos )    

interac :: IO ()
interac = do putStrLn "Inicio"
             putStrLn "Introduce un nombre"
             nombre<-getLine
             putStrLn ("Introducido: " ++ nombre)
             putStrLn "Final"

-- Equivalentes a interac: interac1, interac2, interac3, interac4, interac5
interac1 :: IO () -- usando pseudoasignaciones
interac1 = do _ <- putStrLn "Inicio"
              _ <- putStrLn "Introduce un nombre"
              nombre<-getLine
              _ <- putStrLn ("Introducido: " ++ nombre)
              putStrLn "Final" 
                -- la ultima instrucción no puede ser ni asignación ni pseudoasignación             
interac2 :: IO () -- usando operador (>>=) en lugar de notación "do"
interac2 = putStrLn "Inicio" >>= \ _ -> 
           putStrLn "Introduce un nombre" >>= \ _ -> 
           getLine >>= \ nombre -> 
           putStrLn ("Introducido: " ++ nombre) >>= \ _ ->  
           putStrLn "Final"
interac3 :: IO () -- paréntesis por la derecha para (>>=)
interac3 = putStrLn "Inicio" >>= (\ _ -> 
           putStrLn "Introduce un nombre" >>= ( \ _ -> 
           getLine >>= ( \ nombre -> 
           putStrLn ("Introducido: " ++ nombre) >>= (\ _ ->  
           putStrLn "Final"))))           
interac4 :: IO () -- -- paréntesis por la izquierda para (>>=). Ley monádica de asociatividad.
interac4 = (((putStrLn "Inicio" >>= \ _ -> 
           putStrLn "Introduce un nombre" ) >>= \ _ -> 
           getLine ) >>= \ nombre -> 
           putStrLn ("Introducido: " ++ nombre) ) >>= \ _ ->  
           putStrLn "Final"             
interac5 :: IO () -- -- Ley monádica de "return" como elemento neutro en notación "do".
interac5 = do putStrLn "Inicio"
              putStrLn "Introduce un nombre"
              nombre<-getLine
              putStrLn ("Introducido: " ++ nombre)
              x <- putStrLn "Final"            
              return x

-- equivalente a triangulos
triangulos1 :: [(Integer, Integer, Integer)]
triangulos1 = [1..10] >>= \ c ->
              [1..c]  >>= \ b ->
              [1..b]  >>= \ a ->
              if a^2 + b^2 == c^2 
                then return (a,b,c)
                else []

-- equivalente a calculos
calculos1 :: Maybe Integer -> Maybe Integer -> Maybe [Char]
calculos1 m1 m2 = m1 >>= \ x ->
                  m2 >>= \ y ->
                  m1 >>= \ _ ->
                  if x<y
                    then Just "caso A"
                    else Just "caso B"           

main :: IO ()
main = do interac
          print triangulos
          print (calculos (Just 1) (Just 2))
          print (calculos (Just 1) Nothing)

{-- RESULTADO DEL PROGRAMA:      
Inicio
Introduce un nombre
yo
Introducido: yo
Final
[(3,4,5),(6,8,10)]
Just "caso A"
Nothing
--}
