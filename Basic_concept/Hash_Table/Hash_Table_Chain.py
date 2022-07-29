class HashTable(object):
    def __init__(self, length=10):
        self.array = [None] * length
        
    
    def hash_function(self, key):
        """Get the **index** of our array for a specific string key"""
        length = len(self.array) 
        return hash(key) % length
        
      
    def add(self, key, value):
       
        #Add a value to our array by its key
        index = self.hash_function(key)
        if self.array[index] is not None:
           
            for kvp in self.array[index]:
                # If key is found, then update,its current value to the new value
                if kvp[0] == key:
                    kvp[1] = value
                    
                    break
            else:
                # append=use chainig
                self.array[index].append([key, value])     
                
        else:
            #append=use chainig
            self.array[index] = []
            self.array[index].append([key, value])          
            
            
    
    def search(self, key):
        """Get a value by key"""
        index = self.hash_function(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return print(kvp[1])
            raise KeyError()                                                       



    def delete(self, key):
        index = self.hash_function(key)
        key_exist=False
        bucket=self.array[index]
        for i,kv in enumerate(bucket):
            k,v=kv
            if key==k:
                key_exist=True
                break
        if key_exist:
            del bucket[i]   
            print ('Key {} deleted'.format(key))
        else:
            print ('Key {} not found'.format(key))
            
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
  h.delete(100)
  h.search(25)
  h.display()


if __name__ == "__main__":
    main()
