insert(L,1,Elem,[Elem|L]):-!. insert([],_,Elem,[Elem]). 
insert([H|T],N,Elem,[H|R]):- C is N-1,
insert(T,C,Elem,R).
