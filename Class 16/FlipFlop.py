# flipflop

def palindrome(tuplex):
    s = 0
    l = len(tuplex)
    e = l-1
    while s < e:
        if tuplex[s] != tuplex[e]:
            return False
        s +=1
        e -=1

    return True
        



tuplex = (1,2,3,3,2,1)

if (palindrome(tuplex)):
    print("The given tuple is a palindrome")
else:
    print("The given tuple is not a palindrome")

