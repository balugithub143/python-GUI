from functools import reduce

l = [2, 4, 7, 3 , 12 , 14 ,13 , 84 , 90 ,5 ,6]

filter_object = filter(lambda s: s%2==0, l)

map_object = map(lambda s :s+8 ,filter_object)

s=reduce(lambda x,y:x+y ,map_object )
print("addition of list =",s)