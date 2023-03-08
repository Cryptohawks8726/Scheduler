import csv
import math

matchSchedule = [
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111], 
[8726, 5338, 4099, 612, 254, 111]
]

scouts = []
#2d array (just like match schedule)
scoutPods = []
scoutSchedule = []

with open("example_attendance_roster.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if not line[0] == 'id': # will ignore the first row (the headers)
            scouts.append(line)

def assignScoutPods():
    podNum = math.ceil(len(scouts)/6) #5 (for example)
    scoutNum = 0
    for i in range(podNum):
        pod = []
        scoutPods.append(pod)
        for j in range(6):
            if scoutNum < len(scouts):
                pod.append(scouts[scoutNum][1])
                scoutNum += 1

assignScoutPods()

def assignSchedule():
    numOfMatches = len(matchSchedule)
    i = 0
    for j in range(numOfMatches):
        podNum = len(scoutPods)
        pod = scoutPods[i%podNum]
        scoutSchedule.append(pod)
        i += 1

assignSchedule()
print('''



SCOUT PODS:
''')
print(scoutPods)
print('''



SCOUT SCHEDULE:
''')
print(scoutSchedule)