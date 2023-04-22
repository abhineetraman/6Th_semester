maxlist([H],H). 
maxlist([H|T],M):- maxlist(T,M1),
H M is M1; 
M is H.
