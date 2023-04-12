type Ident = Int
type Nombre = String
type Precio = Float

type Cantidad = Float

--type Producto = (Ident, Nombre, Precio)
--type Pedido = (Producto, Cantidad)

--type Compra = [Pedido]
--EJERCICIO 6

data Producto = Producto Ident Nombre Precio

instance Show Producto where
    show (Producto id nombre precio) = show (id, nombre, precio)

data Pedido = Pedido Producto Cantidad | PedidoUnitario Producto | (:+) Producto

instance Show Pedido where
    show (Pedido producto cantidad) = 
        if cantidad == 1
        then "PedidoUnitario " ++ show producto
        else "Pedido " ++ show producto ++ " " ++ show cantidad

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
product2 :: Producto ; product2 = (id2,name2,price2)

qty0 :: Cantidad ; qty0 = 4 
qty1 :: Cantidad ; qty1 = 1
qty2 :: Cantidad ; qty2 = 1


order0 :: Pedido ; order0 = (product0,qty0)  
order1 :: Pedido ; order1 = (product1,qty1)
order2 :: Pedido ; order2 = (product2,qty2)

pur0 :: Compra ; pur0 = [order0] 
pur1 :: Compra ; pur1 = [order1]
pur2 :: Compra ; pur2 = [order1,order2]  --pedidos de batidora y yate en misma compra
