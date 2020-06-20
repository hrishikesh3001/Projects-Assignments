list1 = [(1, 'Revanth', 19), (2, 'Rohit', 20), (3, 'Ritish', 20)] 
 
print ("Before : " + str(list1)) 
nth = [x[1] for x in list1] 

#List with only nth tuple element (i.e names)
print ("After : " + str(nth)) 
