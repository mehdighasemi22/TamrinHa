import copy

original = [[1, 2], [3, 4]]

shallow = list(original)

deep = copy.deepcopy(original)

original[0][0] = 100

print("original:", original)
print("shallow :", shallow)
print("deep    :", deep)

#===================================tamrine_badi=======================================


my_tuple = ('apple', 'banana', 'cherry')

print(my_tuple.index('banana'))  

print(my_tuple.count('apple'))   # agar do barabar shod , apple neshon mide


#===================================tamrine_badi=======================================

# unpacke sadi
person = ("Ali", 25, "Programmer")
name, age, job = person
print(name, age, job)

# unpack ba *
data = (1, 2, 3, 4, 5)
first, *middle, last = data     
print("first:", first)      # first = 1 __ middle = 2,3,4 __ last = 5
print("middle:", middle)    # "وقتی از * استفاده می‌کنی، یعنی "بقیه مقدارها رو بریز داخل این متغیر به صورت لیست
print("last:", last)

# مشق 9: آن‌پک با وایلدکارت _
student = ("Sara", 17, "A+", "Excellent behavior")
name, age, *_ = student
print("name:", name)
print("age:", age)
