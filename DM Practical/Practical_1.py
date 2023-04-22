people_file = open('People.txt','r')
people_data = [i.split() for i in (people_file.readlines()[1::])]

# Create a ruleset E that contain rules to check for the following conditions:
# 1. The age should be in the range 0-150.
# 2. The age should be greater than yearsmarried.
# 3. The status should be married or single or widowed.
# 4. If age is less than 18 the agegroup should be child, if age is between 18 and 65 the agegroup
# should be adult, if age is more than 65 the agegroup should be elderly.

class People:

    def __init__(self,age,ageGroup,height,status,yearMarried):
        self.age = int(age)
        self.ageGroup=ageGroup
        self.height=float(height)
        self.status=status
        self.yearMarried=int(yearMarried)

    def verifyAge(self):
        if(self.age>=0 and self.age<=150):
            return True
        return False
    
    def verifyYearsMarried(self):
        if(self.age>self.yearMarried):
            return True
        return False

    def verifyStatus(self):
        check=['married','single','widowed']
        if self.status.lower() in check:
            return True
        return False

    def verifyAgeGroup(self):
        if self.age<=18 and self.ageGroup.lower()=='child':
            return True
        elif self.age<=65 and self.ageGroup.lower()=='adult':
            return True
        elif self.age>65 and self.ageGroup.lower()=='elderly':
            return True
        else:
            return False

    def verify(self):
        if self.verifyAge() and self.verifyAgeGroup() and self.verifyYearsMarried() and self.verifyStatus():
            return True
        return False
    
# Check whether ruleset E is violated by the data in the file people.txt.
peoples=[]
ageVisualize=[0,0]
ageGroupVisualize=[0,0]
statusVisualize=[0,0]
yearMarriedVisualize=[0,0]
for i in people_data:
    peoples.append(People(i[0],i[1],i[2],i[3],i[4]))
for i in range(0,len(peoples)):
    print(f"People-{i+1}:-")

    if peoples[i].verifyAge():
        ageVisualize[0]+=1 
    else:
        ageVisualize[1]+=1
    print("Age: ","satisfied" if peoples[i].verifyAge() else "unsatisfied")

    if peoples[i].verifyAgeGroup():
        ageGroupVisualize[0]+=1 
    else:
         ageGroupVisualize[1]+=1
    print("AgeGroup: ","satisfied" if peoples[i].verifyAgeGroup() else "unsatisfied")

    if peoples[i].verifyStatus():
        statusVisualize[0]+=1 
    else:
         statusVisualize[1]+=1
    print("Status: ","satisfied" if peoples[i].verifyStatus() else "unsatisfied")

    if peoples[i].verifyYearsMarried():
        yearMarriedVisualize[0]+=1 
    else:
        yearMarriedVisualize[1]+=1
    print("Year-Married: ","satisfied" if peoples[i].verifyYearsMarried() else "unsatisfied")

    print(ageVisualize)
    print(ageGroupVisualize)
    print(statusVisualize)
    print(yearMarriedVisualize)

# Summarize the results obtained in above part
allVisualize=[0,0]
for i in range(0,len(peoples)):
    if peoples[i].verify():
        allVisualize[0]+=1
    else:
        allVisualize[1]+=1
    print(f"People-{i+1}: {'All Satisfied' if peoples[i].verify() else 'One or more condition violates'}")