n = eval(input("Enter a number: "))
i = 1
sum = 0
a, b = 0, 1
print (a)
while i < (n-1):
    i += 1
    sum = a + b
    a = b
    b = sum
    print (a)
print (sum)


# Another version of the same problem (not like in pseudo code)
n = eval(input("Enter a number: "))
i = 1
sum = 0
a, b = 0, 1
lst = [0, 1]
while i < (n-1):
    i += 1
    sum = a + b
    a = b
    b = sum
    lst.append(sum)
print (lst)