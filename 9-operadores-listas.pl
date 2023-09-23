
lista_ejemplo(X) :-
    X=[2, [sevilla, cadiz, malaga], 3.5, 'hola'], % unificación
    print(X). 

/* Algunos ejemplos con listas y operadores

?- lista_ejemplo(3).
false.

?- lista_ejemplo(X).
[2,[sevilla,cadiz,malaga],3.5,hola]
X = [2, [sevilla, cadiz, malaga], 3.5, hola].

?- [X | Xs] = 'hola'.
false.

?- [X | Xs] = [h, o, l, a].
X = h,
Xs = [o, l, a].

?- [X, Y | Zs] = [h, o, l, a].  
X = h,
Y = o,
Zs = [l, a].

?- [X | [ Y | Zs]] = [h, o, l, a].  
X = h,      
Y = o,      
Zs = [l, a].

?- print(3+4).
3+4
true.

?- X is 3+4, print(X).
7
X = 7.

?- 1+2==2+1.
false.

?- 1+2==1+2.
true.

?- X==Y.
false.

?- X=Y.  
X = Y.

?- member(X, [1,2,3]). 
X = 1 ;
X = 2 ;
X = 3.

?- \+member(X, [1,2,3]). 
false.

?- append([1+1,2],[3,4],[X|XS]).
X = 1+1,
XS = [2, 3, 4].

?- forall(member(X, [1,2,3]), (print(X), write(' '))). 
1 2 3 
true. 

?- findall((x,y), member(X, [1,2,3]), Resultado), print(Resultado).
[(x,y),(x,y),(x,y)]
Resultado = [(x, y), (x, y), (x, y)].

*/

main :- print('operadores-listas').