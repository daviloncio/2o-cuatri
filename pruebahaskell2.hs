


type Ident = Int
type Nombre = String
type Precio = Float
type Cantidad = Float

--EJERCICIO 6

data Producto = Producto Ident Nombre Precio

instance Show Producto where
    show (Producto id nombre precio) = show (id, nombre, precio)

data Pedido = Pedido Producto Cantidad | PedidoUnitario Producto | (:+) Producto Cantidad 

instance Show Pedido where
    show (Pedido producto cantidad) = "Pedido " ++ show producto ++ "con cantidad" ++ show cantidad
    show (PedidoUnitario producto) = "Pedido Unitario " ++ show producto
    show ((:+) Producto Cantidad) = "Pedido usando el :+" ++ show producto ++ "con cantidad" ++ show cantidad -- así no daría error, pero ns cuándo hacemos este ultimo show
instance Eq Pedido where 
    (==) :: Pedido -> Pedido -> Bool
    (==) (Pedido producto1 _)(Pedido producto2 _) = producto1 == producto2
    (==) (PedidoUnitario  producto1)(PedidoUnitario producto2) = producto1 == producto2
    (==) ((:+) producto1 _)((:+) producto2 _) = producto1 == producto2
    (/=) :: Pedido -> Pedido -> Bool
    (/=) (Pedido producto1 _)(Pedido producto2 _) = producto1 == producto2
    (/=) (PedidoUnitario  producto1)(PedidoUnitario producto2) = producto1 == producto2
    (/=) ((:+) producto1 _)((:+) producto2 _) = producto1 == producto2

data Compra = Compra [Pedido]
instance Show Compra where
    show :: Compra -> String
    show (Compra []) = ""
    show (Compra (pedido : xs)) = show pedido ++" , "++ show (Compra xs)


id0 :: Ident ; id0 = 0000 
id1 :: Ident ; id1 = 0001
id2 :: Ident ; id2 = 0002

name0 :: Nombre ; name0 = "aspiradora"
name1 :: Nombre ; name1 = "un yate super guapo"
name2 :: Nombre ; name2 = "batidora"

price0 :: Precio ; price0 = 100 
price1 :: Precio ; price1 = 30000000
price2 :: Precio ; price2 = 250

product0 = Producto 1 "la copa" 2000 
product1 = Producto 2 "yate" 30000000 --yate
order0 = PedidoUnitario product0 
order1 = Pedido product1 2

pur0 = Compra [order0,order1]


--no tiene sentido reescribir las funciones ToString ya que usamos el show.

precioProducto :: Producto -> Float  --son muy sencillas estas dos, no habra que cambiar imagino
precioProducto (Producto id nombre precio) = precio

precioPedido :: Pedido -> Float
precioPedido (Pedido (Producto id nombre precio) cantidad) = precio * cantidad
precioPedido (PedidoUnitario (Producto id nombre precio)) = precio

precioCompra :: Compra -> Float
precioCompra (Compra pedidos)= foldr ((+) . precioPedido) 0 pedidos

fusionaCompras :: Compra -> Compra -> Compra  -- FUNCIONAN AMBAS FUSIONA COMPRAS
fusionaCompras (Compra c1)(Compra c2) = Compra (concat [c1,c2]) --concat es una funcion de orden superior




precioProductoCompra :: Compra -> Producto -> Float --crear una lista por compresion y usar foldr
precioProductoCompra (Compra pedidos)(Producto a b c) = precioCompra (Compra [ (Pedido (Producto id nombre precio) cantidad)  | (Pedido (Producto id nombre precio) cantidad)  <- pedidos, Producto a b c == Producto id nombre precio])+
                                             precioCompra (Compra [ (PedidoUnitario (Producto id nombre precio))  | (PedidoUnitario (Producto id nombre precio))  <- pedidos,Producto a b c == Producto id nombre precio])

                --foldr ((+) . precioCompra) 0 Compra ([(Pedido (Producto id n p) cant) | Producto == prod, (Pedido (Producto id n p) cant) <- pedidos])



