n=int(input("Zadaj čislo väčšie ako 2: "))
j = n - 1 
print("#"*n)
for i in range(n-2):
    print("#")
print("#"*n)
for i in range(n-2):
     print(" "*j + "#")
print("#"*n)
