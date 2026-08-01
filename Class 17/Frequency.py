# count the Frequency

words = { "lemon":3,"pen":2,"coding":2,"ice":2,"purse":3}

k = 3
count = 0
for key in words:
    if words[key] == k:
        count+=1

print(f"THe number of words having {k} frequency is {count}")