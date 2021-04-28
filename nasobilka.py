n=int(input("Zadaj čislo: "))
for riadok in range(1,n+1):
    for stlpec in range(1,n+1):
        j = riadok * stlpec
        print(j, end=" ")
    print()
