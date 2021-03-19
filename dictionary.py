# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:15:50 2021

@author: ASUS

Dictionary

"""
a={"name":"adarsh", "age":21, "college":"vvce"}
print(a["name"])
print(a["college"])
a["age"]=23
print(a)
a["college"]="IDPU"
print(a)
a.pop("age")
print(a)
a.popitem()
print(a)
print(a["adarsh"])

