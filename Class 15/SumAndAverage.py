# sum, average, mix, mix

list1 = [12,34,67,89,98123,3,124,77]

sum = 0
for i in list1:
    sum += i

print("the sum of the list is : ",sum)
print("the average of the list is : ",sum/len(list1))
list1.sort()
print("the sorted list ",list1)
print("the min value of the list is : ",list1[0])
print("the max value of the list is : ",list1[len(list1)-1])