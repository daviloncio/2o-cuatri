module N_5_InicioIO where

io1 :: IO String
io1 = do putStrLn "Introduce un nombre"
         let nombreInicial="pepe" 
         nombre<-getLine 
         return 3 -- Distinto a return de Python
         putStrLn ("Nombre introducido: " ++ nombre)
         putStrLn ("Nombre inicial: " ++ nombreInicial)
         return nombre

io2 :: IO String -- io1 e io2 producen el mismo resultado
io2 = do () <- putStrLn "Introduce un nombre" 
            -- pseudoasignación a un patrón
         let nombreInicial ="pepe" 
         nombre <-getLine
         numero <- return 3
         _ <- putStrLn ("Nombre introducido: " ++ nombre)
         putStrLn ("Nombre inicial: " ++ nombreInicial)
         return nombre

-- Una función pura no puede llamar a una impura (ej: print)
-- Al contrario sí es posible
doble :: Integer->Integer
-- doble 3 = print (2*3) -- error
doble 3 = 2*3
doble x = 2*x

main :: IO ()
main = do putStrLn "Comprobacion de io1 e io2"
          nom1 <- io1
          nom2 <- io2
          putStrLn 
            $ "Has introducido los nombres: " ++ show (nom1, nom2)
          if length nom1 < length nom2 
            then do putStrLn "El primer nombre es menor" 
                    putStrLn "Operacion main finalizada"  
            else do putStrLn "El primer nombre no es menor" 
                    putStrLn "Operacion main finalizada"         

{-- RESULTADO DEL PROGRAMA:      
Comprobacion de io1 e io2
Introduce un nombre
juan
Nombre introducido: juan
Nombre inicial: pepe
Introduce un nombre
maria
Nombre introducido: maria
Nombre inicial: pepe
Has introducido los nombres: ("juan","maria")
El primer nombre es menor
Operacion main finalizada
--}         