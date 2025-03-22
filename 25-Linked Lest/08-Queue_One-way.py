class Node :  
    def __init__(self , data):
        self.data = data
        self.next = None
        
class Queue_Alg: 
    def __init__(self):
        self.head = None
        self.first = None
        self.length = 0 
        
    def enqueue(self , data):
        new_node = Node(data)
        if self.head == None:             
            self.head = new_node 
            self.first = new_node
            self.length = 1
        else:
            self.first.next = new_node
            self.first = new_node    
        self.length += 1      

    def dequeue(self):
        data = None
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
        return data   
             
        
    def __repr__(self):
        if self.length:
            _str = ''
            temp = self.head
            while temp.next: 
                _str += str(temp.data) + " --> "
                temp = temp.next
            else: 
                _str += str(temp.data)    
            return _str        
        else: 
            return ""
        
        
        
qu =  Queue_Alg()
qu.enqueue(6)
qu.enqueue(4)
qu.enqueue(9)

print(qu)       
print(qu.dequeue())
print(qu.dequeue())
print(qu)       
       