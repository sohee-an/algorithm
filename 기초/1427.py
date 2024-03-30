num = input(" ")
print(num)
input_list = []
for i in range(len(num)):
    input_list.append(num[i])

sorted_num = sorted(input_list, reverse=True) 
result = ''.join(sorted_num) 
print(result)