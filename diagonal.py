import numpy as np
x=2*np.ones((20,20))

for i in range(20):
    for j in range(20):
        
        if(i==j):
            x[i][j]=10
            
for i in range(20):
    for j in range(20):     
        if((i+j)==(20-1)):
            x[i][j]=20
            
            
            
print(x)