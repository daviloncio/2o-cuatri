
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
    show (PedidoConProducto producto cantidad) = "Pedido " ++ show producto ++ " " ++ show cantidad
    show (PedidoUnitario producto) = "Pedido Unitario " ++ show producto
    show ((:+) producto) = "Pedido " ++ show producto -- tengo dudas, hay que revisarla

data Compra = Compra [Pedido]
instance Show Compra where
    show :: Compra -> String
    show (Compra []) = "La compra está formada"
    show (Compra (pedido : xs)) = show pedido ++ show (Compra xs)

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
product1 = (id1,name1,price1)




productoToString :: Producto -> String
productoToString = show

pedidoToString ::  Pedido -> String
pedidoToString = show

--compraToString :: Compra -> String  --usar foldr
--compraToString compra="Esta compra está formada por los siguientes pedidos"
                      --map(pedidoToString compra)


--precioProducto :: Producto -> Float  --son muy sencillas estas dos, no habra que cambiar imagino
--precioProducto (ident,nombre,precio) = precio

--precioPedido :: Pedido -> Float
--precioPedido ((ident,nombre,precio),cantidad) = precio * cantidad

--precioCompra :: Compra -> Float
--precioCompra  = foldr (\((ident,nombre,precio),cant) -> cant + acc) 0

