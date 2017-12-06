#!/bin/python

import sys
class stack_:
    def __init__(self):
        self.sta = []
        self.top = -1
        
    def peek(self):
        if self.top >= 0: 
            return self.sta[self.top]
        else: 
            return -99
        
    def pop(self):
        if self.top >= 0: 
            temp = self.sta.pop()
            self.top -= 1
            return temp
        else: return -99
        
    def push(self, s):
        self.sta.append(s)
        self.top += 1
        
    def show(self):
        return ''.join(self.sta[:])
        

def super_reduced_string(s):
    stck = stack_()
    for c in s:
        if stck.peek() == c: 
            stck.pop()
        else: 
            stck.push(c)
            
    temp = stck.show()
    if temp == '': 
        return 'Empty String'
    else: 
        return temp

def main():
    s = raw_input().strip()
    result = super_reduced_string(s)
    print(result)
    
if __name__ == '__main__':
    main()
