a = int(input("Zadaj čislo: "))
faktorial = 1
for i in range(1,a+1):
    faktorial = i * faktorial
print("Faktoriál čisla",a,"je",faktorial,".")
