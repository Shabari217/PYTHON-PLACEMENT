thisList=["orange","mango","kiwi","pineapple","banana"]
thisList.sort(reverse=True)
print(thisList)

thisList=["orange","mango","kiwi","pineapple","banana"]
thisList.sort()
print(thisList)

thisList=[100,50,65,82,23]
thisList.sort(reverse=True)
print(thisList)

thisList=[100,50,65,82,23]
thisList.sort()
print(thisList)

# sort based on how close a number is to 50
# customised sort
def fun(n):
    return abs(n-50)

thisList=[100,50,65,82,90,23]
thisList.sort(key=fun)
print(thisList)

#case insensitive
thisList=["banana","Orange","Kiwi","cherry"]
thisList.sort(key=str.lower)
print(thisList)

