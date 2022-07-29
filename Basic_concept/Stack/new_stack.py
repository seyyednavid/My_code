# implement stack with deque

from collections import deque


class stack(object):

    def __init__ (self, batchsize: int = 10) -> None:
        # 10 is the default capacity
        
        self.stack = deque(maxlen = batchsize)
        self.capacity= batchsize
        self.size: int = 0

    
    def push(self, item) -> None:
        #Add item to top of stack
        
        if not item:
           raise ValueError("Item value of None provided")
          
        
        if self.isFull():
            raise MemoryError("Overflow!! Terminating process.")
        else: 
            self.stack.append(item)
            self.size += 1
        

    
    def pop(self) -> int:
        # return and Remove item in top of stack, return None if the stack is empty
        
        if self.isEmpty():
           return None
            
        else: 
            self.size -= 1
            return self.stack.pop()
        
        
    
    def display(self) -> list:
        # Display  the stack
        
        print(self.stack)  
     
    
    def capacity(self) -> int:
        # stack capacity
        
        return (len(self.stack))

    
    def isEmpty(self) -> bool:
        # Function to check if the stack is empty or not
        
        return self.size == 0
 
  
    def isFull(self) -> bool:
        # Function to check if the stack is full or not
        return self.size == self.capacity
    
   
 





        