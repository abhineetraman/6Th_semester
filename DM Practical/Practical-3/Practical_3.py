# Load the data from wine dataset. Check whether all attributes are standardized or not (mean 
# is 0 and standard deviation is 1). If not, standardize the attributes. Do the same with Iris dataset.

import statistics as st
import csv

meanWine=[0]
standardDeviationWine=[1]

with open("./wineDataset.csv",'r') as csvfile:
    wine_data = csv.reader(csvfile)
    data_Store = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    for i in wine_data:
        data_Store[0].append(int(i[0]))
        for j in range(1,len(i)):
            data_Store[j].append(float(i[j]))
    for i in range(1,len(data_Store)):
        meanWine.append(st.mean(data_Store[i]))
        standardDeviationWine.append(st.stdev(data_Store[i]))


isMean=True
isStandardDeviation=True
for x in meanWine:
    if (round(x)!=0):
        isMean=False
for x in standardDeviationWine:
    if(round(x)!=1):
        isStandardDeviation=False

print(isMean)
print(isStandardDeviation)
if(isMean==False and isStandardDeviation==False):
    with open("./wineStandardDataset.csv",'w+',newline="",encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(0,len(data_Store[0])):
            tempRow=[]
            for j in range(0,len(data_Store)):
                if j==0:
                    tempRow.append(data_Store[j][i])
                else:
                    val=round((data_Store[j][i]-meanWine[j])/standardDeviationWine[j],2)
                    tempRow.append(val)
            writer.writerow(tempRow)


# For Iris Data Set

def isfloat(num):
    if num == 'Inf':
        return False
    try:
        float(num)
        return True
    except ValueError:
        return False
        

meanIris=[]
standardDeviationIris=[]
data=[]
with open('./irisDataSet.csv','r') as csvfile:
    iris_data = csv.reader(csvfile)
    field = next(iris_data)
    data.append(field)
    iris_data_set=[[],[],[],[]]
    for i in iris_data:
       data.append(i) 
       if isfloat(i[0]):
        iris_data_set[0].append(float(i[0]))
       if isfloat(i[1]):
        iris_data_set[1].append(float(i[1]))
       if isfloat(i[2]):
        iris_data_set[2].append(float(i[2]))
       if isfloat(i[3]):
        iris_data_set[3].append(float(i[3]))

for i in iris_data_set:
    meanIris.append(round(st.mean(i),1))
    standardDeviationIris.append(round(st.stdev(i),1))

print(meanIris)
print(standardDeviationIris)

isMeanIris = True
isStdDeviationIris = True

for i in range(0,len(meanIris)):
    if round(meanIris[i])!=0:
        isMeanIris=False
    if round(standardDeviationIris[i])!=1:
        isStdDeviationIris=False

if (isMeanIris==False and isStdDeviationIris==False):
        with open("./irisDataSetStandard.csv",'w+',newline="",encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data[0])

            for i in data[1::]:
                temprow=[]
                for j in range(0,len(i)-1):
                    if isfloat(i[j]):
                        val = round((float(i[j])-meanIris[j])/standardDeviationIris[j],1)
                        temprow.append(val)
                    else:
                        temprow.append(i[j])
                temprow.append(i[4])
                writer.writerow(temprow)