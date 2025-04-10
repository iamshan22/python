l5 =[10,20,30,40,50,10,10,40,60]
print(l5[3:7:1]) 
print(l5[1:8:3]) 


# task 2 (Concatenating list objects):Create two lists and add it (control statement and function ,lambda function or advance function ,comprehension)
l1 = [10,20,30,40,50]
l2 = [60,70,80,90,100]
print(l1+l2)# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(l1*l2) # TypeError: can't multiply sequence by non-int of type 'list'

# task 3 : Repetition of list objects
print(l1*3) # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# task 4 : packing and unpacking of list objects
#a,b,c,d,e,f,g,h,i = [10,20,30,40,50,60,70,80,90]
#print(a,b,d,e,g)


a,b,*c,d = [10,20,30,40,50,60,70,80,90]
print(a,b,d) # 10 20 90
#ValueError: too many values to unpack (expected 4)


