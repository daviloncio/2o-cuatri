% Hechos
    mujer(ana).
    mujer(marta).
    mujer(alicia).
    mujer(carmen).
    mujer(laura).
    mujer(isabel).
    mujer(silvia).
    hombre(juan).
    hombre(luis).
    hombre(miguel).
    hombre(alberto).
    hombre(rodrigo).
    hombre(pedro).
    padres(juan,luis,ana).
    padres(alberto,luis,ana).
    padres(marta,luis,ana).
    padres(alicia,luis,ana).
    padres(rodrigo,juan,laura).
    padres(carmen,juan,laura).
    padres(isabel,juan,laura).
    padres(miguel,juan,laura).
    padres(laura,pedro,silvia).
% Reglas
    hermana(X,Y) :- 
        mujer(X),
        padres(X,P,M),
        padres(Y,P,M).
        % X \= Y. para impedir que una mujer sea "hermana de sí misma"    
    ascendiente(X,Y) :-
        padres(Y,X,_). % X es padre de Y
    ascendiente(X,Y) :-
        padres(Y,_,X). % X es madre de Y
    ascendiente(X,Y) :-
        padres(Y,Z,_), % Z es padre de Y
        ascendiente(X,Z). 
    ascendiente(X,Y) :-
        padres(Y,_,Z), % Z es madre de Y
        ascendiente(X,Z).

main :- print("inicio-familias").

/* Ejemplos de consultas

?- hermana(carmen,isabel).
true.

?- hermana(carmen,marta).  
false.

?- ascendiente(silvia,isabel).
true .

?- ascendiente(silvia,alicia). 
false.

?- ascendiente(pedro,X).    
X = laura ;
X = rodrigo ;
X = carmen ;
X = isabel ;
X = miguel ;
false.

*/
