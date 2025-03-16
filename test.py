from random import randint as rnd
import matplotlib.pyplot as plt
from random import shuffle


# length = 100
# _list = [rnd(0 , length) for i in range(length)]

# for i in range(length-1): # 9 *
#     _min = i 
#     for j in range(i + 1 , length): # (n-8) +...+(n-1)
#         if _list[_min] > _list[j] : 
#             _min = j
#     _list[i] ,_list[_min] = _list[_min] , _list[i]
#     plt.bar(range(length),_list)
#     plt.pause(0.005)
#     plt.clf()
# plt.bar(range(length) , _list)
# plt.show()

# ======================================================================

# length = 15
# _list = [rnd(0 , length) for i in range(length)]

# for i in range(length-1): # O(n**2)
#     flag = True
#     for j in range(length - i - 1): 
#         if _list[j] > _list[j+1] : 
#             flag = False
#             _list[j] ,_list[j+1] = _list[j+1] , _list[j]
            
#         plt.bar(range(length),_list)
#         plt.pause(0.05)
#         plt.clf()
#     if flag : 
#         break
# plt.bar(range(length) , _list)
# plt.show()        

# ======================================================================

length = 50
_list = [i for i in range(length)]
shuffle(_list)

for i in range(1 , length): # start poiter in the index 1 no zero 0 range(1 , length)
    for j in range(i): # range 1 == index 0 /// range 2 == index 0 and index 1
        if _list[j] > _list[i]:
            temp = _list[i]
            del _list[i]
            _list.insert(j , temp)
            break
    plt.bar(range(length),_list)
    plt.pause(0.05)
    plt.clf()
plt.bar(range(length) , _list)
plt.show()       