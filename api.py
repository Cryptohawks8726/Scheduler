import requests
import base64
import json

def encoder():
    sample_string = "neb12345:151e0d73-a9fa-4b0f-9ae6-c9396a9655e3"
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return(base64_string)

encoded = encoder()

link = "https://frc-api.firstinspires.org/v3.0/2022/schedule/CHCMP?tournamentLevel=qual"

header = {"Authorization" : "Basic bmViMTIzNDU6MTUxZTBkNzMtYTlmYS00YjBmLTlhZTYtYzkzOTZhOTY1NWUz", "If-Modified-Since":"2021"}

r = requests.get(link, headers=header)
res = r.content.decode("utf-8")

dict = json.loads(res)
matchList = dict['Schedule']
teamsInMatches = []
for matchInfo in matchList:
    teamsInfo = matchInfo['teams'] # index 0 is the first match
    teams = []
    for teamInfo in teamsInfo:
        teams.append(teamInfo['teamNumber'])
    teamsInMatches.append(teams)

#print(matchList[0])