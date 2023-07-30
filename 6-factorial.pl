
factorial(0, 1) :-
    !. % "cut operator", para no crear "choice points"

factorial(Numero, Factorial) :-
    Numero>0,
    Anterior is Numero-1,
    factorial(Anterior, FactorialAnterior),
    Factorial is Numero*FactorialAnterior,
    !.  % "cut operator", para no crear "choice points"

factorial(_, _) :-
    write('No existe el factorial de ese numero'),
    nl.

main :- print("longitud").

/* Ejemplos de consultas

?- factorial(0,X).
X = 1.

Resultado si no hubiéramos usado el "cut operator":
    ?- factorial(0,X).
    X = 1 ;
    No existe el factorial de ese numero
    true.

?- factorial(3, 6). 
true.

?- factorial(3, X).
X = 6.

?- factorial(-4, X).
No existe el factorial de ese numero
true.

?- trace, factorial(3,6). 
   Call: (11) factorial(3, 6) ? creep
   Call: (12) 3>0 ? creep
   Exit: (12) 3>0 ? creep
   Call: (12) _15300 is 3+ -1 ? creep
   Exit: (12) 2 is 3+ -1 ? creep
   Call: (12) factorial(2, _16922) ? creep
   Call: (13) 2>0 ? creep
   Exit: (13) 2>0 ? creep
   Call: (13) _19360 is 2+ -1 ? creep
   Exit: (13) 1 is 2+ -1 ? creep
   Call: (13) factorial(1, _20982) ? creep
   Call: (14) 1>0 ? creep
   Exit: (14) 1>0 ? creep
   Call: (14) _23420 is 1+ -1 ? creep
   Exit: (14) 0 is 1+ -1 ? creep
   Call: (14) factorial(0, _25042) ? creep
   Exit: (14) factorial(0, 1) ? creep
   Call: (14) _20982 is 1*1 ? creep
   Exit: (14) 1 is 1*1 ? creep
   Exit: (13) factorial(1, 1) ? creep
   Call: (13) _16922 is 2*1 ? creep
   Exit: (13) 2 is 2*1 ? creep
   Exit: (12) factorial(2, 2) ? creep
   Call: (12) 6 is 3*2 ? creep
   Exit: (12) 6 is 3*2 ? creep
   Exit: (11) factorial(3, 6) ? creep
true.

*/