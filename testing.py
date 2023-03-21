import csv
import math
import api
import tabulate


def getScouts():
    """
    function description
    reads scouts from csv file and returns the scouts in a list

    :return list of scouts
    """
    scoutsList = []
    with open('attendance.csv', "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if not line[0] == 'id': # will ignore the first row (the headers)
                scoutsList.append(line)

    return scoutsList

def getNextScouts(nextScout, scouts):
    """
    function description
    adds the next 6 scouts and the next scout to the scouts list
    
    :param nextScout: the scout number it is currently on
    :param scouts: the scout list

    :return the next 6 scouts (pod) and the next scout
    """
    scoutsList = []

    for _ in range(6):
        if nextScout >= len(scouts):
            nextScout = 0

        scoutsList.append(scouts[nextScout])
        nextScout += 1

    return scoutsList, nextScout

def getNextMatches(numMatches, nextMatch, matchSchedule):
    """
    function description
    gets next # matches based on how long the user wants to make the scouting time
    
    :param numMatches: number of matches in a row
    :param nextMatch: the current match number (iteration) it is on

    :return the next # matches based on user input
    """
    matches = []

    for _ in range(numMatches):
        if nextMatch >= len(matchSchedule):
            return matches, nextMatch
        matches.append(matchSchedule[nextMatch])
        nextMatch += 1

    return matches, nextMatch

def assignScouts():
    """
    function description
    gets next 6 scouts paired with the next # of matches

    :return none, just writes to the csv file
    """
    matchSchedule = api.teamsInMatches
    scouts = getScouts()
    nextScout = 0
    nextMatch = 0
    numMatches = 5

    output = []
    tempList = []
    finalList = []

    for _ in range(math.ceil(len(matchSchedule) / numMatches)):
        nextScouts, nextScout = getNextScouts(nextScout, scouts)

        nextMatches, nextMatch = getNextMatches(numMatches, nextMatch, matchSchedule)

        for i in range(numMatches):
            match = []

            for j in range(6):
                match.append([nextMatches[i][j], nextScouts[j]])
            
            output.append(match)


    matchNum = 1
    for match in output:
        for scoutPair in match:
            scoutInfo = [scoutPair[1], matchNum, scoutPair[0]]
            tempList.append(scoutInfo)
        matchNum += 1


    for scout in scouts:
        temp = [scout]
        for row in tempList:
            if row[0] == scout:
                temp.append(f"{row[1]}-{row[2]}")

        finalList.append(temp)

    for row in finalList:
        print(row)
        

    with open('output.csv', 'w', newline='') as csvfile: 
        print('Writing to: ' + 'output.csv')
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(["Name", "Match Number-Team Number"])
        # writing the data rows 
        csvwriter.writerows(finalList)


if __name__ == '__main__':
    assignScouts()