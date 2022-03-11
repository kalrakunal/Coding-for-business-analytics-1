#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#In this program, two group of integers are to be inputted and then intersected for common integer in the groups
#First, two groups will be entered by the user in g1 and g2 groups
g1 =(input("Enter number group 1: "))
g2 =(input("Enter number group 2: "))
#Then, both groups will be slitted with whitespace using the split function
x = ((g1.split()))
y = ((g2.split()))
#After that, set function is used for storing multiple variables in a single object and both groups are compared for common numbers
x_set = set(x)
y_set = set(y)
#Now, if-else function is used for the computation
#In this, if there will be common numbers, it will be printed as list and if not, then a message will be shown
if (x_set & y_set):
    a = list(x_set & y_set)
    print(*a)
else:
    print("No common elements")


# In[ ]:





# In[ ]:




