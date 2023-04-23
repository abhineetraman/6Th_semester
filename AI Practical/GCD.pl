gcd(M,0,M):-!.
gcd(M,N,D):-
   N > 0,
   X is mod(M,N),
   gcd(N,X,D).
