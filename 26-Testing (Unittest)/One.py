from random import randint as rnd

def add(x , y): 
    return x + y

def mul(x , y): 
    return x * y 

def divid(x , y): 
    if y == 0: 
        raise ValueError('Can not divide by zero !')
    return x / y

def init_pop(n , m): 
    population_list = [[rnd(0 , n-1) for i in range(n)] for i in range(m)]
    return population_list