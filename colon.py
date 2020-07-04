from copy import deepcopy
tuple =("hello", 6 ,[], True)
print(tuple)
tuple_colon = deepcopy(tuple)
tuple_colon[2].append(50)
print(tuple_colon)
print(tuple)
         
