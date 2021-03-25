# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 00:51:11 2021

@author: shiuli Subhra Ghosh : Roll No- MDS202035
"""

class Doublenode:
    def __init__(self, data = None):
        self.value = data 
        self.next = None
        self.prev = None 
    
class Deque:
    def __init__(self, l = []):
        self.head = None # Initially there are no elements 
        self.tail = None
        for i in l:
            new_node = Doublenode(i)
            if self.tail == None:
                self.head = new_node
                self.tail = new_node

            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                
        
    def insert_front(self, v):
        new_node = Doublenode(v)
        
        
        # If the list is empty 
        if self.head == None: 
            self.head = new_node
            self.tail = new_node
            return 
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
        
    def insert_rear(self,v):
        new_node = Doublenode(v)
        
        # If the list is empty 
        if self.tail == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

            
    def delete_front(self):
        if self.head == None:
            raise IndexError("Sorry, The Deque is Empty")
        else:
            temp = self.head
            if temp.next != None :
                temp.next.prev = None
                self.head = temp.next 
                temp.next = None
                return(temp.value)
            else:
                self.head = None
                self.tail = None
                return(temp.value)
        
    def delete_rear(self):
        if self.tail == None:
            raise IndexError("Sorry, The Deque is Empty")
        else:
            temp = self.tail 
            if temp.prev != None:
                temp.prev.next = None
                self.tail = temp.prev
                temp.prev = None
                return(temp.value)
            else:
                self.head = None
                self.tail = None
                return(temp.value)      
        
        
    def __str__(self):
        selflist = []
        if self.head == None:   # If it is empty list 
            return(str(selflist))
        temp = self.head
        selflist.append(temp.value) # append the current value of the list 
        
        while temp.next != None:
            temp = temp.next 
            selflist.append(temp.value)
        return(str(selflist))
         