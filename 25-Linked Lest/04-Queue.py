class Node :  
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None
        
class Custom_Queue: 
    def __init__(self):
        self.head = None
        self.front = None
        self.length = 0 
        
    def enqueue(self , data):
        new_node = Node(data)
        if self.head: 
            new_node.next = self.head
            self.head.prev = new_node  # With this command, we can make our list link two-way
            self.head = new_node 
        else:
            self.head = new_node 
            self.front = new_node
            
        self.length += 1      

    def dequeue(self):
        if self.length <= 1: 
            if self.length == 0:
                print('Queue is Empty') 
            else : 
                data = self.front.data
                self.head = None
                self.front = None
                self.length -= 1
                return data          
        else:      
            data = self.front.data
            self.front = self.front.prev
            self.front.next = None
            self.length -= 1
            return data      
        
    def __repr__(self):
        if self.length:
            _str = ''
            temp = self.head
            while temp.next: 
                _str += str(temp.data) + " <--> "
                temp = temp.next
            else: 
                _str += str(temp.data)    
            return _str        
        else: 
            return ""
    
    
qu = Custom_Queue()
qu.enqueue(3)
qu.enqueue(5)

print(qu)
print(qu.dequeue())
print(qu)
print(qu.dequeue())
print(qu)

# print(qu.head.data)   
# print(qu.head.next.data)  
# print(qu.head.next.prev.data)    