import math 
import csv

with open("Project/data.csv", newline='')as f:
    r = csv.reader(f)
    file_data = list(r)
data = file_data[0]

def mean(data):
    n = len(data)
    sum = 0
    for i in data:
        sum += int(i)
    mean = sum/n
    return mean

squaredList = []

for i in data:
    a = int(i)- mean(data)
    a = a**2
    squaredList.append(a)
    
sum = 0
for i in squaredList:
    sum = sum+i
    
result = sum/ ( len(data))
standardDeviation = math.sqrt(result)
print(f"This is your required standard deviation of the data ==> {standardDeviation}")
