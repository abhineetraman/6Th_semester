maxlist([H],H). 
maxlist([H|T],M):- 
	maxlist(T,M1),
	max(H,M1,M). 

max(X,Y,X):- X>=Y,!.
max(_,Y,Y).
