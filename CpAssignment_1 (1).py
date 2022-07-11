#!/usr/bin/env python
# coding: utf-8

#  #                                                        ASSIGNMENT -1 
# PROGRAMMING IN PYTHON

# ## PROGRAMMING QUESTIONS LEVEL-1

# 11) pattern:

# In[7]:


n = 6
for i in range(n):
    for j in range(i):
        print(" * ",end ="")
    print(" ")


# 12) Write a program to remove characters from a string starting from zero up to n and return a new string.

# In[126]:


str_old = str(input("Enter string values: "))
n = int(input("Enter the position of the string to remove: "))
new_str = str_old[:(n-1)] + str_old[n:]
print ("The string after removal of nth character : " + new_str)


# 13) Iterate the given list of numbers and print only those numbers which are divisible by 5

# In[24]:


lst = [1,38,26,35,20,37,48,25,18,35,25,30,40,55,51,35,85,90]
l = len(lst)
for i in range(l):
    if(lst[i] %5 == 0 ):
        print(lst[i],end=" ")
    


# 14) Write a program to find how many times substring “Hi” appears in the given string.

# In[27]:


strng = "Hi is used as a friendly greeting.Hi, this is keerthanaa.Hi there,How was the flight,Hi,hi,Hi,Hi?"
output = strng.count("Hi")
print(output)


# 15) pattern

# In[6]:


n = 6
for i in range(n):
    for j in range(i):
        print(i,end =" ")
    print(" ")


# 9) check if the number is an Armstrong number or not

# In[129]:


n = int(input("Enter a value: "))
sum = 0
temp = n
while temp>0:
 digit = temp % 10
 sum += digit **3
 temp //= 10
if sum == n:
 print("The number is armstrong number")
else:
 print("It is not a armstrong number")


# # List Exercises

# 17) Python program to interchange first and last elements in a list

# In[34]:


lst = [2.34,"hello",23,"d0ll@r"]
temp = lst[0]
lst[0] = lst[-1] #the last element can be indicated as -1.
lst[-1]=temp
print(lst)


# 18) Python program to swap two elements in a list

# In[37]:


position_1 = int(input("Enter the position of the element you want to swap from:"))
position_2 = int(input("Enter the position of the element you want to swap to:"))
lst = [2,43,19,46,29,40,59,69]
temp_variable=lst[position_1 -1]
lst[position_1 -1] = lst[position_2 -1]
lst[position_2 -1] = temp_variable
print("The new list is",lst)


# 19) Python | Ways to find length of list

# In[39]:


given_list= ['d0ll@r',"mama",20,2+7j,"gojo satarou",'hello', 23+21j, 2.34]
length = len(given_list)
print("Length of the list is: ",length)


# In[41]:


given_list= ['d0ll@r',"mama",20,2+7j,"gojo satarou",'hello', 23+21j, 2.34]
count= 0
for i in given_list:
    count = count + 1
print("Length of the list is: ",count)    


# 20) Maximum of two numbers in Python

# In[42]:


lst = [2,43,19,46,29,40,59,69]
max(lst)


# 21) Minimum of two numbers in Python

# In[43]:


lst = [2,43,19,46,29,40,59,69]
min(lst)


# # String Exercises

# 22) Python program to check whether the string is Symmetrical or Palindrome

# In[109]:


#palindrome
def palindrome(a):
    mid = (len(a)-1)//2
    first = 0      
    last = len(a)-1
    flag = 0

    while(first <= mid):
        if (a[first]== a[last]):
            first += 1
            last -= 1
        else:
            flag = 1
            break;
    if (flag == 0):
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
#symmetry
def symmetry(a):
     
    n = len(a)
    flag = 0
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
         
    start_1 = 0
    start_2 = mid
     
    while(start_1 < mid and start_2 < n):
         
        if (a[start_1]== a[start_2]):
            start_1 = start_1 + 1
            start_2 = start_2 + 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
strng = 'ammaamma'
palindrome(strng)
symmetry(strng)


