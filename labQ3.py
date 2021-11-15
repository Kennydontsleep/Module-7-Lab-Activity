def multiplyList(n):
    total = 1
    for i in n:
        total = total * i
    return total


numL= [5, 2, 7, -1]
print("total is",multiplyList(numL))