import pandas as pd
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

data = pd.read_csv('./breast-cancer.csv')

dataset = [['A', 'B', 'C', 'D', 'F', 'H'],['B', 'E', 'F', 'H'],['A', 'C', 'E'],['B', 'C', 'D', 'F', 'H'],
['A', 'B', 'C', 'D', 'E'],['C','D','F','H'],['A','C','D','H'],['E','H']]

records=[]

for i in range(0,len(data)):
    records.append([str(data.values[i,j]) for j in range(0,10)])

TE = TransactionEncoder()
# For Breast cancer data
# TE_ary = TE.fit(records).transform(records)

# For dataset
TE_ary = TE.fit(dataset).transform(dataset)

df = pd.DataFrame(TE_ary,columns=TE.columns_)
print(df)

# Frequent Itemsets with minimum support 50%
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print(frequent_itemsets)
# Association rules with minimum confidence 75%
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0.75))

# Frequent Itemsets with minimum support 60%
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print(frequent_itemsets)
# Association rules with minimum confidence 60%
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6))