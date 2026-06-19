# character occurance

str1 = input("Enter the phrase : ")
ch = input("enter the character that had to be counted : ")
count = 0
for i in str1:
    if ch == i:
        count+=1

print(f"the no. of {ch} {str1} is {count}")