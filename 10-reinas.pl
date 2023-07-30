/* Problema de las 8 reinas */

tablero([1,_,2,_,3,_,4,_,5,_,6,_,7,_,8,_]).

solucion([]).
solucion([X,Y|ZS]):-
		solucion(ZS),
		member(Y,[1,2,3,4,5,6,7,8]),
		no_ataca([X,Y],ZS).

no_ataca(_,[]).
no_ataca([X,Y],[X1,Y1|ZS]):-
		Y =\= Y1,
		Y1 - Y =\= X1 - X,
		Y1 - Y =\= X - X1,
		no_ataca([X,Y],ZS).

escribir_solucion([]).
escribir_solucion([X, Y | ZS]):-
         write(' Casilla: '), write(X), write(' , '), write(Y),
         nl,
         escribir_solucion(ZS).

escribir_soluciones :- 
	forall((tablero(S), solucion(S)), (escribir_solucion(S), nl)). 

main :- print("reinas"). 

/* Resultado (92 soluciones)

?- escribir_soluciones.
... escribe las 92 soluciones de una vez  ...

?- tablero(S), solucion(S), escribir_solucion(S).  Pulsando ; tras cada solución
 Casilla: 1 , 4
 Casilla: 2 , 2
 Casilla: 3 , 7
 Casilla: 4 , 3
 Casilla: 5 , 6
 Casilla: 6 , 8
 Casilla: 7 , 5
 Casilla: 8 , 1
S = [1, 4, 2, 2, 3, 7, 4, 3, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 2
 Casilla: 3 , 4
 Casilla: 4 , 7
 Casilla: 5 , 3
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 1
S = [1, 5, 2, 2, 3, 4, 4, 7, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 5
 Casilla: 3 , 2
 Casilla: 4 , 8
 Casilla: 5 , 6
 Casilla: 6 , 4
 Casilla: 7 , 7
 Casilla: 8 , 1
S = [1, 3, 2, 5, 3, 2, 4, 8, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 4
 Casilla: 4 , 2
 Casilla: 5 , 8
 Casilla: 6 , 5
 Casilla: 7 , 7
 Casilla: 8 , 1
S = [1, 3, 2, 6, 3, 4, 4, 2, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 7
 Casilla: 3 , 1
 Casilla: 4 , 3
 Casilla: 5 , 8
 Casilla: 6 , 6
 Casilla: 7 , 4
 Casilla: 8 , 2
S = [1, 5, 2, 7, 3, 1, 4, 3, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 3
 Casilla: 5 , 1
 Casilla: 6 , 7
 Casilla: 7 , 5
 Casilla: 8 , 2
S = [1, 4, 2, 6, 3, 8, 4, 3, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 1
 Casilla: 5 , 4
 Casilla: 6 , 7
 Casilla: 7 , 5
 Casilla: 8 , 2
S = [1, 3, 2, 6, 3, 8, 4, 1, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 3
 Casilla: 3 , 8
 Casilla: 4 , 4
 Casilla: 5 , 7
 Casilla: 6 , 1
 Casilla: 7 , 6
 Casilla: 8 , 2
S = [1, 5, 2, 3, 3, 8, 4, 4, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 7
 Casilla: 3 , 4
 Casilla: 4 , 1
 Casilla: 5 , 3
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 2
S = [1, 5, 2, 7, 3, 4, 4, 1, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 1
 Casilla: 3 , 5
 Casilla: 4 , 8
 Casilla: 5 , 6
 Casilla: 6 , 3
 Casilla: 7 , 7
 Casilla: 8 , 2
S = [1, 4, 2, 1, 3, 5, 4, 8, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 4
 Casilla: 4 , 1
 Casilla: 5 , 8
 Casilla: 6 , 5
 Casilla: 7 , 7
 Casilla: 8 , 2
S = [1, 3, 2, 6, 3, 4, 4, 1, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 7
 Casilla: 3 , 5
 Casilla: 4 , 3
 Casilla: 5 , 1
 Casilla: 6 , 6
 Casilla: 7 , 8
 Casilla: 8 , 2
S = [1, 4, 2, 7, 3, 5, 4, 3, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 4
 Casilla: 3 , 2
 Casilla: 4 , 8
 Casilla: 5 , 5
 Casilla: 6 , 7
 Casilla: 7 , 1
 Casilla: 8 , 3
S = [1, 6, 2, 4, 3, 2, 4, 8, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 4
 Casilla: 3 , 7
 Casilla: 4 , 1
 Casilla: 5 , 8
 Casilla: 6 , 2
 Casilla: 7 , 5
 Casilla: 8 , 3
S = [1, 6, 2, 4, 3, 7, 4, 1, 5|...] ;
 Casilla: 1 , 1
 Casilla: 2 , 7
 Casilla: 3 , 4
 Casilla: 4 , 6
 Casilla: 5 , 8
 Casilla: 6 , 2
 Casilla: 7 , 5
 Casilla: 8 , 3
S = [1, 1, 2, 7, 3, 4, 4, 6, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 8
 Casilla: 3 , 2
 Casilla: 4 , 4
 Casilla: 5 , 1
 Casilla: 6 , 7
 Casilla: 7 , 5
 Casilla: 8 , 3
S = [1, 6, 2, 8, 3, 2, 4, 4, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 2
 Casilla: 3 , 7
 Casilla: 4 , 1
 Casilla: 5 , 4
 Casilla: 6 , 8
 Casilla: 7 , 5
 Casilla: 8 , 3
S = [1, 6, 2, 2, 3, 7, 4, 1, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 7
 Casilla: 3 , 1
 Casilla: 4 , 8
 Casilla: 5 , 5
 Casilla: 6 , 2
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 4, 2, 7, 3, 1, 4, 8, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 8
 Casilla: 3 , 4
 Casilla: 4 , 1
 Casilla: 5 , 7
 Casilla: 6 , 2
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 5, 2, 8, 3, 4, 4, 1, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 8
 Casilla: 3 , 1
 Casilla: 4 , 5
 Casilla: 5 , 7
 Casilla: 6 , 2
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 4, 2, 8, 3, 1, 4, 5, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 7
 Casilla: 3 , 5
 Casilla: 4 , 8
 Casilla: 5 , 1
 Casilla: 6 , 4
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 2, 2, 7, 3, 5, 4, 8, 5|...] ;
 Casilla: 1 , 1
 Casilla: 2 , 7
 Casilla: 3 , 5
 Casilla: 4 , 8
 Casilla: 5 , 2
 Casilla: 6 , 4
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 1, 2, 7, 3, 5, 4, 8, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 5
 Casilla: 3 , 7
 Casilla: 4 , 4
 Casilla: 5 , 1
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 2, 2, 5, 3, 7, 4, 4, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 2
 Casilla: 3 , 7
 Casilla: 4 , 5
 Casilla: 5 , 1
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 4, 2, 2, 3, 7, 4, 5, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 7
 Casilla: 3 , 1
 Casilla: 4 , 4
 Casilla: 5 , 2
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 3
S = [1, 5, 2, 7, 3, 1, 4, 4, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 4
 Casilla: 3 , 1
 Casilla: 4 , 5
 Casilla: 5 , 8
 Casilla: 6 , 2
 Casilla: 7 , 7
 Casilla: 8 , 3
S = [1, 6, 2, 4, 3, 1, 4, 5, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 1
 Casilla: 3 , 4
 Casilla: 4 , 6
 Casilla: 5 , 8
 Casilla: 6 , 2
 Casilla: 7 , 7
 Casilla: 8 , 3
S = [1, 5, 2, 1, 3, 4, 4, 6, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 2
 Casilla: 3 , 6
 Casilla: 4 , 1
 Casilla: 5 , 7
 Casilla: 6 , 4
 Casilla: 7 , 8
 Casilla: 8 , 3
S = [1, 5, 2, 2, 3, 6, 4, 1, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 7
 Casilla: 4 , 2
 Casilla: 5 , 8
 Casilla: 6 , 5
 Casilla: 7 , 1
 Casilla: 8 , 4
S = [1, 6, 2, 3, 3, 7, 4, 2, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 7
 Casilla: 3 , 3
 Casilla: 4 , 6
 Casilla: 5 , 8
 Casilla: 6 , 5
 Casilla: 7 , 1
 Casilla: 8 , 4
S = [1, 2, 2, 7, 3, 3, 4, 6, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 6
 Casilla: 5 , 8
 Casilla: 6 , 5
 Casilla: 7 , 2
 Casilla: 8 , 4
S = [1, 7, 2, 3, 3, 1, 4, 6, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 1
 Casilla: 3 , 8
 Casilla: 4 , 6
 Casilla: 5 , 3
 Casilla: 6 , 7
 Casilla: 7 , 2
 Casilla: 8 , 4
S = [1, 5, 2, 1, 3, 8, 4, 6, 5|...] ;
 Casilla: 1 , 1
 Casilla: 2 , 5
 Casilla: 3 , 8
 Casilla: 4 , 6
 Casilla: 5 , 3
 Casilla: 6 , 7
 Casilla: 7 , 2
 Casilla: 8 , 4
S = [1, 1, 2, 5, 3, 8, 4, 6, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 1
 Casilla: 5 , 5
 Casilla: 6 , 7
 Casilla: 7 , 2
 Casilla: 8 , 4
S = [1, 3, 2, 6, 3, 8, 4, 1, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 7
 Casilla: 5 , 5
 Casilla: 6 , 8
 Casilla: 7 , 2
 Casilla: 8 , 4
S = [1, 6, 2, 3, 3, 1, 4, 7, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 5
 Casilla: 3 , 3
 Casilla: 4 , 1
 Casilla: 5 , 6
 Casilla: 6 , 8
 Casilla: 7 , 2
 Casilla: 8 , 4
S = [1, 7, 2, 5, 3, 3, 4, 1, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 3
 Casilla: 3 , 8
 Casilla: 4 , 2
 Casilla: 5 , 5
 Casilla: 6 , 1
 Casilla: 7 , 6
 Casilla: 8 , 4
S = [1, 7, 2, 3, 3, 8, 4, 2, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 7
 Casilla: 5 , 2
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 4
S = [1, 5, 2, 3, 3, 1, 4, 7, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 5
 Casilla: 3 , 7
 Casilla: 4 , 1
 Casilla: 5 , 3
 Casilla: 6 , 8
 Casilla: 7 , 6
 Casilla: 8 , 4
S = [1, 2, 2, 5, 3, 7, 4, 1, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 2
 Casilla: 4 , 5
 Casilla: 5 , 8
 Casilla: 6 , 1
 Casilla: 7 , 7
 Casilla: 8 , 4
S = [1, 3, 2, 6, 3, 2, 4, 5, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 1
 Casilla: 3 , 5
 Casilla: 4 , 2
 Casilla: 5 , 8
 Casilla: 6 , 3
 Casilla: 7 , 7
 Casilla: 8 , 4
S = [1, 6, 2, 1, 3, 5, 4, 2, 5|...] ;
 Casilla: 1 , 8
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 6
 Casilla: 5 , 2
 Casilla: 6 , 5
 Casilla: 7 , 7
 Casilla: 8 , 4
S = [1, 8, 2, 3, 3, 1, 4, 6, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 8
 Casilla: 3 , 6
 Casilla: 4 , 1
 Casilla: 5 , 3
 Casilla: 6 , 5
 Casilla: 7 , 7
 Casilla: 8 , 4
S = [1, 2, 2, 8, 3, 6, 4, 1, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 7
 Casilla: 3 , 2
 Casilla: 4 , 6
 Casilla: 5 , 3
 Casilla: 6 , 1
 Casilla: 7 , 8
 Casilla: 8 , 4
S = [1, 5, 2, 7, 3, 2, 4, 6, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 2
 Casilla: 4 , 7
 Casilla: 5 , 5
 Casilla: 6 , 1
 Casilla: 7 , 8
 Casilla: 8 , 4
S = [1, 3, 2, 6, 3, 2, 4, 7, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 2
 Casilla: 3 , 7
 Casilla: 4 , 1
 Casilla: 5 , 3
 Casilla: 6 , 5
 Casilla: 7 , 8
 Casilla: 8 , 4
S = [1, 6, 2, 2, 3, 7, 4, 1, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 7
 Casilla: 3 , 2
 Casilla: 4 , 8
 Casilla: 5 , 6
 Casilla: 6 , 4
 Casilla: 7 , 1
 Casilla: 8 , 5
S = [1, 3, 2, 7, 3, 2, 4, 8, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 7
 Casilla: 4 , 2
 Casilla: 5 , 4
 Casilla: 6 , 8
 Casilla: 7 , 1
 Casilla: 8 , 5
S = [1, 6, 2, 3, 3, 7, 4, 2, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 2
 Casilla: 3 , 7
 Casilla: 4 , 3
 Casilla: 5 , 6
 Casilla: 6 , 8
 Casilla: 7 , 1
 Casilla: 8 , 5
S = [1, 4, 2, 2, 3, 7, 4, 3, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 1
 Casilla: 3 , 3
 Casilla: 4 , 8
 Casilla: 5 , 6
 Casilla: 6 , 4
 Casilla: 7 , 2
 Casilla: 8 , 5
S = [1, 7, 2, 1, 3, 3, 4, 8, 5|...] ;
 Casilla: 1 , 1
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 3
 Casilla: 5 , 7
 Casilla: 6 , 4
 Casilla: 7 , 2
 Casilla: 8 , 5
S = [1, 1, 2, 6, 3, 8, 4, 3, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 8
 Casilla: 3 , 4
 Casilla: 4 , 7
 Casilla: 5 , 1
 Casilla: 6 , 6
 Casilla: 7 , 2
 Casilla: 8 , 5
S = [1, 3, 2, 8, 3, 4, 4, 7, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 7
 Casilla: 4 , 4
 Casilla: 5 , 1
 Casilla: 6 , 8
 Casilla: 7 , 2
 Casilla: 8 , 5
S = [1, 6, 2, 3, 3, 7, 4, 4, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 4
 Casilla: 3 , 2
 Casilla: 4 , 8
 Casilla: 5 , 6
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 5
S = [1, 7, 2, 4, 3, 2, 4, 8, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 2
 Casilla: 5 , 7
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 5
S = [1, 4, 2, 6, 3, 8, 4, 2, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 6
 Casilla: 3 , 1
 Casilla: 4 , 7
 Casilla: 5 , 4
 Casilla: 6 , 8
 Casilla: 7 , 3
 Casilla: 8 , 5
S = [1, 2, 2, 6, 3, 1, 4, 7, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 4
 Casilla: 3 , 6
 Casilla: 4 , 8
 Casilla: 5 , 3
 Casilla: 6 , 1
 Casilla: 7 , 7
 Casilla: 8 , 5
S = [1, 2, 2, 4, 3, 6, 4, 8, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 2
 Casilla: 5 , 4
 Casilla: 6 , 1
 Casilla: 7 , 7
 Casilla: 8 , 5
S = [1, 3, 2, 6, 3, 8, 4, 2, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 8
 Casilla: 5 , 4
 Casilla: 6 , 2
 Casilla: 7 , 7
 Casilla: 8 , 5
S = [1, 6, 2, 3, 3, 1, 4, 8, 5|...] ;
 Casilla: 1 , 8
 Casilla: 2 , 4
 Casilla: 3 , 1
 Casilla: 4 , 3
 Casilla: 5 , 6
 Casilla: 6 , 2
 Casilla: 7 , 7
 Casilla: 8 , 5
S = [1, 8, 2, 4, 3, 1, 4, 3, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 8
 Casilla: 3 , 1
 Casilla: 4 , 3
 Casilla: 5 , 6
 Casilla: 6 , 2
 Casilla: 7 , 7
 Casilla: 8 , 5
S = [1, 4, 2, 8, 3, 1, 4, 3, 5|...] ;
 Casilla: 1 , 2
 Casilla: 2 , 6
 Casilla: 3 , 8
 Casilla: 4 , 3
 Casilla: 5 , 1
 Casilla: 6 , 4
 Casilla: 7 , 7
 Casilla: 8 , 5
S = [1, 2, 2, 6, 3, 8, 4, 3, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 2
 Casilla: 3 , 6
 Casilla: 4 , 3
 Casilla: 5 , 1
 Casilla: 6 , 4
 Casilla: 7 , 8
 Casilla: 8 , 5
S = [1, 7, 2, 2, 3, 6, 4, 3, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 6
 Casilla: 3 , 2
 Casilla: 4 , 7
 Casilla: 5 , 1
 Casilla: 6 , 4
 Casilla: 7 , 8
 Casilla: 8 , 5
S = [1, 3, 2, 6, 3, 2, 4, 7, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 7
 Casilla: 3 , 3
 Casilla: 4 , 8
 Casilla: 5 , 2
 Casilla: 6 , 5
 Casilla: 7 , 1
 Casilla: 8 , 6
S = [1, 4, 2, 7, 3, 3, 4, 8, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 8
 Casilla: 3 , 5
 Casilla: 4 , 3
 Casilla: 5 , 1
 Casilla: 6 , 7
 Casilla: 7 , 2
 Casilla: 8 , 6
S = [1, 4, 2, 8, 3, 5, 4, 3, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 5
 Casilla: 3 , 8
 Casilla: 4 , 4
 Casilla: 5 , 1
 Casilla: 6 , 7
 Casilla: 7 , 2
 Casilla: 8 , 6
S = [1, 3, 2, 5, 3, 8, 4, 4, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 2
 Casilla: 3 , 8
 Casilla: 4 , 5
 Casilla: 5 , 7
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 4, 2, 2, 3, 8, 4, 5, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 7
 Casilla: 3 , 2
 Casilla: 4 , 4
 Casilla: 5 , 8
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 5, 2, 7, 3, 2, 4, 4, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 4
 Casilla: 3 , 2
 Casilla: 4 , 5
 Casilla: 5 , 8
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 7, 2, 4, 3, 2, 4, 5, 5|...] ;
 Casilla: 1 , 8
 Casilla: 2 , 2
 Casilla: 3 , 4
 Casilla: 4 , 1
 Casilla: 5 , 7
 Casilla: 6 , 5
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 8, 2, 2, 3, 4, 4, 1, 5|...] ;
 Casilla: 1 , 7
 Casilla: 2 , 2
 Casilla: 3 , 4
 Casilla: 4 , 1
 Casilla: 5 , 8
 Casilla: 6 , 5
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 7, 2, 2, 3, 4, 4, 1, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 1
 Casilla: 3 , 8
 Casilla: 4 , 4
 Casilla: 5 , 2
 Casilla: 6 , 7
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 5, 2, 1, 3, 8, 4, 4, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 1
 Casilla: 3 , 5
 Casilla: 4 , 8
 Casilla: 5 , 2
 Casilla: 6 , 7
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 4, 2, 1, 3, 5, 4, 8, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 2
 Casilla: 3 , 8
 Casilla: 4 , 1
 Casilla: 5 , 4
 Casilla: 6 , 7
 Casilla: 7 , 3
 Casilla: 8 , 6
S = [1, 5, 2, 2, 3, 8, 4, 1, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 7
 Casilla: 3 , 2
 Casilla: 4 , 8
 Casilla: 5 , 5
 Casilla: 6 , 1
 Casilla: 7 , 4
 Casilla: 8 , 6
S = [1, 3, 2, 7, 3, 2, 4, 8, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 1
 Casilla: 3 , 7
 Casilla: 4 , 5
 Casilla: 5 , 8
 Casilla: 6 , 2
 Casilla: 7 , 4
 Casilla: 8 , 6
S = [1, 3, 2, 1, 3, 7, 4, 5, 5|...] ;
 Casilla: 1 , 8
 Casilla: 2 , 2
 Casilla: 3 , 5
 Casilla: 4 , 3
 Casilla: 5 , 1
 Casilla: 6 , 7
 Casilla: 7 , 4
 Casilla: 8 , 6
S = [1, 8, 2, 2, 3, 5, 4, 3, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 5
 Casilla: 3 , 2
 Casilla: 4 , 8
 Casilla: 5 , 1
 Casilla: 6 , 7
 Casilla: 7 , 4
 Casilla: 8 , 6
S = [1, 3, 2, 5, 3, 2, 4, 8, 5|...] ;
 Casilla: 1 , 3
 Casilla: 2 , 5
 Casilla: 3 , 7
 Casilla: 4 , 1
 Casilla: 5 , 4
 Casilla: 6 , 2
 Casilla: 7 , 8
 Casilla: 8 , 6
S = [1, 3, 2, 5, 3, 7, 4, 1, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 2
 Casilla: 3 , 4
 Casilla: 4 , 6
 Casilla: 5 , 8
 Casilla: 6 , 3
 Casilla: 7 , 1
 Casilla: 8 , 7
S = [1, 5, 2, 2, 3, 4, 4, 6, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 5
 Casilla: 4 , 8
 Casilla: 5 , 1
 Casilla: 6 , 4
 Casilla: 7 , 2
 Casilla: 8 , 7
S = [1, 6, 2, 3, 3, 5, 4, 8, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 8
 Casilla: 3 , 4
 Casilla: 4 , 1
 Casilla: 5 , 3
 Casilla: 6 , 6
 Casilla: 7 , 2
 Casilla: 8 , 7
S = [1, 5, 2, 8, 3, 4, 4, 1, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 2
 Casilla: 3 , 5
 Casilla: 4 , 8
 Casilla: 5 , 6
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 7
S = [1, 4, 2, 2, 3, 5, 4, 8, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 6
 Casilla: 3 , 1
 Casilla: 4 , 5
 Casilla: 5 , 2
 Casilla: 6 , 8
 Casilla: 7 , 3
 Casilla: 8 , 7
S = [1, 4, 2, 6, 3, 1, 4, 5, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 8
 Casilla: 5 , 5
 Casilla: 6 , 2
 Casilla: 7 , 4
 Casilla: 8 , 7
S = [1, 6, 2, 3, 3, 1, 4, 8, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 3
 Casilla: 3 , 1
 Casilla: 4 , 6
 Casilla: 5 , 8
 Casilla: 6 , 2
 Casilla: 7 , 4
 Casilla: 8 , 7
S = [1, 5, 2, 3, 3, 1, 4, 6, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 2
 Casilla: 3 , 8
 Casilla: 4 , 6
 Casilla: 5 , 1
 Casilla: 6 , 3
 Casilla: 7 , 5
 Casilla: 8 , 7
S = [1, 4, 2, 2, 3, 8, 4, 6, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 3
 Casilla: 3 , 5
 Casilla: 4 , 7
 Casilla: 5 , 1
 Casilla: 6 , 4
 Casilla: 7 , 2
 Casilla: 8 , 8
S = [1, 6, 2, 3, 3, 5, 4, 7, 5|...] ;
 Casilla: 1 , 6
 Casilla: 2 , 4
 Casilla: 3 , 7
 Casilla: 4 , 1
 Casilla: 5 , 3
 Casilla: 6 , 5
 Casilla: 7 , 2
 Casilla: 8 , 8
S = [1, 6, 2, 4, 3, 7, 4, 1, 5|...] ;
 Casilla: 1 , 4
 Casilla: 2 , 7
 Casilla: 3 , 5
 Casilla: 4 , 2
 Casilla: 5 , 6
 Casilla: 6 , 1
 Casilla: 7 , 3
 Casilla: 8 , 8
S = [1, 4, 2, 7, 3, 5, 4, 2, 5|...] ;
 Casilla: 1 , 5
 Casilla: 2 , 7
 Casilla: 3 , 2
 Casilla: 4 , 6
 Casilla: 5 , 3
 Casilla: 6 , 1
 Casilla: 7 , 4
 Casilla: 8 , 8
S = [1, 5, 2, 7, 3, 2, 4, 6, 5|...] ;
false.

*/