
%logica1confallo->relacion trace y arbol de ejecucion
% Hechos
    carretera(cordoba,granada,200).
    carretera(cordoba,jaen,100).
    carretera(cordoba,malaga,150).
    carretera(cordoba,sevilla,140).
    carretera(sevilla,cadiz,200).
    carretera(sevilla,huelva,100).
    carretera(sevilla,malaga,100).
% Reglas

%redefinimos esta regla para la funcion distancia


distancia2(Origen,Destino,X):-carretera(Origen,Destino,X).

distancia(Origen,Destino,X):-carretera(Origen,Destino,X).
distancia(Origen,Destino,X):-carretera(Destino,Origen,X).
distancia(Origen,Destino,X):-
    carretera(Origen,Intermedio,Y),distancia(Intermedio,Destino,Z),X is Y+Z,
    !.
distancia(Origen,Destino,X):
    carretera(Intermedio,Origen,Y),distancia(Intermedio,Destino,Z),X is Y+Z.

%primero, nos damos cuneta de que para dar con todos los caminos posibles salimos de cordoba y luego de sevilla,después realizaremos
%distancias donde sumamos kilómetros, donde Nonooooooooo siempre sumaremos carretera(sevilla,cordoba,140)

conexiones_cordoba=[carretera(cordoba,granada,200),
                    carretera(cordoba,jaen,100),
                    carretera(cordoba,malaga,150)].
conexiones_sevilla =[carretera(sevilla,cadiz,200),
                    carretera(sevilla,huelva,100),
                    carretera(sevilla,malaga,100)].
conexion_central=carretera(cordoba,sevilla,140).

distancias=findall(Diccionario, 
 (carretera(Ciudad1, Ciudad2, Km),distancia(Ciudad1, Ciudad2, Distancia),
 Diccionario = _{origen:Ciudad1, destino:Ciudad2, distancia:Distancia}),
 ListaDistancias).


main :- print("inicio-carreteras").
     :- print(distancias).


/* Ejemplos de consultas

?- main.
"inicio-carreteras"
true.

?.- carretera(cordoba,sevilla).        
true.

?- carretera(cordoba,huelva). 
false.
Falso en Prolog no equivale a insatisfactible en Lógica

?- conectado(sevilla,cadiz).
true .

?- conectado(cordoba,huelva). 
true .

?- carretera(almeria,almeria).
false.

?- conectado(cordoba,X).        Pulsar ; tras cada solución
X = granada ;
X = jaen ;
X = malaga ;
X = sevilla ;
X = cadiz ;
X = huelva ;
X = malaga ;
false.

?- conectado(cordoba,X).  Pulsar . para no buscar más soluciones
X = granada ;
X = jaen ;
X = malaga .

?- conectado(cordoba,_).   
true .
Como en Haskell (variable anónima/comodín)

?- carretera(malaga,_).
false.

?- conectado(X,X).         
false.
En Haskell no se permiten variables repetidas (debido a currificación)

?- conectado(_,_).
true .

?- conectado(X,Y). 
X = cordoba,
Y = granada ;
X = cordoba,
Y = jaen ;
X = cordoba,
Y = malaga ;
X = cordoba,
Y = sevilla ;
X = sevilla,
Y = cadiz ;
X = sevilla,
Y = huelva ;
X = sevilla,
Y = malaga ;
X = cordoba,
Y = cadiz ;
X = cordoba,
Y = huelva ;
X = cordoba,
Y = malaga ;
false.

*/
