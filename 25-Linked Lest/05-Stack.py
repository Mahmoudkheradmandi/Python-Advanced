
class Node :  
    def __init__(self , data):
        self.data = data
        self.next = None
        
class Custom_Stack: 
    def __init__(self):
        self.head = None
        self.length = 0 
        
    def push(self , data):
        new_node = Node(data)
        if self.head: 
            new_node.next = self.head
            self.head = new_node
                 
        else: 
            self.head = new_node   
        self.length += 1
        
    def pop(self):
        data = None
        if self.head: 
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
        return data   

    def __repr__(self):
        _str = ''
        if self.head:
            temp = self.head
            while temp.next: 
                _str += str(temp.data) + " --> "
                temp = temp.next
            else: 
                _str += str(temp.data)    
            return _str
        else: 
            return ""
            
    
    
sk = Custom_Stack()
sk.push(5)
sk.push(3)
sk.push(9)
print(sk)

print(sk.pop())  
print(sk)  