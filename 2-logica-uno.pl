% Hechos
   chico(juan).
   chico(pepe).
   chica(ana).
   chica(maria).
% Reglas
   invita(X, Y) :- chico(X), chica(Y).
   % regla para hacer "debugging" llamando a "print"
   invitaPrint(X, Y) :- chico(X), print("X"+X), chica(Y), print("Y"+Y).

main :- print("logica-uno").

% para mostrar todas las soluciones de una vez:
mainPrint1 :- forall(invita(X, Y), (print(X+Y), nl)). % nl significa "newline"
mainPrint2 :- findall((X,Y), invita(X, Y), Resultado), print(Resultado). 

/* Ejemplos de consultas

En cada consulta pulsar ; tras cada solución
Si pulsamos . ya no se buscan más soluciones

?- invita(X, Y).
X = juan,
Y = ana ;
X = juan, 
Y = maria ;
X = pepe,
Y = ana ;
X = pepe, 
Y = maria.

?- mainPrint1.
juan+ana
juan+maria
pepe+ana
pepe+maria
true.

?- mainPrint2.
[(juan,ana),(juan,maria),(pepe,ana),(pepe,maria)]
true.

?- invita(X, X).
false.

?- trace.

[trace] ?- invita(X, Y).
   Call: (10) invita(_14628, _14630) ? creep
      Call: (11) chico(_14628) ? creep
      Exit: (11) chico(juan) ? creep
      Call: (11) chica(_14630) ? creep
      Exit: (11) chica(ana) ? creep
   Exit: (10) invita(juan, ana) ? creep
X = juan,
Y = ana ;
      Redo: (11) chica(_14630) ? creep
      Exit: (11) chica(maria) ? creep
   Exit: (10) invita(juan, maria) ? creep
X = juan,
Y = maria ;
      Redo: (11) chico(_14628) ? creep
      Exit: (11) chico(pepe) ? creep
      Call: (11) chica(_14630) ? creep
      Exit: (11) chica(ana) ? creep
   Exit: (10) invita(pepe, ana) ? creep
X = pepe,
Y = ana ;
      Redo: (11) chica(_14630) ? creep
      Exit: (11) chica(maria) ? creep
   Exit: (10) invita(pepe, maria) ? creep
X = pepe,
Y = maria.

[trace] ?- invitaPrint(X, Y).
   Call: (10) invitaPrint(_14750, _14752) ? creep
      Call: (11) chico(_14750) ? creep
      Exit: (11) chico(juan) ? creep
      Call: (11) print("X"+juan) ? creep
"X"+juan
      Exit: (11) print("X"+juan) ? creep
      Call: (11) chica(_14752) ? creep
      Exit: (11) chica(ana) ? creep
      Call: (11) print("Y"+ana) ? creep
"Y"+ana
      Exit: (11) print("Y"+ana) ? creep
   Exit: (10) invitaPrint(juan, ana) ? creep
X = juan,
Y = ana ;
      Redo: (11) chica(_14752) ? creep
      Exit: (11) chica(maria) ? creep
      Call: (11) print("Y"+maria) ? creep
"Y"+maria
      Exit: (11) print("Y"+maria) ? creep
   Exit: (10) invitaPrint(juan, maria) ? creep
X = juan,
Y = maria ;
      Redo: (11) chico(_14750) ? creep
      Exit: (11) chico(pepe) ? creep
      Call: (11) print("X"+pepe) ? creep
"X"+pepe
      Exit: (11) print("X"+pepe) ? creep
      Call: (11) chica(_14752) ? creep
      Exit: (11) chica(ana) ? creep
      Call: (11) print("Y"+ana) ? creep
"Y"+ana
      Exit: (11) print("Y"+ana) ? creep
   Exit: (10) invitaPrint(pepe, ana) ? creep
X = pepe,
Y = ana ;
      Redo: (11) chica(_14752) ? creep
      Exit: (11) chica(maria) ? creep
      Call: (11) print("Y"+maria) ? creep
"Y"+maria
      Exit: (11) print("Y"+maria) ? creep
   Exit: (10) invitaPrint(pepe, maria) ? creep
X = pepe,
Y = maria.

print y write son similares, pero no son equivalentes:
   ?- print('hola'), nl, print('hola  '), nl, write('hola  '), write('final'). 
   hola
   'hola  '
   hola  final
   true.

*/