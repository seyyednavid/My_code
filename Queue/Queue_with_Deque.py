
from collections import deque

class Queue():

    def __init__ (self,batchSize=5):
        self.queue=deque(maxlen=batchSize)
        self.capacity=batchSize

    # Add an element 
    def enqueue(self , item):
        if self.isFull():
            print('Overflow!! Terminating process.')
            return None
            
        else: self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if self.isEmpty():
            print('Queue UnderFlow!! Terminating process.')
            return None
            
        else: self.queue.popleft()

    # Display  the queue
    def display(self):
        print(self.queue)  
     
    # queue size
    def  size(self):
        return(len(self.queue)) 

    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.size() == 0
 
    # Function to check if the queue is full or not
    def isFull(self):
        return self.size() == self.capacity    

def main() -> None:
    
  q=Queue(10)
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.enqueue(4)
  q.enqueue(5)
  q.enqueue(6)
  q.enqueue(7)
  q.dequeue()
  q.display()

if __name__ == "__main__":
    main()

