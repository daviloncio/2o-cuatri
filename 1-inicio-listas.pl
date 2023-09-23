% Hechos
    ordenada([]).
    ordenada([_]).
% Reglas
    ordenada([X|[Y|Zs]]) :- 
        X =< Y, 
        ordenada([Y|Zs]).

main :- print("inicio-listas").

/* Ejemplos de consultas

?- ordenada([2]).
true .

?- ordenada([2,0,5]).
false.

?- ordenada([1,2,3]).
true .

?- ordenada([1 | [2,3]]).
true .

?- ordenada([1,X]).   
ERROR: Arguments are not sufficiently instantiated

?- trace, ordenada([1,2,3]).
   Call: (11) ordenada([1, 2, 3]) ? creep
        Call: (12) 1=<2 ? creep
        Exit: (12) 1=<2 ? creep
        Call: (12) ordenada([2, 3]) ? creep
            Call: (13) 2=<3 ? creep
            Exit: (13) 2=<3 ? creep
            Call: (13) ordenada([3]) ? creep
            Exit: (13) ordenada([3]) ? creep
        Exit: (12) ordenada([2, 3]) ? creep
   Exit: (11) ordenada([1, 2, 3]) ? creep
true .

?- trace, ordenada([1,X]).
   Call: (11) ordenada([1, _1320]) ? creep
   Call: (12) 1=<_1320 ? creep
ERROR: Arguments are not sufficiently instantiated
ERROR: In:
ERROR:   [12] 1=<_4128
ERROR:   [11] ordenada([1,_4162]) 
...

[trace] ?- nodebug.
true.

?- main.
"inicio-listas"
true.

?. halt.
FINALIZAR PROLOG

*/
