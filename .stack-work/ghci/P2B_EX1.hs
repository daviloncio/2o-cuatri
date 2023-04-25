
module P2B_EX1.P2B_EX1 where
-- cambios realizados al codigo dado



cls :: IO ()
cls = putStr "\ESC[2J"

type Pos = (Int,Int)

width :: Int
width = 9

height :: Int
height = 9

type Board = [Pos]

glider :: Board
glider = [(3, 7), (18, 5), (14, 6), (7, 35), (7, 7), (2, 2), (1, 26),(9,16), (7,10)]



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

nextgen :: Board -> Board
nextgen b = survivors b ++ births b

life :: Board -> Int -> IO ()
life _ 0 = return ()
life b n = do 
            showcells b
            wait 
            life ((nextgen b)) (n-1)


wait :: IO String
wait = getLine


main4 :: IO()
main4 = showcells glider 