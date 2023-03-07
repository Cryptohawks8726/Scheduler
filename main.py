import csv

scouts = []
matchSchedule = [
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111]
]
#2d array (just like match schedule)
scoutSchedule = []

with open("example_attendance_roster.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if not line[0] == 'id': # will ignore the first row (the headers)
            scouts.append(line)

def assign():
    i = 0
    for match in matchSchedule:
        scoutList = []
        scoutSchedule.append(scoutList)
        for team in match:
            scout = scouts[i % len(scouts)]
            scoutList.append(scout[1])
            
            i += 1
    
    print(scoutSchedule)

assign()