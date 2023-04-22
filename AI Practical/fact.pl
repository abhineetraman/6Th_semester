factorial(1,1):-!.
factorial(N,Fact_of_N):-
    Q is N-1,
    factorial(Q, Fact_of_Q),
    write(Fact_of_Q),nl,
    Fact_of_N is N*Fact_of_Q.
