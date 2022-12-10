with open("file1.txt") as data1:
    num1 = data1.readlines()
    n = []
    for num in num1:
        n.append(int(num.strip()))

with open("file2.txt") as data2:
    num2 = data2.readlines()
    n1 = []
    for nu in num2:
        n1.append(int(nu.strip()))

print(n1)
print(n)
numbers = [b for b in n1 if b in n]
print(numbers)
