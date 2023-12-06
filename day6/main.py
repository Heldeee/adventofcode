
def get_data(input):
    time = []
    distance = []
    for line in input:
        elements = line.split()
        numbers = [int(x) for x in elements if x.isdigit()]
        
        if "Time" in line:
            time.extend(numbers)
        elif "Distance" in line:
            distance.extend(numbers)

    tablo = []
    for i in range(len(time)):
        tablo.append([time[i], distance[i]])

    return tablo

def get_record(race):
    possible = []
    time, record = race
    for i in range (time + 1):
        compute = i * (time - i)
        if compute > record:
            possible.append(compute)
    return possible

def puzzle6(input):
    data = get_data(input)

    total = 1
    for race in data:
        total *= len(get_record(race))
    return total

input = open("test.txt","r")
print(puzzle6(input))
input = open("input6-1.txt","r")
print(puzzle6(input))

def get_data2(input):
    tablo = []
    time = []
    distance = []
    for line in input:
        elements = line.split()
        numbers = [int(x) for x in elements if x.isdigit()]
        if "Time" in line:
            time.extend(numbers)
        elif "Distance" in line:
            distance.extend(numbers)
        
        res = ""
        temp = [str(x) for x in numbers]
        for num in temp:
            res += num
        tablo.append(int(res))

    return [tablo]

def puzzle6_2(input):
    data = get_data2(input)

    total = 1
    for race in data:
        total *= len(get_record(race))
    return total

input = open("test.txt","r")
print(puzzle6_2(input))
input = open("input6-1.txt","r")
print(puzzle6_2(input))