data Producto = Producto { id :: Int, name :: String, precio :: Float } deriving Show

data PedidoUnitario = PedidoUnitario { producto :: Producto, cantidad :: Int } deriving Show

data Pedido = Pedido { pedidos :: [PedidoUnitario] } deriving Show

(+:) :: Pedido -> PedidoUnitario -> Pedido
(+:) (Pedido ps) p = Pedido (p:ps)

instance Show Producto where
  show (Producto id name precio) = "Producto { id = " ++ show id ++ ", name = " ++ name ++ ", precio = " ++ show precio ++ " }"

instance Show PedidoUnitario where
  show (PedidoUnitario producto cantidad) = "PedidoUnitario { producto = " ++ show producto ++ ", cantidad = " ++ show cantidad ++ " }"

instance Show Pedido where
  show (Pedido pedidos) = "Pedido { pedidos = " ++ show pedidos ++ " }"

p1 = Producto 1 "Tijeras" 10.0
p2 = Producto 2 "Alfombra" 20.0

pu1 = PedidoUnitario p1 1
pu2 = PedidoUnitario p2 2

ped = Pedido [] :+: pu1 :+: pu2

print ped -- muestra "Pedido { pedidos = [PedidoUnitario { producto = Producto { id = 1, name = \"Tijeras\", precio = 10.0 }, cantidad = 1 },
-- PedidoUnitario { producto = Producto { id = 2, name = \"Alfombra\", precio = 20.0 }, cantidad = 2 }] }"


instance Show Pedido where
    show (PedidoConProducto producto cantidad) = "Pedido " ++ show producto ++ "con cantidad" ++ show cantidad
    show (PedidoUnitario producto) = "Pedido Unitario " ++ show producto
    show ((:+) producto) = "Pedido usando el :+" ++ show producto -- así no daría error, pero ns cuándo hacemos este ultimo show

data Compra = Compra [Pedido]
instance Show Compra where
    show :: Compra -> String
    show (Compra []) = ""
    show (Compra (pedido : xs)) = show pedido ++ show (Compra xs)