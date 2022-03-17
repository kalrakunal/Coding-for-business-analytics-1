#!/usr/bin/env python
# coding: utf-8

# In[9]:


#In this program, two group of integers are to be inputted and then intersected for common integer in the groups
#First, two groups will be entered by the user in g1 and g2 groups using list comprehension
g1_list = list(int(g1) for g1 in input("Enter number group 1: ").strip().split())
g2_list = list(int(g2) for g2 in input("Enter number group 2: ").strip().split())
#In this, split function is used for the separator for required  format
#Now, for intersecting the two lists and find common number, list comprehension concept has been used
if __name__ == '__main__':
    common_list = [c for c in g1_list if c in g2_list]
    print(*common_list, sep=" ")


# In[ ]:




