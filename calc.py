x = 5 
y = 4

numbers_list = [20, 12, -2, 88, 90, 200, -100, 20]

def find(list):
    for i in list: 
        if (i == 90):
            print("Found")
            return
        print("Not Found")

find(numbers_list)

def sum(list):
    sum = 1
    for i in list:
        sum = sum + i
    return sum

result = sum(numbers_list)
print(result)