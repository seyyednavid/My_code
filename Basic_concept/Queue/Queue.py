
class Queue():

    def __init__ (self,size=5):
        self.queue=[]* size
        self.capacity=size

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
            
        else: self.queue.pop(0)

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
  q=Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  q.dequeue()
  q.dequeue()
  q.enqueue(1)
  q.enqueue(1)
  q.enqueue(1)
  q.enqueue(5)
  q.display()


if __name__ == "__main__":
    main()




