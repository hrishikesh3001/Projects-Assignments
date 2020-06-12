#program for identifying positive numbers

list1 = [12,-7,-5,64,-14]

list2 = [12,14,-95,3]

for num in list1: 
      
    if num >= 0: 
       print(num, end = " ") 

while(num < len(list2)): 

    if num >= 0: 
        print("\n", list2[num], end = " ") 

    num += 1