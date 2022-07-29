class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

  

class LinkedList:
    def __init__(self):
        self.head = None

         
    #  function display
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


   # Function to insert a new node at the beginning

    def add_begin(self, new_data):
      new_node = Node(new_data)
      new_node.next = self.head
      self.head = new_node

   ## Function to insert a new node at the end

    def add_last(self,new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node


    # Function to insert a new node after a specific node
    def insert_after_item(self,target_data , data):
        temp = self.head
        
        while temp is not None:
            if temp.data == target_data:
                break
            temp = temp.next
        if temp is None:
            print("data not in the list")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node



     # Function to delete a  node at the beginning       
    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next   




     # Function to delete a  node at the end
    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None



     # Function to delete a  specific node
    def delete_element_by_value(self, x):
         if self.head is None:
           print("The list has no element to delete")
           return

            
         if self.head.data == x:
           self.delete_at_start()
           return

         temp = self.head
         while temp.data is not None:
           if temp.next.data == x:
               break
           temp = temp.next

         if temp.next is None:
           print("item not found in the list")
         else:
           temp.next = temp.next.next
           



def main() -> None:
  listt=LinkedList()
  listt.add_begin('a')
  listt.add_begin('b')
  listt.add_begin('c')
  listt.add_last('k')
  listt.insert_after_item('c','w')
  listt.delete_at_start()
  listt.delete_at_end()
  listt.delete_element_by_value('b')
  print(listt)

if __name__ == "__main__":
    main()


      