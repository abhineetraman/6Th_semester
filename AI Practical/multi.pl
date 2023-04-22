multi(N1,1,N1). 
multi(N1,N2,Ans):- Temp is N2-1,
     multi(N1,Temp,Ans1),
     Ans is Ans1+N1.
