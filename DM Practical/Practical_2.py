def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

class Iris:
    def __init__(self,sepalLength,sepalWidth,petalLength,petalWidth,species) -> None:
        self.sepalLength = float(sepalLength) if isFloat(sepalLength) else 0.0
        self.sepalWidth = float(sepalWidth) if isFloat(sepalWidth) else 0.0
        self.petalLength = float(petalLength) if isFloat(petalLength) else 0.0
        self.petalWidth = float(petalWidth) if isFloat(petalWidth) else 0.0
        self.species=species
    
    def checkSpecies(self):
        possibleValue = ["setosa","versicolor","virginica"]
        if (self.species in possibleValue):
            return True
        return False
    
    def checkPetalLengthSign(self):
        if (self.petalLength>0.0):
            return True
        return False
    
    def checkPetalWidthSign(self):
        if(self.petalWidth>0.0):
            return True
        return False
    def checkSepalLengthSign(self):
        if(self.sepalLength>0.0):
            return True
        return False
    def checkSepalWidthSign(self):
        if(self.sepalWidth>0.0):
            return True
        return False
    
    def checkPetalLength(self):
        if(self.petalLength>=2*self.petalWidth):
            return True
        else:
            return False

    def checkSepalLength(self):
        if(self.sepalLength>0 and self.sepalLength<=30):
            return True
        return False

    def compareSepalPetal(self):
        if(self.sepalLength>self.petalLength):
            return True
        return False

import csv

# Calculate the number and percentage of observations that are complete.
complete_count=0
Number_of_entries=0
rows=[]
with open('./iris.csv','r') as csvfile:
    iris_data = csv.reader(csvfile)
    field = next(iris_data)
    rows.append(field)
    for i in iris_data:
        rows.append(i)
        Number_of_entries+=1
        if "NA" not in i:
            complete_count+=1

complete_percentage = (complete_count/Number_of_entries)*100
print("Complete Observations: ",complete_count)
print("InComplete Observations: ",Number_of_entries-complete_count)
print("Complete Observation Percentage: ",complete_percentage,"%")
print("InComplete Observation Percentage: ",100-complete_percentage,"%")
# print(rows)

# Replace all the special values in data with NA.

with open('./final_iris.csv','w+',newline="",encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(rows[0])

    for i in rows[1::]:
        if("Inf" in i):
            i[i.index("Inf")]="NA"
        writer.writerow(i)

# Define these rules in a separate text file and read them.

iris = []
with open('./final_iris.csv','r') as csvfile:
    data = csv.reader(csvfile)
    header = next(data)
    for i in data:
        iris.append(Iris(*i))

# Determine how often each rule is broken (violatedEdits). Also summarize and plot the result.
species=[0,0]
PLsign=[0,0]
PWsign=[0,0]
SLsign=[0,0]
SWsign=[0,0]
petalLength=[0,0]
sepalLength=[0,0]
sepalPetal=[0,0]

for i in iris:
    if(i.checkSpecies()):
        species[0]+=1
    else:
        species[1]+=1
    
    if(i.checkPetalLengthSign()):
        PLsign[0]+=1
    else:
        PLsign[1]+=1
        print(i.petalLength)

    if(i.checkPetalWidthSign()):
        PWsign[0]+=1
    else:
        PWsign[1]+=1

    if(i.checkSepalLengthSign()):
        SLsign[0]+=1
    else:
        SLsign[1]+=1

    if(i.checkSepalWidthSign()):
        SWsign[0]+=1
    else:
        SWsign[1]+=1
    
    if(i.checkPetalLength()):
        petalLength[0]+=1
    else:
        petalLength[1]+=1

    if(i.checkSepalLength()):
        sepalLength[0]+=1
    else:
        sepalLength[1]+=1

    if(i.compareSepalPetal()):
        sepalPetal[0]+=1
    else:
        sepalPetal[1]+=1

print("Valid iris on the basis of Species: ",species[0])
print("Invalid iris on the basis of Species: ",species[1])
print("Positive Petal Length: ",PLsign[0])
print("Negative Petal Length or NA: ",PLsign[1])
print("Positive Petal Width: ",PWsign[0])
print("Negative Petal Width or NA: ",PWsign[1])
print("Positive Sepal Length: ",SLsign[0])
print("Negative Sepal Length or NA: ",SLsign[1])
print("Positive Sepal Width: ",SWsign[0])
print("Negative Sepal Width or NA: ",SWsign[1])
print("Iris with Sepal Length less than 30cm: ",sepalLength[0])
print("Iris with Sepal Length more than 30cm: ",sepalLength[1])
print("Iris with its Petal Length equal to atleast two times of its Petal Width: ",petalLength[0])
print("Iris with its Petal Length equal to less than two times of its Petal Width: ",petalLength[1])
print("Iris with Sepal greater than its Petals: ",sepalPetal[0])
print("Iris with Sepal less than its Petals: ",sepalPetal[1])

# Visualization
# import matplotlib.pyplot as plt
# import numpy as np
# x=['Valid','Invalid']
# N=2
# width=0.10
# ind=np.arange(N)

# bar1=plt.bar(ind,species,width,color='red')
# bar2=plt.bar(ind+width,PLsign,width,color="green")
# bar3=plt.bar(ind+width*2,PWsign,width,color="blue")
# bar4=plt.bar(ind+width*3,SLsign,width,color="yellow")
# bar5=plt.bar(ind+width*4,SWsign,width,color="orange")
# bar6=plt.bar(ind+width*5,petalLength,width,color="skyblue")
# bar7=plt.bar(ind+width*6,sepalLength,width,color="maroon")
# bar8=plt.bar(ind+width*7,sepalPetal,width,color="purple")

# plt.ylabel("Number of Iris")
# plt.title("Overall Visualization")

# plt.xticks(ind+width,x)
# plt.legend((bar1,bar2,bar3,bar4,bar5,bar6,bar7,bar8),("Species","PetalLengthSign","PetalWidthSign","SepalLengthSign","SepalWidthSign","PetalLength","SepalLength","Relation between SepalLength and PetalLength"))
# plt.show()

# Find outliers in sepal length using boxplot and boxplot.stats
sepalLengthValues=[]
for i in iris:
    sepalLengthValues.append(i.sepalLength)

# print(sepalLengthValues)

# Sepal Length Visualization
# plt.boxplot(sepalLengthValues)
# plt.show()