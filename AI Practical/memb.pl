memb(X, [X|Tail]).
   memb(X, [Head|Tail]):- memb(X, Tail).
