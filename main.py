import csv
import math
import api

matchSchedule = api.teamsInMatches
rawSchedule = api.matchList


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

def listToString(list):
    i = 0
    finalStr = ''
    for item in list:
        i += 1
        finalStr += str(item)
        if i < len(list):
            finalStr += ', '
    return finalStr

def dictToString(dict):
    i = 0
    finalStr = ''
    for k, v in dict.items():
        i += 1
        finalStr += str(k)+'-'+str(v)
        if i < len(dict):
            finalStr += ', '
    return finalStr

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

print('''



SCOUT PODS:
''')
podI = 0
for scoutPod in scoutPods:
    podI += 1
    string = 'Pod '+str(podI)+': '+ listToString(scoutPod)

print('''



SCOUT SCHEDULE:
''')
# print match number

"""

scoutToRobot = [] # will have each pair of scout, matchNUm-robotNum

podNum = 0 # iteration number
# for each matchInfo in the schedule
for match in rawSchedule:
    j = 0 # scout pod iteration
    # for each teamInfo in the match
    for team in matchSchedule[podNum]:
        # gets the current pod we are assigning
        currentPod = scoutPods[podNum % len(scoutPods)]
        scout = 'UNASSIGNED' # default
        if j < len(currentPod):
            scout = currentPod[j] # gets the current scout out of the scout pod
        
        scoutToRobot.append([scout, str(match['matchNumber'])+'-'+str(team)])
        j += 1
    podNum += 1

csvList = []

for scoutPod in scoutPods:
    for scout in scoutPod:
        scoutInfo = [scout] # will have the scout name and all of their match-robotNum assigned to them
        for nameRobotPair in scoutToRobot:
            name = nameRobotPair[0]
            robotInfo = nameRobotPair[1] # the match-robotNum pair
            if name == scout:
                scoutInfo.append(robotInfo)
        csvList.append(scoutInfo)

csvFields = ['name', 'matchNumber-robotNumber']

print(csvList)

# writing to csv file 
with open("output.csv", 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
   
    # writing the fields 
    csvwriter.writerow(csvFields) 
    # writing the data rows 
    csvwriter.writerows(csvList)




