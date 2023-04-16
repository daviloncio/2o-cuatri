

type Ident = Int
type Nombre = String
type Precio = Float
type Cantidad = Float

--EJERCICIO 6

data Producto = Producto Ident Nombre Precio

instance Show Producto where
    show (Producto id nombre precio) = show (id, nombre, precio)

data Pedido = PedidoConProducto Producto Cantidad | PedidoUnitario Producto | (:+) Producto

instance Show Pedido where
    show (PedidoConProducto producto cantidad) = "Pedido " ++ show producto ++ "con cantidad" ++ show cantidad
    show (PedidoUnitario producto) = "Pedido Unitario " ++ show producto
    show ((:+) producto) = "Pedido usando el :+" ++ show producto -- así no daría error, pero ns cuándo hacemos este ultimo show

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
order1 = PedidoConProducto product1 2

pur0 = Compra [order0,order1]


--no tiene sentido reescribir las funciones ToString ya que usamos el show.

precioProducto :: Producto -> Float  --son muy sencillas estas dos, no habra que cambiar imagino
precioProducto (Producto id nombre precio) = precio

precioPedido :: Pedido -> Float
precioPedido (PedidoConProducto (Producto id nombre precio) cantidad) = precio * cantidad
precioPedido (PedidoUnitario (Producto id nombre precio)) = precio

precioCompra :: Compra -> Float
precioCompra (Compra pedidos)= foldr ((+) . precioPedido) 0 pedidos

fusionaCompras :: Compra -> Compra -> Compra  -- FUNCIONAN AMBAS FUSIONA COMPRAS
fusionaCompras (Compra c1)(Compra c2) = Compra (concat [c1,c2]) --concat es una funcion de orden superior




precioProductoCompra :: Compra -> Producto -> Float --crear una lista por compresion y usar foldr
precioProductoCompra (Compra pedidos) prod = 
    foldr ((+) . precioCompra) 0 Compra ([(PedidoConProducto (Producto id n p) cant) | Producto == prod, (PedidoConProducto (Producto id n p) cant) <- pedidos])
    
