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
    # assign the same pod to say 5 matches in a row
    for j in range(numOfMatches):
        podNum = len(scoutPods)
        pod = scoutPods[i%podNum]
        scoutSchedule.append(pod)
        i += 1

assignSchedule()
# maybe print the pods at the beginning with a label (pod 1, pod 2, etc)
# and then print out the match numbers each followed by the pod number
# i.e.
"""
Pod 1: Amogh, Deven, Abhinav, Nick, Tarun
Pod 2: ...

Match 1: Pod 1
Match 2: Pod 1
Match 3: Pod 2
...
Match 35: Pod 3
"""

print('''



SCOUT PODS:
''')
print(scoutPods)
print('''



SCOUT SCHEDULE:
''')
# print match number
print(scoutSchedule)