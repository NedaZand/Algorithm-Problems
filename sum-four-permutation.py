from itertools import permutations  

arr=[1, 0, -1, 0, -2, 2]
permArr = list(permutations(arr,4))

def summer(a):
    sum=0
    for j in a:
        sum = sum + j
    return(sum)
    
result=[]
for i in permArr:
    answer = summer(i)
    if(answer == 0):
        result.append(i)
   
    
print(result)