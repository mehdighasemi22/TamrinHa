list = [3, 1, 4, 1, 5]




list.append(9)       #اضاف کردن عدد 9
        #برای ساخت لیست جدا نمیدونم باید چه کرد

list.remove(1)       #عدد 1 را از لیست حذف کن (فقط اولین مورد)

del list[2]      #عنصر سوم را حذف کن (اندیس 2)

list[1] = 100        #5. عنصر دوم را به عدد 100 تغییر بده (اندیس 1)

list.sort(0>20)         # 6. لیست را از کوچک به بزرگ مرتب کن

print(list)

#========================================TAMRINE BADI=====================================

lst = [10, 20, 30, 40, 50, 60, 70]

Taghir1 = lst[1:5]      # 1. از عنصر دوم تا پنجم را استخراج کن (اندیس 1 تا 4)
print("1:", Taghir1)            #که میشه [20, 30, 40, 50]


even_index = lst[::2]           # 2. همه عناصر زوج ایندکس را استخراج کن (اندیس‌های 0, 2, 4, ...)
print("2:", even_index)                #این رو کمک گرفتم


reversed_lst = lst[::-1]           # 3. لیست را برعکس کن
print("3:", reversed_lst)


last_three = lst[-3:]          # 4. یک زیرلیست از آخرین 3 عنصر بساز
print("4:", last_three)                       


#=========================================TAMRINE BADI======================================
import copy

original = [[1, 2], [3, 4]]



copy1 = list(original)        # 1. با استفاده از list() یک کپی از لیست بگیر و نام آن را copy1 بگذار

copy2 = copy.deepcopy(original)         # 2. با استفاده از copy.deepcopy یک کپی دیگر بگیر و نام آن را copy2 بگذار

original[0][0] = 100       # 3. مقدار original[0][0] را به 100 تغییر بده

print("original:", original)
print("copy1   :", copy1)          # 4. خروجی original، copy1 و copy2 را چاپ کن
print("copy2   :", copy2)

#======================================TAMRINE BADI==================================================


lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']


meghdare_apple = lst.count('apple')             # 1. چند بار کلمه 'apple' در لیست آمده است؟
print("1. تعداد 'apple':",meghdare_apple )              


banana_index = lst.index('banana')        #اولین ایندکس 'banana' در لیست کجاست؟
print("2. اولین ایندکس 'banana':", banana_index)


if 'grape' not in lst:
    lst.append('grape')         # 3. اگر 'grape' در لیست نبود، به آن اضافه کن
print("3. لیست نهایی:", lst)


#======================================TAMRINE BADI===================================


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

middle = matrix[1][1]
print("1. عنصر وسط:", middle)    # 1. عنصر وسط ماتریس را چاپ کن (ردیف و ستون با اندیس 1)

second_row = matrix[1]      
print("2. سطر دوم:", second_row)      # 2. سطر دوم را چاپ کن (اندیس 1)

third_column = [row[2] for row in matrix]       # 3. ستون سوم را به صورت یک لیست استخراج کن (اندیس 2)
print("3. ستون سوم:", third_column)

#====================================TAMRINE BADI============================

sentence = "Python is a powerful language"


words = sentence.split()        # 1. کلمات را به صورت یک لیست جدا کن
print("1. لیست کلمات:", words)


reversed_sentence = ' '.join(reversed(words))       # 2. ترتیب کلمات را برعکس کن و به رشته تبدیل کن
print("2. جمله برعکس:", reversed_sentence)
       
long_words = [word for word in words if len(word) > 3]          # 3. فقط کلماتی که طول‌شان بیشتر از 3 حرف است را در یک لیست قرار بده
print("3. کلمات با طول > 3:", long_words)


