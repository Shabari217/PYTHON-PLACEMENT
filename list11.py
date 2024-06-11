# count the no of occurences of a given item in the lis

def count_occ(li,x):
    c=0
    for i in li:
        if(i==x):
            c=c+1
    return c
li=[8,6,8,20,8,10,9,8]
x=8
print(count_occ(li,x))

# write program to count unique values in the list

L=[1,2,2,5,8,4,4,8]
l1=[]
c=0
for i in L:
    if i not in l1:
        c +=1
        l1.append(i)
print("No of unique items are:",c)



# find out the duplicate removal list product using list comprehension
def d_prod(res_list):
    prod=1
    for ele in res_list:
        prod=prod*ele
    return prod
test_list=[1,3,5,6,3,5,6,1]
print("The original list is:"+str(test_list))
res=[]
[res.append(x) for x in test_list if x not in res]
product=d_prod(res)
print("Duplication removal list product:" +str(product))


# write a program to extract elemrnts with a frequency greater than k


test_list=[4,6,4,3,3,4,3,7,8,8,8]
print("The original list:"+str(test_list))
k=2
res=[]
for i in test_list:
    freq=test_list.count(i)
    if freq>k and i not in res:
        res.append(i)
print("The required elements:"+str(res))

# write a program to test if a list contains elements in the range 

test_list=[4,5,6,7,3,9]
print("the original list is:"+str(test_list))
i,j=3,10
res=True
for ele in test_list:
    if ele <i or ele> j:
        res=False
        break
print("Does list contain all elemrnts in range:"+str(res))


# write a program to demonstrate list intersection and union

def list_intersection(l1,l2):
    return list(set(l1) & set(l2))
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
print("Intersection:",list_intersection(l1,l2))

def list_union(l1,l2):
    return list(set(l1) | set(l2))
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
print("Union:",list_union(l1,l2))

# write a program to merge two sorted list into a single sorted list

def merge_sorted_lists(l1,l2):
    merged_list=[]
    i=j=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            merged_list.append(l1[i])
            i+=1
        else:
            merged_list.append(l2[j])
            j+=1
    merged_list.extend(l1[i:])
    merged_list.extend(l2[j:])
    return merged_list
l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
print("Merged sorted list:",merge_sorted_lists(l1,l2))


# find the largest sub array sum of a given list

def largest_subarray_sum(l):
    max_sum=current_sum=l[0]

    for num in l[1:]:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum
l=[-2,1,-3,4,-1,2,1,-5,4]
print("Largest subarray sum:",largest_subarray_sum(l))


# write a program to partition a list around the given value such that all elements less than the given value come before it and all elements greater than the given value come after it  

def partition_list(l,pivot):
    less_than=[x for x in l if x<pivot ]
    equal_to=[x for x in l if x==pivot]
    greater_than=[x for x in l if x>pivot]
    return less_than+equal_to+greater_than
l=[3,1,4,1,5,9,2,6,5]
pivot=4
print("Partitioned list:",partition_list(l,pivot))


# find the peak element in the list of integers.peak element is an element that is greater than or equal to its neighbors

def find_peak_element(nums):
    if not nums:
        return None
    left,right=0,len(nums)-1
    while left<right:
        mid=left+(right-left)//2
        if nums[mid]<nums[mid+1]:
            left=mid+1
        else:
            right=mid
    return left
my_list=[1,2,1,3,5,6,4]
print("Peak element index:",find_peak_element(my_list))

