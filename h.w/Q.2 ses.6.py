

n = int(input('Please enter your number: '))
list = []
 
list2 = int(input("Enter number of elements : "))
 
for i in range(0, list2):
    m = int(input())
   
    list.append(m)  
 
print('old_list= ', list )
for i in range(len(list)-1):
    if len(list) < 4:
       print('The list has to contain at least four values')
       break
      
    
    elif list[i]<0:
            print('the numbers has to be a positive value')
            break
            
    elif list[i]>list[i+1]:
        print('the list has to be sorted')
        break
    else:
        new_list = list[n:-n]  
        print('your new list is: ',new_list)
        break

    
    













 



