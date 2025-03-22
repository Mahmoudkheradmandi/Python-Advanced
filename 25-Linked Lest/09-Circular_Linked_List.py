class Node :  
    def __init__(self , data):
        self.data = data
        self.next = None
        
class Liink_list: 
    def __init__(self):
        self.head = None
        self.length = 0 
        
    def push(self , data): 
        new_node = Node(data)
        if self.head : 
            temp = self.head
            while temp.next != self.head : 
                temp = temp.next
            else: 
                new_node.next = self.head
                self.head = new_node
                temp.next = new_node  
                self.length = 1               
        else : 
            self.head = new_node
            new_node.next = new_node 
            self.length = 1 
            
    def pop(self , index=-1):
        if index == -1 : # In this case, it should delete the last node
            if self.head :
                temp = self.head
                while temp.next.next != self.head : 
                    temp = temp.next
                else: 
                    data = temp.next.data
                    if self.length == 1 :
                        self.head = None
                    else:      
                        temp.next = self.head
                    self.length -= 1
                    return data    
            else: 
               return None
        else: 
            if self.head: 
                temp = self.head
                if index > self.length -1 : 
                    index = self.length - 1
                elif index < 0: 
                    temp = self.head
                    while temp.next != self.head :  
                        temp = temp.next
                    else: 
                        data = self.head.data 
                        temp.next = self.head.next
                        self.head = self.head.next
                        return data          
                index -=1 
                while index : 
                    temp = temp.next
                    index -= 1
                else :     
                    data = temp.next.data
                    temp.next = temp.next.next
                    self.length += 1 
                    return data 
            else: 
                return None       
       
            
    def __repr__(self):
        
        _str = ''
        if self.head:
            temp = self.head
            while temp.next != self.head : 
                _str += str(temp.data) + " --> "
                temp = temp.next
            else: 
                _str += str(temp.data) + " --> [loop] "    
        return _str        
       
        
        
ll = Liink_list()
ll.push(2)
ll.push(5)
ll.push(8)
print(ll)
# print(ll.pop())
# print(ll.pop(1))
# print(ll)
print(ll.pop(1))
print(ll)        