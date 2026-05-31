# not operator

a = 10
b = 12
c = 12

print(not(a==b))
print(not(b==c))

a = 'coding'
b = 'python'
if (a != b):
    print(a, "and",b, "are different ")

a = 1
b = 4
c = 5

if ( (a==4) != (b == 4)):
    print( "hello")

n = int(input("enter a number : "))
if not(n%2 == 0):
    print("is an odd number")