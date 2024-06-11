my_tuple=(1,2,3)
another_tuple=tuple([4,5,6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
combined_tuple=my_tuple+another_tuple
print(combined_tuple)
repeated_tuple=my_tuple*3
print(repeated_tuple)
print(2 in my_tuple)
print(4 not in my_tuple)
print(len(my_tuple))
for item in my_tuple:
    print(item)
string_to_tuple=tuple("hello")
print(string_to_tuple)
list_to_tuple=tuple([1,2,3])
print(list_to_tuple)
print(my_tuple.count(2))
print(my_tuple.index(3))


#SORT 
tuple_of_integers=(5,2,8,1,3)
sorted_tuple=tuple(sorted(tuple_of_integers))
print("Sorted tuple:",sorted_tuple)

tuple_of_tuples=((1,'apple'),(3,'orange'),(2,'banana'))
sorted_tuples=sorted(tuple_of_tuples,key=lambda x:x[1])
print("Sorted tuples:",sorted_tuples)


# Tuple Comprehension
squares_tuple=tuple(x**2 for x in range(1,6))
print("Squares tuple:",squares_tuple)

# Zip two tuples
l1=[1,2,3]
l2=['a','b','c']
zipped_tuple=tuple(zip(l1,l2))
print("Zipped tuple:",zipped_tuple)


# Distance bw two points
from collections import namedtuple
import math
Point=namedtuple('Point',['x','y'])
point1=Point(1,2)
point2=Point(4,6)
distance=math.sqrt((point2.x-point1.x)**2+(point2.y-point1.y)**2)
print("Distance between point1 aand point2:",distance)


# Filter
original_tuple=(1,2,3,4,5)
filtered_tuple=tuple(filter(lambda x:x%2==0,original_tuple))
print("Filtered tuple:",filtered_tuple)


# Add
from functools import reduce
def add(x,y):
    return x+y
original_tuple=(1,2,3,4,5)
result=reduce(add,original_tuple)
print("Result of reducing the tuple:",result)
