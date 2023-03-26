
factorial :: Int -> Int

factorial 0 = 1
factorial n = n * factorial(n-1)

--EJ1:

type Ident = Int
type Nombre = String
type Precio = Float

type Cantidad = Int

type Producto = (Ident, Nombre, Precio)
type Pedido = (Producto, Cantidad)

type Compra = [Pedido]

id0 :: Ident ; id0 = 0001

name0 :: Nombre ; name0 = "aspiradora"

price0 :: Precio ; price0 = 100

product0 :: Producto; product0 = (id0,name0,price0)

qty0 :: Cantidad ; qty0 = 4

order0 :: Producto; order0 = (product0,qty0)

pur0 :: Compra ; pur0 = [order0]

 

--EJ 2:

productoToString :: Producto -> String
productoToString  (ident,nombre,precio) = "Producto numero" ++ show ident ++ ":" ++ Nombre ++ "de precio" ++ show precio 

--pedidoToString ::  Pedido -> String
--pedidoToString ((id, nombre, precio), cantidad) = "El pedido está formado por " ++ show cantidad ++ " unidad(es) del Producto " ++ show ident ++ ": " ++ nombre ++ " de precio " ++ show precio ++". El precio total es " ++ show (precio * cantidad)



--compraToString :: Compra -> String
--compraToString  [] = ""
--compraToString  (x:xs) = pedidoToString x ++ compraToString xs


precioProducto :: Producto -> Float
precioProducto (ident,nombre,precio) = precio

precioCompra :: Compra -> Float
precioCompra  [] = ""
precioCompra (x:xs) = precioProducto x + precioProducto xs

fusionaCompras :: Compra -> Compra -> Compra
fusionaCompras [] x = x
fusionaCompras x [] = x
fusionaCompras (x:xs) (y:ys) = x : y : fusionaCompras xs ys


--precioProductoCompra :: Compra -> Producto -> Float
--precioProductoCompra [] _ = 0
--precioProductoCompra (((id,_,precio),cant):xs) (a, _, _) = 
  --if id  == a
  --then precio * (+) precioProductoCompra xs (a,"",0)
  --else precioProductoCompra xs (a,"",0)



