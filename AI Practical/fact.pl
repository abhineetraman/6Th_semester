factorial(0,1). 
factorial(N,X):- 
	N1 is N-1, 
	factorial(N1,X1), 
	X is X1*N.
