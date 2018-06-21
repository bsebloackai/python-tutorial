dataset = [(3,3.5,"R"), (3.5,4.5,"B"), (4.5,3,"R"), (10,1,"B"), (10,2,"B"), (10,3,"B"), (10,4,"B")]

x = input("Enter New Observation x: ")
y = input("Enter New Observation y: ")
k = input("Enter the value of k: ")
new_data = (x, y)

distances = map(lambda d: ((((new_data[0] - d[0]) ** 2 + (new_data[1] - d[1]) ** 2 )) ** 0.5, d[2]), dataset)
distances.sort()
neighbours = distances[0:k]

reds = filter(lambda t : t[1] == "R", neighbours)
blues = filter(lambda t : t[1] == "B", neighbours)

observation = 'red' if len(reds) > len(blues) else 'blue'
print('The new value is ' + observation)