
module P2B_EX2.P2B_EX2 where
-- cambios realizados al codigo dado

cls :: IO ()
cls = putStr "\ESC[2J"

type Pos = (Int,Int)
pos :: Pos
pos = (1, 1)
pos2 :: Pos
pos2 = (2, 2)

width :: Int
width = 6

height :: Int
height = 6

type Board = [Pos]

glider :: Board
--glider = [(1,1),(1,3),(1,4),(1,6),(2,3),(2,4),(3,1),(3,6),(4,1),(4,3),(4,4),(4,6),(6,2),(6,3),(6,4),(6,5)]
glider = [(1,1)]
showcells :: Board -> IO ()
showcells b = putStrLn (unlines [ [if isAlive b (x,y) then 'X' else '_' | x <- [1..width]] | y <- [1..height]])

isAlive :: Board -> Pos -> Bool
isAlive b p = elem p b

isEmpty :: Board -> Pos -> Bool
isEmpty b p = not (isAlive b p)

neighbs :: Pos -> [Pos]
neighbs (x,y) = map wrap [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y),
                          (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]

wrap :: Pos -> Pos
wrap (x,y) = (((x-1) `mod` width) + 1, ((y-1) `mod` height) + 1)

liveneighbs :: Board -> Pos -> Int
liveneighbs b = length . filter (isAlive b) . neighbs

survivors :: Board -> [Pos]
survivors b = [p | p <- b, elem (liveneighbs b p) [2,3]]

births :: Board -> [Pos]
births b = [p | p <- rmdups (concat (map neighbs b)),
                isEmpty b p,
                liveneighbs b p == 3]

rmdups :: Eq a => [a] -> [a]
rmdups []     = []
rmdups (x:xs) = x : rmdups (filter (/= x) xs)


wait :: IO String
wait = getLine

life_evo :: Board -> Pos -> String
life_evo b p = if isAlive b p then "X" else "_"


celulaSumInvBin :: Board -> Pos -> Bool
celulaSumInvBin b p
    | liveNeighbors > deadNeighbors = False
    | liveNeighbors < deadNeighbors = True
    | otherwise = not (isAlive b p)
  where
    liveNeighbors = liveneighbs b p
    deadNeighbors = 8 - liveNeighbors

nextgen :: Board -> Board
nextgen b = [p | p <- rmdups (concat (map neighbs b)), celulaSumInvBin b p]


life_changes :: Board -> IO ()
life_changes b = do
  let numChanges = sum $ zipWith (\p1 p2 -> if p1 == p2 then 0 else 1) b (nextgen b)
  putStrLn $ "Número de cambios : " ++ show numChanges


life :: Board -> Int -> IO ()
life _ 0 = return ()
life b n = do
    let center = (div width 2, div height 2)
        corners = [(1,1), (1,height), (width,1), (width,height)]
        posiciones = center:corners  -- creamos una lista con las posiciones relevantes que luego seran devueltas
    putStrLn $ "Evolución de posición central y esquinas: " ++ unwords (map (life_evo b) posiciones)
    life_changes b
    wait
    life ((nextgen b)) (n-1)




turns :: Board -> Int -> Bool -> IO ()
turns b 0 _ =  return()
turns b n showTurns = do
    putStrLn ""
    if showTurns
        then do
            putStrLn ("Siguiente turno:")
            showcells b
            putStrLn "----------------------"
        else return ()
    let next = nextgen b
    turns next (n-1) showTurns





