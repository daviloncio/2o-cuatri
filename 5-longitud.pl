/* Haskell
   longitud :: Num p => [a] -> p
   longitud [] = 0
   longitud (x:xs) = longitud xs + 1
*/

longitud([], 0).
longitud([_|XS], Longitud) :- 
   longitud(XS, LongitudResto), 
   Longitud is LongitudResto+1.

main :- print("longitud").

/* Ejemplos de consultas

?- trace.
true. 

[trace] ?- longitud([a,b], 2).
   Call: (10) longitud([a, b], 2) ? creep
      Call: (11) longitud([b], _4190) ? creep
         Call: (12) longitud([], _5002) ? creep
         Exit: (12) longitud([], 0) ? creep
         Call: (12) _4190 is 0+1 ? creep
         Exit: (12) 1 is 0+1 ? creep
      Exit: (11) longitud([b], 1) ? creep
      Call: (11) 2 is 1+1 ? creep
      Exit: (11) 2 is 1+1 ? creep
   Exit: (10) longitud([a, b], 2) ? creep
true.

[trace] ?- longitud([a,b], X). 
   Call: (10) longitud([a, b], _228) ? creep
   Call: (11) longitud([b], _1554) ? creep
   Call: (12) longitud([], _2366) ? creep
   Exit: (12) longitud([], 0) ? creep
   Call: (12) _1554 is 0+1 ? creep
   Exit: (12) 1 is 0+1 ? creep
   Exit: (11) longitud([b], 1) ? creep
   Call: (11) _228 is 1+1 ? creep
   Exit: (11) 2 is 1+1 ? creep
   Exit: (10) longitud([a, b], 2) ? creep
X = 2.

*/