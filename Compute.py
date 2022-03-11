#!/usr/bin/env python
# coding: utf-8

# In[13]:


#In this program, a class is to be defined in which a list of dictionaries to be inputted and then computed
#So, first a class named as shapes is been defined
class shapes:
#Now a list named as data is cretaed in which set of dictionaries are defined with the values
    data = [ {"type": "Square", "area": 150.5},
             {"type": "Rectangle", "area": 80},
             {"type": "Rectangle", "area": 660},
             {"type": "Cicle", "area": 68.2},
             {"type": "Triangle", "area": 20}  ]
#Now, after creating list of dictionaries, all are to printed in the sentence format
#So, oops concepts are used for calling the class and inside object and then is printed
print("1 -", (shapes.data[0]["type"]), "with area size" ,(shapes.data[0]["area"]))
print("2 -", (shapes.data[1]["type"]), "with area size" ,(shapes.data[1]["area"]))
print("3 -", (shapes.data[2]["type"]), "with area size" ,(shapes.data[2]["area"]))
print("4 -", (shapes.data[3]["type"]), "with area size" ,(shapes.data[3]["area"]))
print("5 -", (shapes.data[4]["type"]), "with area size" ,(shapes.data[4]["area"]))


# In[ ]:




