#  armstrong numbers

n = int(input("enter the number : "))
c = 0
t = n
while t > 0:
    r = t % 10
    c += 1
    t //= 10

print ("The number of the digits",c)