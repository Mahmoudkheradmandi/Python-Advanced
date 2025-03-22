
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
    
    
# first = Node(15)
# second = Node(10)
# third = Node(1)

# print(first.data) 
# print(first.next)            

# first.next = second
# second.next = third

# ls = Liink_list()
# ls.head = first

# print(ls.head.data)
# print(ls.head.next.data)
# print(ls.head.next.next.data)

li1 = Liink_list()
li1.push(2) 
li1.push(4) 
li1.push(7) 

li1.append(45)

print(li1)

li1.insert(-5 , 88)
li1.insert(100 , 33)
li1.insert(2 , 90)

print(li1)