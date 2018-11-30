"""
List of List Iterator
Given an array of arrays, implement an iterator class to allow the client to traverse and remove elements in the array list.

This iterator should provide three public class member functions:
boolean hasNext() return true if there is another element in the set
int next() return the value of the next element in the array
void remove() remove the last element returned by the iterator. That is, remove the element that the previous next() returned. 
This method can be called only once per call to next(), otherwise an exception will be thrown.
"""

###Flatten the array
class Vector2D():
    def __init__(self,vec2d):
        self.stack = vec2d
        self.cur = 0
        self.call_next = False
        
    def hasNext(self):
        if not self.stack or self.cur == len(self.stack):
            return False
        f = self.stack[self.cur]
        while isinstance(f,list):
            self.stack = self.stack[:self.cur] + f + self.stack[self.cur+1:]
            f = self.stack[self.cur]
        return True
        
    def next(self):
        if self.hasNext():
            value = self.stack[self.cur]
            self.call_next = True
            self.cur += 1
            return value
        self.call_next = False
        return None
        
    def remove(self):
        if not self.call_next:
            raise Exception('Call next() first.')
        self.cur -= 1
        self.stack.pop(self.cur)
        self.call_next = False



class Vector2D():
    def __init__(self,vec2d):
        self.stack = vec2d
        self.row = 0
        self.col = 0
        self.call_next = False
        
    def hasNext(self):
        while self.row < len(self.stack):
            if self.col < len(self.stack[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False
        
    def next(self):
        value = self.stack[self.row][self.col]
        self.col += 1
        if self.col >= len(self.stack[self.row]):
            self.col = 0
            self.row += 1
        self.call_next = True
        return value
        
    def remove(self):
        if not self.call_next:
            raise Exception('Call next() first.')
        row,col = self.row,self.col
        if col == 0:
            row -= 1
            self.stack[row].pop()
        else:
            self.stack[row].pop(col-1)
            self.col -= 1
        if self.stack[row] == []:
            self.stack.pop(row)
            self.row -= 1 
        self.call_next = False
        
