import csv
import math
import api
import click

matchSchedule = api.teamsInMatches
rawSchedule = api.matchList

scouts = []
#2d array (just like match schedule)
scoutPods = []
#scoutSchedule = []

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

"""
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
"""

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
csvList = [] # final list

def assignScouts(scoutingTime):
    matchNum = 0 # match number
    currentPodNum = 0 # current pod number
    timesScouted = 0 # scouting time elapsed
    # for each matchInfo in the schedule
    for match in rawSchedule:
        j = 0 # iteration inside scout pod (each scout)
        # for each teamInfo in the match
        for team in matchSchedule[matchNum]:
            # gets the current pod we are assigning
            currentPod = scoutPods[currentPodNum % len(scoutPods)]
            scout = 'UNASSIGNED' # default
            if j < len(currentPod):
                scout = currentPod[j] # gets the current scout out of the scout pod
            
            scoutToRobot.append([scout, str(match['matchNumber'])+'-'+str(team)])
            j += 1
        matchNum += 1
        timesScouted += 1
        if timesScouted >= scoutingTime:
            currentPodNum += 1
            timesScouted = 0
    
    # organize each assigned robot to the scout's name
    for scoutPod in scoutPods:
        for scout in scoutPod:
            scoutInfo = [scout] # will have the scout name and all of their match-robotNum assigned to them
            for nameRobotPair in scoutToRobot:
                name = nameRobotPair[0] # name of the scout
                robotInfo = nameRobotPair[1] # the matchNum-robotNum pair
                if name == scout:
                    scoutInfo.append(robotInfo)
            csvList.append(scoutInfo)
    
    # for the unassigned robots that need scouts
    unassignedList = ["UNASSIGNED"] # will have the scout (UNASSIGNED) name and all of their match-robotNum assigned to them
    for nameRobotPair in scoutToRobot:
        name = nameRobotPair[0] # name of the scout
        robotInfo = nameRobotPair[1] # the matchNum-robotNum pair
        if name == "UNASSIGNED":
            unassignedList.append(robotInfo)
    #csvList.append(unassignedList)

    #scoutNum = 0
    #for unasgnRobot in unassignedList:
        #unasgnRobotInfo = unasgnRobot.split("-")
        #unasgnRobotMatchNum = unasgnRobotInfo[0]
        #if not unasgnRobot == "UNASSIGNED": # the first item in the list is not a robot, it is just the name of the list (named "UNASSIGNED")
            #print(csvList[scoutNum % len(scouts)].append(unasgnRobot))
            #scoutNum += 1


def getNextScouts():
    currentScoutNumber = 0
    currentPodNumber = 0
    lastScoutGroup = []
    gettingScouts = []
    for scout in scouts:
        if currentScoutNumber <= 5:
            lastScoutGroup.append(scout[1])
            currentScoutNumber += 1
            '''if len(gettingScouts[currentScoutNumber]):
            #currentPodNumber % len(gettingScouts)
            #currentPodNumber += 1'''
        elif currentScoutNumber > 5:
            currentScoutNumber = 0
    
    gettingScouts.append(lastScoutGroup)
    
    return gettingScouts





csvFields = ['name', 'matchNumber-robotNumber']

lName = ""
fName = ""

@click.command()
@click.option('--link', default ='attendance.csv', help = 'file to read from')
@click.option('--output', default ='example_output.csv', help = 'file to write to')
@click.option('--time', default = 1, help='time each scout has to watch matches')

def inputParams(link, output, time):
    # input
    print('Reading from: '+link)
    lName = link
    with open(lName, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if not line[0] == 'id': # will ignore the first row (the headers)
                scouts.append(line)
    
    assignScoutPods()
    assignScouts(time)

    # calculate break time
    print('Calculated break time: ' + str(time * (len(scoutPods) - 1) ))
    print(getNextScouts())

    # output
    fName = output
    # writing to csv file 
    with open(fName, 'w', newline='') as csvfile: 
        print('Writing to: ' + fName)
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
    
        # writing the fields 
        csvwriter.writerow(csvFields) 
        # writing the data rows 
        csvwriter.writerows(csvList)
  
if __name__=="__main__":
    inputParams()
    