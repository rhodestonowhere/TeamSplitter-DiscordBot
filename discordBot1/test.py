
playerDict = {}
playerDict.setdefault("a", 1)
playerDict.setdefault("b", 2)
playerDict.setdefault("c", 3)
playerDict.setdefault("d", 4)
playerDict.setdefault("e", 5)
playerDict.setdefault("f", 6)
globalAvg = sum(playerDict.values()) / len(playerDict) #global average is sum of dictionary values over number of elements in dictionary
team1 = []
team2 = []
team1 = []
team2 = []
team1 = list(playerDict)[0]
team2 = list(playerDict)[1]
print(team1)
print(team2)
team1TotalSkill = playerDict[team1[0]]
playerDict.pop(team1[0])
print(team1TotalSkill)
team2TotalSkill = playerDict[team2[0]]
playerDict.pop(team2[0])
print(team2TotalSkill)

for player in playerDict:
    print("start")
    team1Avg = team1TotalSkill / len(team1)
    team2Avg = team2TotalSkill / len(team2)
    if team1Avg > team2Avg:
            lowAvgTeam = team2
            lowTotalSkill = team2TotalSkill
            highAvgTeam = team1
            highTotalSkill = team1TotalSkill
    else:
            lowAvgTeam = team1
            print(lowAvgTeam)
            lowTotalSkill = team1TotalSkill
            highAvgTeam = team2
            highTotalSkill = team2TotalSkill

    # if playerDict[player] > globalAvg:
    #         lowAvgTeam.insert(0, player)
    #         lowTotalSkill += playerDict[player]
    #         print("first")
    #         print(lowAvgTeam)
    #         print(lowTotalSkill)
    #         print("Team 1:")
    #         print(team1)
    #         print("Team2 :")
    #         print(team2)

    # else:
    #         highAvgTeam.insert(0, player)
    #         highTotalSkill += playerDict[player]
    #         print("second")
    #         print(highAvgTeam)
    #         print(highTotalSkill)
    #         print("Team 1:")
    #         print(team1)
    #         print("Team2 :")
    #         print(team2)
