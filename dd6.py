import csv
import pprint
from tqdm import tqdm
import time

subs=[]
arr = [['NA' for _ in range(30)] for _ in range(30)]
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if i == j: 
      arr[i][j] = '-'

for i in range(3):
    for j in range(10):
        if(j!=9):
            index="0"+str(i+1)+"0"+str(j+1)
        else:
            index=ndex="0"+str(i+1)+str(j+1)

        with open("dd6/"+index+".csv") as f:
            reader=csv.reader(f)
            subs.append([row for row in reader])

for a in range(30):
    for b in range(30):

        if(a<b):
            dences=[]
            Margin=0
            length=0

            if(len(subs[a])>len(subs[b])):
                length=len(subs[b])-60
                Margin=len(subs[a])-len(subs[b])
            else:
                length=len(subs[a])-60
                Margin=len(subs[b])-len(subs[a])
            
            for i in tqdm(range(length)):

                sums=0
                difs=0
                dence=1

                
                    
                for j in range(60):
                    
                        if(len(subs[a])>len(subs[b])):
                            dif=int(subs[a][i+1+j+Margin][2])-int(subs[b][i+1+j][2])
                            sum=int(subs[a][i+1+j+Margin][2])+int(subs[b][i+1+j][2])
                        elif(len(subs[a])>len(subs[b])):
                            dif=int(subs[a][i+1+j][2])-int(subs[b][i+1+j+Margin][2])
                            sum=int(subs[a][i+1+j][2])+int(subs[b][i+1+j+Margin][2])
                        else:
                            dif=int(subs[a][i+1+j][2])-int(subs[b][i+1+j][2])
                            sum=int(subs[a][i+1+j][2])+int(subs[b][i+1+j][2])

                        dif=dif*dif
                        
                        sum=sum*sum
                        sums+=sum
                        difs+=dif
                    
            
                if(sums>=5500):
                    dence=difs/sums

                dences.append(dence)

            point=0

            for i in range(len(dences)-15):
                get=True

                for j in range(15):
                    if((dences[i+j])>0.05):
                        get=False

                if(get):
                    point+=1
            
            arr[a][b] = point
            arr[b][a] = point
print(arr)