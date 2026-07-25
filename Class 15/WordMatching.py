# word matching
def word_matching(list1):
    newlist = []
    count = 0
    for word in list1:
        if word[0] == word[-1]:
            count+=1
            newlist.append(word)
    print(newlist)
    return count

list1 = ['accasia', 'bob','currency','likes','pop']
print("The count of first and last letter matching :",word_matching(list1)) 