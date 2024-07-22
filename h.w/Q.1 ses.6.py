
list1 = ["apples","peaches","oranges","watermelon"]

if len(list1) == 1:
    printed_list = list1[0]
elif len(list1) > 1:
    printed_list= ",".join(list1[:-1]) + ' ' + 'and'+ " " + list1[-1]

else:
    printed_list = ""

print(printed_list)

