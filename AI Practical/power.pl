power(Num,1,Num).
power(Num,Pow,Ans):- Pow1 is Pow-1,
    power(Num,Pow1,Ans1),
    Ans is Ans1*Num. 
