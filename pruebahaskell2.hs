
{-# LANGUAGE InstanceSigs #-}  


type Ident = Int
type Nombre = String
type Precio = Float
type Cantidad = Float

--EJERCICIO 6

data Producto = Producto Ident Nombre Precio

instance Eq Producto where 
    (==) :: Producto -> Producto -> Bool
    (==) (Producto id1 name1 price1)(Producto id2 name2 price2) = (Producto id1 name1 price1) == (Producto id2 name2 price2)
    (/=) :: Producto -> Producto -> Bool
    (/=)(Producto id1 name1 price1)(Producto id2 name2 price2) = not((id1,name1,price1) == (id2,name2,price2))


 

instance Show Producto where
    show (Producto id nombre precio) = show (id, nombre, precio)




data Pedido = Pedido Producto Cantidad| PedidoUnitario Producto | (:+) Producto Cantidad 

instance Show Pedido where
    show (Pedido producto cantidad) = "Pedido " ++ show producto ++ "con cantidad" ++ show cantidad
    show (PedidoUnitario producto) = "Pedido Unitario " ++ show producto
    show ((:+) producto cantidad) = "Pedido usando el :+" ++ show producto ++ "con cantidad" ++ show cantidad -- así no daría error, pero ns cuándo hacemos este ultimo show
instance Eq Pedido where 
    (==) :: Pedido -> Pedido -> Bool
    (==) (Pedido producto1 _)(Pedido producto2 _) = producto1 == producto2
    (==) (PedidoUnitario producto1)(PedidoUnitario producto2) = producto1 == producto2
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

errorProducto :: Producto -> String -> Maybe Producto
errorProducto _ razon = error razon

errorPedido :: Pedido -> String-> Maybe Pedido
errorPedido _  razon = error razon 






productoS :: Producto -> Maybe Producto
productoS (Pedido  (Producto codigo nombre precio) cantidad) 
  | precio <= 0 = errorPedido (Pedido (Producto codigo nombre precio) cantidad) "el precio del producto no puede ser negativo"
  | nombre == "" = errorPedido (Pedido (Producto codigo nombre precio) cantidad) "el nombre del producto no se ha establecido"


--funcion que usaremos para crear instancias de Pedido
--no hace falta una función de comprobación para crear un pedidoUnitario ya que nos hemos asegurado de que el 
--producto está creado con los datos correctos
pedidoS :: Producto -> Cantidad -> Pedido  
pedidoS (Producto codigo nombre precio) cantidad 
  | cantidad < 0 = errorPedido (Pedido (Producto codigo nombre precio) cantidad) "el pedido no puede tener cantidad negativa"
  | otherwise Pedido (ProductoS codigo nombre precio) cantidad


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
order2 = Pedido (1 "uu" 200) 2

pur0 = Compra [order0,order1,order1]


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




precioProductoCompra :: Compra -> Producto -> Float 
--crear una lista por compresion,creamos dos compras con solo el producto ordenado
--(una con los pedidos y otra con pedidos unitarios) y usar precio compra
precioProductoCompra (Compra pedidos)(Producto a b c) = 
 precioCompra (Compra [ Pedido (Producto id nombre precio) cantidad | (Pedido (Producto id nombre precio) cantidad)  
 <- pedidos, Producto a b c == Producto id nombre precio])+
 precioCompra (Compra [ PedidoUnitario (Producto id nombre precio)  | (PedidoUnitario (Producto id nombre precio))  
 <- pedidos,Producto a b c == Producto id nombre precio])

buscaPedidosConProducto :: Compra -> Producto -> Compra 
buscaPedidosConProducto (Compra pedidos) (Producto a b c) = 
    
    let c1 = Compra [ Pedido (Producto id nombre precio) cantidad | (Pedido (Producto id nombre precio) cantidad)  <- pedidos, Producto a b c == Producto id nombre precio]
        c2 =(Compra [ PedidoUnitario (Producto id nombre precio)  | (PedidoUnitario (Producto id nombre precio))  <- pedidos,Producto a b c == Producto id nombre precio])
    in fusionaCompras c1 c2

buscaPedidosConProductos :: Compra -> [Producto] -> Compra
--usamos la funcion anterior y foldl
buscaPedidosConProductos (Compra pedidos) prods= 
        let c1 = Compra [ PedidoS (Producto id nombre precio) cantidad | (Pedido (Producto id nombre precio) cantidad)  <- pedidos, elem (Producto id nombre precio) prods]
            c2 =(Compra [ PedidoUnitario (Producto id nombre precio)  | (PedidoUnitario (Producto id nombre precio))  <- pedidos,elem (Producto id nombre precio) prods])
        in fusionaCompras c1 c2

eliminaProductoCompra :: Compra -> Producto -> Compra
eliminaProductoCompra (Compra pedidos) prod= 
        let c1 = Compra [ Pedido (Producto id nombre precio) cantidad | (Pedido (Producto id nombre precio) cantidad)  <- pedidos, Producto id nombre precio/=prod]
            c2 =(Compra [ PedidoUnitario (Producto id nombre precio)  | (PedidoUnitario (Producto id nombre precio))  <- pedidos,Producto id nombre precio/=prod])
        in fusionaCompras c1 c2

eliminaCompraCantidad :: Compra -> Cantidad -> Compra
eliminaCompraCantidad(Compra pedidos) cant_max =
        let c1 = Compra [ Pedido (Producto id nombre precio) cantidad | (Pedido (Producto id nombre precio) cantidad)  <- pedidos,cant_max>=cantidad]
            c2 =Compra [ PedidoUnitario (Producto id nombre precio)  | cant_max /= 1,(PedidoUnitario (Producto id nombre precio))  <- pedidos ]
        in fusionaCompras c1 c2

cantidadProducto :: Compra -> Producto -> Float
--lo usamos para la funcion siguiente,y devuelve el numero de repeticiones que tiene un producto en una compra
cantidadProducto (Compra pedidos) (Producto id nombre precio) = (precioProductoCompra (Compra pedidos) (Producto id nombre precio)/precio)
--si dividimos el precio total de un producto en la compra entre el precio de la unidad obtenemos la cantidad del producto presente en la compra.

eliminarRepeticiones :: Compra -> Compra --funcion definida correctamente, por ahora el terminal se queda pillado
eliminarRepeticiones (Compra pedidos) =         
    
    let prods = [Producto id nombre precio | (Pedido (Producto id nombre precio) cantidad)  <- pedidos,  Producto id nombre precio `notElem` prods]++[Producto id nombre precio | PedidoUnitario (Producto id nombre precio)  <- pedidos,  Producto id nombre precio `notElem` prods]
        cantidades_prods = [cantidadProducto (Compra pedidos) un_producto | un_producto <- prods]
        new_pedidos = [Pedido un_producto cant | un_producto <- prods,cant <- cantidades_prods]
    in Compra new_pedidos
