dmerge([],L2,L2). 
dmerge(L1,[],L1).
dmerge([H1|T1],[H2|T2],[H1|T3]):- H1=<H2,
dmerge(T1,[H2|T2],T3).
dmerge([H1|T1],[H2|T2],[H2|T3]):- dmerge([H1|T1],T2,T3).
