
class Node :  # this class for create node
    def __init__(self , data):
        self.data = data
        self.next = None
        
class Liink_list: 
    def __init__(self):
        self.head = None
        self.length = 0 
        
    def push(self , data): 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1      
    
    def append(self , data):
        new_node = Node(data)
        temp = self.head
        while temp.next: 
            temp = temp.next
        else: 
            temp.next = new_node    
        self.length += 1
        
    def insert(self , index , data): 
        if index <= 0: 
            self.push(data)
        elif index >= self.length - 1: 
            self.append(data)
        else: 
            temp = pre = self.head
            while index: 
                pre = temp
                temp = temp.next
                index -= 1
            else: 
                new_node = Node(data)
                new_node.next = temp
                pre.next = new_node
                self.length += 1    
    
    def pop(self , index=-1):
        if index == -1 : # In this case, it should delete the last node
            temp = self.head
            while temp.next.next: 
                temp = temp.next
            data = temp.next.data     
            temp.next = None
            self.length += 1     
            return data
        elif index == 0 : 
            data = self.head.data
            self.head = self.head.next
            self.length += 1 
            return data
        else:
            temp = self.head
            index -=1 
            while index : 
                temp = temp.next
                index -= 1
            data = temp.next.data
            temp.next = temp.next.next
            self.length += 1 
            return data 
            
    def setter(self , lst : list):
        for i in lst[::-1]:
            self.push(i)
            
              
                         
            
    def __len__(self): 
        return self.length
    
    def isempty(self): 
        return self.length == 0
    
    def __repr__(self):
        _str = ''
        temp = self.head
        while temp.next: 
            _str += str(temp.data) + " --> "
            temp = temp.next
        else: 
            _str += str(temp.data)    
        return _str
    
    
lst = [1,2,3]
li1 = Liink_list()
li1.push(2) 
li1.push(14) 
li1.push(7)
# li1.push(10)
# li1.push(1)
# li1.push(15)     
print(li1)
li1.setter(lst)
# print(li1.pop())
# print(li1.pop(2))
# print(li1.pop(0))
print(li1)