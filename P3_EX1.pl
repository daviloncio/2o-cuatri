%logica1confallo->relacion trace y arbol de ejecucion
% Hechos
    carretera(cordoba,granada).
    carretera(cordoba,jaen).
    carretera(cordoba,malaga).
    carretera(cordoba,sevilla).
    carretera(sevilla,cadiz).
    carretera(sevilla,huelva).
    carretera(sevilla,malaga).
% Reglas
    conectado(Origen,Destino):- carretera(Origen, Destino).
    conectado(Origen,Destino):- carretera(Destino,Origen).
    conectado(Origen,Destino):-  % definición con recursividad
        carretera(Origen,Intermedio), conectado(Intermedio,Destino).
    conectado(Origen,Destino):-  % definición con recursividad
        carretera(Destino,Intermedio), conectado(Intermedio,Origen).


main :- print("inicio-carreteras").
     :- print("iyww").
     :- conectado(sevilla,cordoba).
     :- conectado(sevilla,granada).


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
