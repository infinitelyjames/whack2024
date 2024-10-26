import matplotlib.pyplot as plt
import numpy as np
arr=[] #creating the array
# using loadtxt()
filename = "1MSFT.csv"
if filename[0]=="1":
    arr = np.loadtxt(filename,
                 delimiter=",", dtype=str, skiprows= 1, usecols=2)
    arr05 = []
    print(arr)
    for i in range(len(arr)-1,0,-1):
        temp = (arr[i])[:-4]
        arr05.append(int(temp[1:]))
else:
    arr = np.loadtxt(filename,delimiter=",", dtype=str, skiprows= 1, usecols=(3,2))
    arr05 = []
    for i in range(len(arr)-1,0,-1):
        temp = (arr[i][0]+arr[i][1])[:-4]
        arr05.append(int(temp[1:]))
#displaying our result.

temp = []
for i in range(len(arr05)):
    temp.append(i)
xpoints = np.array(temp)
ypoints = np.array(arr05)
plt.plot(xpoints, ypoints)
plt.show()