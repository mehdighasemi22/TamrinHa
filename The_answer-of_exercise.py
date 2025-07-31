# list


# Create a list of numbers from 1 to 10.
list = [1,2,3,4,5,6,7,8,9,10]
print (list)
# Add the number 11 to the list using append.
list.append (11)
print(list)
# Insert the number 0 at the beginning of the list.
list.insert (0,0)
                       # insert hamishe 2 ta arguments mikhad
print(list)
# Remove the number 5 from the list using remove.
list.remove (4)
print (list)
# Find the index of the number 7 in the list.
# list.index =====> NEMISHE
print(list.index(7))
# Count how many times the number 3 appears in the list.
# list.count(3) =====> NEMISHE
print(list.count(3))
# Sort the list in descending order.
list.sort(reverse=True)
print(list)
# Reverse the list.
list.reverse
print(list)
# Create a new list by copying the current list and add the number 100 to it.
new_list = list.copy()
new_list.append(100)
print(new_list)
# Clear all elements from the copied list.
new_list.clear()
print(new_list)
#================================================================
# Tuple


# Create a tuple with mixed data types and print its length.
my_tuple = (10, "hello", 3.14, True)
print(len(my_tuple))
# Count the number of times a specific value appears in a tuple.
print(my_tuple.count(2))
# Find the index of a specific value in a tuple.
my_tuple = ('apple', 'banana', 'cherry', 'banana')
print(my_tuple.index('banana'))
# Convert a list to a tuple and sort it.=========> in ro natonestam anjam bedam

# Unpack a tuple into individual variables.========> in ro ham hamintor

#========================================================================
# dictionary


# Create a dictionary of student names and grades. Add, update, and delete an entry.
students = {"Ali": 90,"Sara": 85,"Reza": 78}
students["Mina"] = 88
students["Kasra"] = 92
del students["Reza"]
print(students)
# Write a function that counts the frequency of each character in a string using a dictionary.=========>in ro ham natonestam anjambedam :(
# Merge two dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2) 

print(dict1)
# Print all keys and values in a dictionary.
my_dict = {'name': 'Ali', 'age': 25, 'city': 'Tehran'}
print(my_dict.keys())
print(my_dict.values())
# Check if a key exists in a dictionary.=======> to consol bayad bezanim cd (change directory)???
#=====================================================================
# Set


# Create a set from a list with duplicate values and print it.
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)
# Find the union, intersection, and difference of two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
    # | = union
union_set = set1 | set2
print(union_set)
# Check if one set is a subset/superset of another.=====>in ro natonestam anjam bedam

# Add and remove elements from a set.
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(3)
print(my_set)
# Find elements that are in one set but not both. 
a = {1, 2, 3}
b = {3, 4, 5}
            #بهش میگن تفاوت متغارن (Symmetric )
result = a ^ b
print(result)
#========================================================================
# Frozenset


# Create a frozenset from a list.
my_list = [1, 2, 3, 2, 1]
my_frozenset = frozenset(my_list)
print(my_frozenset)
# Find the intersection and difference between two frozensets.
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print(a & b)#===> اشتراک دو مجموعه
print(a - b)#===> تفاضل (عضوهایی که فقط در مجموعه اول هست)
# Check if an element is in a frozenset.

# Use a frozenset as a key in a dictionary.

# Compare a set and a frozenset for equality.