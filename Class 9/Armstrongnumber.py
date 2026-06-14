#  armstrong numbers

n = int(input("enter the number : "))
s = 0
t = n
while t > 0:
    r = t % 10
    s += r **3
    t //= 10

if s == n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")