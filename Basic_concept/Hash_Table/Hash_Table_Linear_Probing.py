class HashTable(object):
    def __init__(self, length=10):
        self.array = [None] * length
        
    
    def hash_function(self, key):
        """Get the **index** of our array for a specific string key"""
        length = len(self.array) 
        index=hash(key) % length
        if self.array[index] == None :
            return index
        else :
            
            # Implementing linear probing
            while self.array[index] != None :
                index = (index+1)%10
                
            return index
        
        
    def add(self, key, value):
        #Add a value to our array by its key
        index = self.hash_function(key)
        self.array[index]=key
       
    
    def search(self, key):
        """Get a value by key"""
        index = key%len(self.array)
        

        if self.array[index] != key :
            while self.array[index] != key and self.array[index] != None :
                index = (index+1)%10
                
        if self.array[index] == key :
            return index
        else :
            return None                                                    



    def delete(self, key):
        index = key%len(self.array)
       

        if self.array[index] != key :
            while self.array[index] != key and self.array[index] != None :
                index = (index+1)%10
                
        if self.array[index] == key :
            del self.array[index]
        else :
            return None    
        
    def display(self):
        print(self.array)

                
def main() -> None:
  h= HashTable()
  h.add(25,'usa')
  h.add(27,'EN')
  h.add(10,'IR')
  h.add(100,'NETH')
  h.add(200,'us')
  h.add(300,'us')
  h.delete(300)
  print(h.search(300))
  h.display()

if __name__ == "__main__":
    main()

