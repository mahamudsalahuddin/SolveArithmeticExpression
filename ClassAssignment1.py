list1 = input("Enter a string: ")
list2 = input("Enter finding value: ")
positions = []
temp = 0
length = len(list2)
times = list1.count(list2)
print(times, " times")
for val in range(times):
    positions.append(list1.find(list2, temp))
    temp = list1.find(list2, temp) + length
print("Positions", positions)