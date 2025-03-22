
class TreeNode: 
    def __init__(self , data):
        self.data = data 
        self.children = []
        self.parent = None
    
    def get_level(self): 
        level = 0
        p = self.parent
        while p : 
            level += 1 
            p = p.parent
        return level        
    
    def add_child(self , child): 
        self.children.append(child)
        child.parent = self
        
    
    def print_tree(self): 
        spaces = "  "* self.get_level() 
        prefix = spaces + '|__' if self.parent else '|--'
        print(prefix,self.data)
        for child in self.children: 
            child.print_tree() 
    
    def search_child(self ,key):
        if self.data == key: 
            return True
        else: 
            for child in self.children: 
                found = child.search_child(key)
                if found: 
                    return True
        return False         
                   

def create_tree():
     
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    root.add_child(laptop)
    laptop.add_child(TreeNode('DELL'))
    laptop.add_child(TreeNode('ASUS'))
    laptop.add_child(TreeNode('MSI'))
    laptop.add_child(TreeNode('APPLE'))
    
    phone = TreeNode('phone')
    root.add_child(phone)
    phone.add_child(TreeNode('SAMSUNG'))
    phone.add_child(TreeNode('APPLE'))
    phone.add_child(TreeNode('LG'))    
    
    tv = TreeNode('tv')
    root.add_child(tv)
    tv.add_child(TreeNode('LG')) 
    tv.add_child(TreeNode('SONY')) 
    
    
    
    
    
    return root
        
if __name__ == '__main__' : 
    
    root = create_tree()
    # root.print_tree()
    print(root.search_child('MSI'))
    
    
    
     