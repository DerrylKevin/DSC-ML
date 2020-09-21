def pairs(array):
    count = 0
    
    for x in set(array):
        count += array.count(x) // 2
    
    print(f"\n{count} pair")
    return

n = int(input("Enter number of elements: "))

array = [int(input("Enter element: ")) for i in range(n)]

pairs(array)
