list1 = [3, 5, 6, 8] 
list2 = [2, 4, 8, 9, 7]

print("List_1 Before assigning : " + str(list1)) 
list1.extend(range(6)) 

print("List_1 After assigning : " + str(list1)) 

print("List_2 Before assigning : " + str(list2)) 
list2.append('new') 

print("List_2 After assigning : " + str(list2)) 