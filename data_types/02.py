# print(dir(list))



# append : ad the element at the end of the list
l1 = [10,20]
l1.append(30) 
l1.append(40) 
print(l1)
 
# Note : apend have 1 behavior

# extend : add the multi element st the end of list
l2=[10,20,30]
l2.extend([100,200,300,400,500])
print(l2)

#Note : extend have 2 behavior



l1=[10,20]
l2=[30,40]
l1.append(l2)
print(l1)


# POP
# pop method will remove element from the end of list
# 2 behavior
l1 = [10,20,30,40,50]
print("see it was deleted", l1.pop())
print(l1)

#pop(index)
l2=[10,20,30,40,50]
l2.pop(2)
print(l2)