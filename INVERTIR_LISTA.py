my_list=[]

for x in range(11):

	my_list.append(x)

length=len(my_list)

for i in range(length// 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)