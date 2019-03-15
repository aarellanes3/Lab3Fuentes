# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:41:01 2019

@author: aarel
"""
#Andres Arellanes CS2302 MW 1:30-2:50pm Dr. Olac Fuentes TA. Anindita Nath
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right
        
    
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T
    

def Search(T,k):
    temp = T
    while temp is not None:
        if temp.item < k:
            T = T.right
        if temp.item > k:
            T = T.left
        if T.item == k:
            print(k, 'found')
        return T
        


def extract(T):
    if T is None:
        return []
    if T is not None:
        small = extract(T.left)
        large = extract(T.right)
        return small + [T.item] + large
 
def depth(T,d):    
    if T is None:
        return None
    if d==0:
        return T.item
    left = depth(T.left,d-1) 
    right = depth(T.right,d-1)
    return left, right


def printbydepth(T,d):
    for i in range(d):
        print("keys at depth ", i ,depth(T,d))
    
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
Search(T,50)
print(extract(T))
printbydepth(T,2)