delte(1,[_|T],T). 
delte(P,[X|Y],[X|R]):- P1 is P-1,
delte(P1,Y,R).
