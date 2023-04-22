sumlist([],0). 
sumlist([H|T],S):- sumlist(T,S1),
   S is H+S1.
