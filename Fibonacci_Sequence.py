# Going to print the first 20 digits of the fibonacci sequence
a = 0
b = 1
for i in range (0,20):
    c = a + b
    a = b
    b = c
    i += 1 
    print(c)
