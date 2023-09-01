    
class Node:
    def __init__(self, data):
        self.data = data
        self.prev:Node = None 
        self.next:Node = None
        
class LinkedList:
    def __init__(self):
        self.head:Node = None
        self.tale:Node = None
        
    def is_empty(self) -> bool:
        return self.head is None
    
    def prepend(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tale = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tale = new_node
            
        else:
            self.tale.next = new_node
            new_node.prev = self.tale
            self.tale = new_node
            
    def insert_after(self, target_data, data):
        new_node = Node(data)
        x = self.head
        while x:
            if x.data == target_data: 
                if x == self.tale:
                    self.append(data)
                    return
                new_node.prev = x
                new_node.next = x.next
                x.next = new_node
                new_node.next.prev = new_node
                return 
            x = x.next    
               
        print(f"{target_data} data not found") 
              
               
    def insert_before(self, target_data, data):
        new_node = Node(data)
        x = self.head
        while x:
            if x.data == target_data: 
                if x == self.head:
                    self.prepend(data)
                    return
                    
                new_node.next = x
                new_node.prev = x.prev
                x.prev.next = new_node
                x.prev = new_node
                return
            x = x.next
        print(f"{target_data} data not found") 
    
    
    def delete(self, data):
        x = self.head
        while x:
            if x.data == data:
                if x == self.head:
                    self.head = x.next
                    x.next.prev = None
                    return
                elif x == self.tale:
                    self.tale = x.prev
                    x.prev.next = None
                    return
                        
                x.prev.next = x.next
                x.next.prev = x.prev
                x.prev = x.next = None
                return
            
            x = x.next
        print(f"{data} data not found")
        
    def display(self):
        x = self.head
        while x:
            print(x.data, end= " ")
            
            x = x.next
        print()    
            
lst = LinkedList()
print(lst.is_empty())
lst.append("Flash")
lst.prepend("SPS") 
lst.append("Premium")
lst.insert_after("Premium","Lakot") 
lst.insert_before("SPS","Qolej")
lst.display()
lst.delete("Lakot")       
lst.display()
lst.delete("Qolej")       
lst.display()  
print(lst.is_empty())