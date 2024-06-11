# Creating a tuple
def create_tuples():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ('a', 'b', 'c', 'd', 'e')
    tuple3 = ("apple", "banana", "cherry")
    return tuple1, tuple2, tuple3

# Accessing tuples
def access_tuple_items(tuple1, tuple2):
    print("Tuple 1:", tuple1)
    print("First element of tuple 1:", tuple1[0])
    print("Last element of tuple 1:", tuple1[-1])
    print("Tuple 2:", tuple2)
    print("Second element of tuple 2:", tuple2[1])
    print("Second last element of tuple 2:", tuple2[-2])
    print(tuple1[0:5])

# Unpacking tuples
def unpacking_tuple1(tuple3):
    (green, yellow, red) = tuple3
    print(green)
    print(yellow)
    print(red)

# Unpacking of tuples using asterisk
def unpacking_tuple2(fruits):
    (green, yellow, *rest) = fruits
    print(green)
    print(yellow)
    print(rest)

def change_tuples(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    list1.append(6)
    list2.remove('c')
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    return tuple1, tuple2

def loop_through_tuple(tuple1):
    print("Looping through tuple 1 using for loop:")
    for item in tuple1:
        print(item)
    print("\nLooping through tuple 1 using while loop and index numbers:")
    index = 0
    while index < len(tuple1):
        print(tuple1[index])
        index += 1

# Joining tuples
def join_tuples(tuple1, tuple2):
    tuple3 = tuple1 + tuple2
    return tuple3

# MAIN PROGRAM
tuple1, tuple2, tuple3 = create_tuples()
access_tuple_items(tuple1, tuple2)
print()

unpacking_tuple1(tuple3)
print()

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
unpacking_tuple2(fruits)
print()

tuple1, tuple2 = change_tuples(tuple1, tuple2)
print("After making changes:")
access_tuple_items(tuple1, tuple2)
print()

tuple3 = join_tuples(tuple1, tuple2)
print("Joined tuple:", tuple3)
print()

loop_through_tuple(tuple1)