# 23) Reverse words in a given String in Python

# In[51]:


strng ="Levi Ackerman"
reverse =strng[::-1]
print(reverse)


# 24) Ways to remove i’th character from string in Python

# In[58]:


strng ="This is Gojo Satarou"
strng.replace('i','a')


# # Tuple Exercises

# 27) Python program to Find the size of a Tuple

# In[73]:


import sys as s
exmple_tuple= ("Levi Ackerman",36,"Gojo Satarou",30,"eren yeager","kaneki ken",57+9j)
size = s.getsizeof(exmple_tuple)
print("the size is:",size)


# 28) Python – Maximum and Minimum K elements in Tuple

# In[69]:


ex_tuple = (1,38,26,35,20,37,48,25,18,35,25,30,40,55,51,35,85,90)
print("The maximum element in tuple is:",max(ex_tuple))
print("The minimum element in tuple is:",min(ex_tuple))


# 29) Python – Sum of tuple elements

# In[72]:


import numpy as np
ex_tuple = (1,38,26,35,20,37,48,25,18,35,25,30,40,55,51,35,85,90)
sum = np.sum(ex_tuple)
print("Sum of tuple elements is ",sum)    


# # Dictionary Exercises

# 32) Python | Sort Python Dictionaries by Key or Value

# In[121]:


def dictionary():
 
 key = {}
 key[2] = 21
 key[10] = 69
 key[7] = 71
 key[3] = 143
 key[1] = 18
 print("key:", key)
 print("keys and values sorted ")
 
 for i in sorted(key):
    print((i, key[i]), end=" ")
def main():
 dictionary()
if __name__ == "__main__":
 main()


# 33) Python dictionary with keys having multiple inputs

# In[120]:


my_dict = {}
l, m, n = 69, 71, 143
my_dict[l, m, n] = l + m - n
a, b, c = 52, 54, 11
my_dict[a, b, c] = a + b - c
print("The dictionary are :")
print(my_dict)


# # Set Exercises
# 

# 36)Find the size of a Set in Python

# In[82]:


import sys as s
exmple_set= {"Levi Ackerman",36,"Gojo Satarou",30,"eren yeager","kaneki ken",57+9j}
size = s.getsizeof(exmple_set)
print("the size is:",size)


# 37)Iterate over a set in Python

# In[91]:


exm_set = {"Levi Ackerman",36,"Gojo Satarou",30,"eren yeager",18}
for i in exm_set:
    print(i)


# # Matrix Exercises

# 41)Python – Assigning Subsequent Rows to Matrix first row elements

# In[113]:


gn_list = [[5, 3, 9], [1, 0, 8], [0, 5, 8], [8, 1, 2]]
res = {gn_list[0][ele] :  gn_list[ele + 1] for ele in range(len(gn_list) - 1)}
print("The New Matrix : " + str(res))


# 42)Adding and Subtracting Matrices in Python

# In[95]:


#addition
import numpy as n
ar_1= n.array([[10, 67], [83, 45]])
ar_2= n.array([[48, 53], [67, 75]])
print("Addition of two matrix is ")
print(n.add(ar_1,ar_2))


# In[97]:


#subraction
import numpy as n
ar_1= n.array([[10, 67], [83, 45]])
ar_2= n.array([[48, 53], [67, 75]])
print("Addition of two matrix is ")
print(n.subtract(ar_1,ar_2))


# # Functions Exercises

# 46)How to get list of parameters name from a function in Python?

# In[80]:


# this code is for finding the length of a string which uses len a built in function
#so,on how to get the list of parameters name from a function in Python.You just have to press(shift + tab) key
strng = "HARRY STYLES"
#len(#shift + tab)
len(strng)


# In[77]:


import inspect  
print(inspect.signature(len))


# 47)How to Print Multiple Arguments in Python?

# In[105]:


def greetings_func(name,greetings):
    print('happy new year {} !,I wish you {}'.format(name , greetings))
name = 'Surya'
greetings ='well'
greetings_func(name,greetings)

