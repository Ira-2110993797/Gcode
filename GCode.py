#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

if __name__=="__main__":
    if len(sys.argv)!= 2:
        print("Usage: python.model.py <name>")
        sys.exit(1)
        
    name=sys.argv[1]
    print(f"{name}, welcome to docker!")

