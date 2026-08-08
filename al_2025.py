
def menu():
    print("1. Read a student's mark")
    print("2. Display marks")
    print("3. Exit")
    i=int(input("Enter your choice: "))
    return i

def calculate(n):
    result = 0
    for i in range(1, n+1):
        for j in range (i):
            result += i*j
    return result
print(calculate(4))
