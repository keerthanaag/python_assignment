#!/usr/bin/env python
# coding: utf-8

# In[4]:


# INHERITANCE
class Base_class1(object):
    def __init__(self):
        self.str1 = "hi"
        print ("from base_class1")
  
class Base_class2(object):
    def __init__(self):
        self.str2 = "welcome"        
        print ("from Base_class2")
  
class Derived(Base_class1, Base_class2):
    def __init__(self):
        Base_class1.__init__(self)
        Base_class2.__init__(self)
        print ("Derived")
          
    def printStrs(self):
        print(self.str1, self.str2)
         
  
ob = Derived()
ob.printStrs()


# In[8]:


class Company:
    def __init__(self, name, proj):
        self.name = name      #  public
        self._proj = proj     #  protected
    
    # public function 
    def show(self):
        print("The code of the company is = ",self.ccode)

#  child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable
    
    # public function 
    def show_sal(self):
        print("The salary of ",self.name," is ",self.__sal,)

# instance or object
c = Company("Brush Industrie", "Mark 2")
e = Emp("Swathi", 9000, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name," is working on ",e._proj)
e.show_sal()


# In[11]:


#EXCEPTION HANDLING
# value error
#import math
#math.sqrt(-10)
import math

x = int(input('Please enter a positive number:\n'))

try:
    print(f'Square Root of {x} is {math.sqrt(x)}')
except ValueError :
    print(f'You entered {x}, which is not a positive number.')


# In[13]:


#zerodivision error
num_list=[]
total=0
try:
    avg=total/len(num_list)
    print("Average:"+avg)
except ZeroDivisionError:
    print ("Zero Division Error occurred")


# In[17]:


#name error
#prin("indu")
try:
    prin("indu")
except NameError as e:
    print("Name error occured")


# In[21]:


#type error
try:
    a = 100
    b = "10"
    Result = a / b
except TypeError:
    print("type error occured")


# In[26]:


# index error
m = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("The Tuple is:", m)
index = 10
try:
    element = m[index]
    print("Element at index {} is {}".format(index, element))
except IndexError:
    print("Index should be smaller.")


# In[29]:


a = 15.0
b = 0

try:
    result = a / b
except ZeroDivisionError:
    result = "infinity"

print(result)


# In[32]:


# regular expression
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# In[36]:


import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x.start())


# In[39]:


import re

txt = "The34 23r32ain in Spain"
x = re.split("\s", txt)
print(x)


# In[43]:


import re

txt = "The rain in Spain"
x = re.sub("\s", "  ", txt)
print(x)


# In[47]:


# aggregation
import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
print(ser)
print(ser.sum())
print(ser.mean())


# In[50]:


# masking and boolean arrays
import pandas as pd
  
df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                   "B":[5, 2, 54, 3, 2],
                   "C":[20, 16, 7, 3, 8],
                   "D":[14, 3, 17, 2, 6]})

df.mask(df > 10, 1)


# In[ ]:




