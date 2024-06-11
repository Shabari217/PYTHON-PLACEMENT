#swap function
def swaplist(i):
    size=len(i)
    temp=li[0]
    li[0]=li[size-1]
    li[size-1]=temp
    return li
li=[12,35,9,56,24]
print(swaplist(li))

#swap elements at given position
def swapPositions(lis,pos1,pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
lis=[23,65,19,90]
pos1,pos2=1,3
print(swapPositions(lis,pos1-1,pos2-1))

# sum and average

L=[4,5,1,2,9,7,10,8]
sum=0
for i in L:
    sum=sum+i

avg=sum/len(L)

print("sum=",sum)
print("average=",avg)
print(L[0])
print(L[7])

#find minimum and maximum elemrnt in an array

L=[0,1,2,5]

L.sort()
print("Smallest element is:",L[0])
print("Largest element is:",L[-1])