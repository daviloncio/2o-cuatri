% Hechos
    p.          % cláusula: [p]
    q.          % cláusula: [q]
% Reglas
    s :- p.     % cláusula: NO[p] OR [s]
    r :- p,q.   % cláusula: NO[p] OR NO[q] OR [r]

main :- print("logica-cero").

/* Ejemplos de consultas

?.- s.        % negación consulta: NO[s]
true.

?.- r.        % negación consulta: NO[r]
true.

?.- s,r.      % negación consulta: NO[s] OR NO[r]
true.

?- trace.
true.

[trace] ?- s,r.
   Call: (11) s ? creep
        Call: (12) p ? creep
        Exit: (12) p ? creep
   Exit: (11) s ? creep
   Call: (11) r ? creep
        Call: (12) p ? creep
        Exit: (12) p ? creep
        Call: (12) q ? creep
        Exit: (12) q ? creep
   Exit: (11) r ? creep
true.

*/
