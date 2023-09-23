/*
El encapsulamiento de datos (data/Haskell, class/Python)
    se puede conseguir en Prolog usando funciones
El último argumento de cada predicado suele corresponder
    con el retorno, como en Haskell o Python    
*/

area(circulo(punto(_,_), Radio), Area) :-
    Area is pi* Radio**2.

producto(vector(X1,Y1), vector(X2,Y2), Producto) :-
    Producto is X1*X2 + Y1*Y2.

producto(vector([A]), vector([B]), Producto) :-
    Producto is A*B,
    !.
producto(vector([A | AS]), vector([B | BS]), Producto) :-
    Primero is A*B,
    producto(vector(AS), vector(BS), ProductoResto),
    Producto is Primero+ProductoResto.

sumar(fraccion(Num1, Denom1), fraccion(Num2, Denom2), Sumar) :-
    NumRes is Num1*Denom2+Denom1*Num2,
    DenRes is Denom1*Denom2,
    Sumar = fraccion(NumRes, DenRes).

% Funciones aritméticas, condicionales ------------------------

absoluto(Numero, Absoluto) :-
    Numero>0,  
    Absoluto is Numero,
    !.
absoluto(Numero, Absoluto) :-
    Absoluto is -Numero.

% ---------------------------------------------------------------

main :- print('calculos').

/* Ejemplos

?- area(circulo(punto(0,0),2), X).
X = 12.566370614359172.

?- producto(vector(1,2), vector(3,4), X).
X = 11.

?- producto(vector([2]), vector([3]), 6).
true.

?- producto(vector([2]), vector([3]), X).    
X = 6.

?- producto(vector([1,2,3]), vector([4,5,6]), X).
X = 32.

?- sumar(fraccion(2,3),fraccion(4,5),X).
X = fraccion(22, 15).

?- absoluto(4,X).
X = 4.

?- absoluto(-4,X).
X = 4.

*/