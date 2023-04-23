
module P1A_EX1.P1A_EX1 where

--EJ1:

type Ident = Int
type Nombre = String
type Precio = Float

type Cantidad = Float

type Producto = (Ident, Nombre, Precio)
type Pedido = (Producto, Cantidad)

type Compra = [Pedido]

id0 :: Ident ; id0 = 0000
id1 :: Ident ; id1 = 0001
id2 :: Ident ; id2 = 0002

name0 :: Nombre ; name0 = "aspiradora"
name1 :: Nombre ; name1 = "un yate super guapo"
name2 :: Nombre ; name2 = "batidora"

price0 :: Precio ; price0 = 100
price1 :: Precio ; price1 = 30000000
price2 :: Precio ; price2 = 250

product0 :: Producto ; product0 = (id0,name0,price0)
product1 :: Producto ; product1 = (id1,name1,price1)
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


--EJ 2:

productoToString :: Producto -> String
productoToString  (ident,nombre,precio) = "Producto numero " ++ show ident ++ ": " ++ nombre ++ " de precio " ++ show precio

pedidoToString ::  Pedido -> String
pedidoToString ((id, nombre, precio), cantidad) = "El pedido esta formado por " ++ show cantidad ++ " unidad(es) del Producto " ++ show id ++ ": " ++ nombre ++ " de precio " ++ show precio ++". El precio total es " ++ show (precio * cantidad)



compraToString :: Compra -> String
compraToString  [] = ""
compraToString  (x:xs) = pedidoToString x ++ compraToString xs


precioProducto :: Producto -> Float
precioProducto (ident,nombre,precio) = precio

precioPedido :: Pedido -> Float
precioPedido ((ident,nombre,precio),cantidad) = precio * cantidad

precioCompra :: Compra -> Float
precioCompra [] = 0
precioCompra (x:xs) = precioPedido x + precioCompra xs
--(precioProducto(x !! 0) * x !! 1 ) + precioCompra xs

fusionaCompras :: Compra -> Compra -> Compra  -- FUNCIONAN AMBAS FUSIONA COMPRAS
fusionaCompras [] x = x
fusionaCompras x [] = x
fusionaCompras (x:xs) (y:ys) = x : y : fusionaCompras xs ys

fusionaCompras2 :: Compra -> Compra -> Compra
fusionaCompras2 [] ys = ys
fusionaCompras2(x:xs) ys = x : fusionaCompras xs ys


precioProductoCompra :: Compra -> Producto -> Float --crear una lista por compresion y usar foldr
precioProductoCompra [] _ = 0
precioProductoCompra (((id,_,precio),cant):xs) (a,_,_) =
  if id  == a
  then precio * cant + precioProductoCompra xs (a,"", 0)
  else precioProductoCompra xs (a,"",0)

buscaPedidosConProducto :: Compra -> Producto -> [Pedido] --Devolvemos otra compra o lista de pedidos, da igual ya que queremos una lista de pedidos
buscaPedidosConProducto [] _ = []
buscaPedidosConProducto (((id,nombre,precio),cant):xs) (a,nom_prod,prec_prod) =
  if id == a
  then ((id,nombre,precio),cant) : buscaPedidosConProducto xs (a,nombre,precio)
  else buscaPedidosConProducto xs (a,nombre,precio)

buscaPedidosConProductos :: Compra -> [Producto] -> [[Pedido]]
--devuelve una lista con la lista de pedidos que incluyen el producto 1,otra lista con los pedidos del prodcuto 2 etc.
buscaPedidosConProductos compra [] = []
buscaPedidosConProductos compra ((a,nom_prod,prec_prod):xs) =
  buscaPedidosConProducto compra (a,nom_prod,prec_prod) : buscaPedidosConProductos compra xs


eliminaProductoCompra :: Compra -> Producto -> Compra
eliminaProductoCompra [] _ = []
eliminaProductoCompra (((id,name,precio),cant):xs) (a,b,c) =
  if id==a
  then eliminaProductoCompra xs (a,b,c)
  else ((id,name,precio),cant) :eliminaProductoCompra xs (a,b,c)

eliminaCompraCantidad :: Compra -> Cantidad -> Compra
eliminaCompraCantidad [] _ = []
eliminaCompraCantidad (((id,name,precio),cant):xs) cant_max =
  if cant > cant_max
  then eliminaCompraCantidad xs cant_max
  else ((id,name,precio),cant) : eliminaCompraCantidad xs cant_max

main1 :: IO () 
main1 = do
        print("PRUEBAS FUNCIONES PARTE 1:\n")
        print(pedidoToString order0)
        print(compraToString pur0)
        print(productoToString product0)
        print(precioCompra pur2)
        print(fusionaCompras pur0 pur1)
        print(precioProductoCompra pur2 product1)
        print(precioProductoCompra pur0 product0)
        print(buscaPedidosConProducto pur2 product1)
        print(buscaPedidosConProductos pur2 [product1,product2])
        print(eliminaProductoCompra pur2 product1)
        print(eliminaCompraCantidad pur0 3)
        print("FIN")

