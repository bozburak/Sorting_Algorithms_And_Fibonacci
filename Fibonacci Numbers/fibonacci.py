a, b = 0, 1
print a,"\n", b
for i in range(10):
    c = a + b
    a = b
    b = c
    print c
