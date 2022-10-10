@bot.command
@lightbulb.option('player_skill', 'Input: player,skill| list of players with skills to be split')
@lightbulb.command('fair_split_2', 'splits a list of players into two most balanced teams using averages. skill level ranges 1-5')
@lightbulb.implements(lightbulb.SlashCommand)
async def fair_split_2(context):
    
    playerList = context.options.player_skill.split() #initial list of (player,skill) tuples
    playerDict = {} #declare dictionary 
    for tuple in playerList: #for each tuple in player list,
        pair = tuple.split(",") #split tuple using "," delimiter to seperate player name and skill
        playerDict.setdefault(pair[0], int(pair[1])) #add player's name and according skill to dictionary

    globalAvg = sum(playerDict.values()) / len(playerDict) #global average is sum of dictionary values over number of elements in dictionary
    # print(globalAvg)
    """
    Outline of method:
    set team1[0] = first element of dict
    set team2[0] = second element of dict
    team1Avg = sum(team1) / len(team1)
    team2Avg = sum(team2) / len(team2)
    for pair in playerDict:
        if pair value < global avg 
            add to team with lowest average skill
        else
            add to team with highest average skill
        if either team is has reached team capacity then put remaining players into other team
    """
    team1 = [] 
    team2 = []
    keys = list(playerDict.keys()) #get list of all keys in the dictionary as list
    team1.insert(0, keys[0]) #insert first and second elements of list into teams
    team2.insert(0, keys[1])
    team1TotalSkill = playerDict[team1[0]] #get skill of initial players
    keys.pop(0) #remove player from dictionary and list
    playerDict.pop(team1[0])
    team2TotalSkill = playerDict[team2[0]]
    keys.pop(1)
    playerDict.pop(team2[0])

    
    for player in playerDict: #for every player in playerDict
        print('///////////////////////////////////////////')
        print("|Loop Start| Global Average is: {}".format(globalAvg))
        print('///////////////////////////////////////////')
        team1Avg = team1TotalSkill / len(team1) #calculate the average skill of both teams
        team2Avg = team2TotalSkill / len(team2)
        print("Team 1 average is: {}".format(team1Avg))
        print("Team 2 average is: {}".format(team2Avg))

        if len(team1) == (len(playerDict)+2) / 2: #check if the length of either team has reached roughly half of the total players
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("Team 1 has reached capacity! Placing remaining members in Team 2.")
            print("player name is: {}".format(player))
            team2.insert(0, player) #if so, then add player to opposite team
            team2TotalSkill += playerDict[player] #add skill to team's total skill
            continue

        elif len(team2) == (len(playerDict)+2) / 2:       
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("Team 2 has reached capacity! Placing remaining members in Team 1.")
            print("player name is: {}".format(player))
            team1.insert(0, player)
            team1TotalSkill += playerDict[player]
            continue

        if team1Avg > team2Avg: #in the case that team 2 is lower skilled team
            print("Low Average Team is: Team 2")
            if playerDict[player] > globalAvg: #if player skill is higher than the global average
                print("player skill: higher than globalAvg")
                print("player name is: {}".format(player))
                print("player skill is: {}".format(playerDict[player]))
                team2.insert(0, player) #add player to lower skilled team
                team2TotalSkill += playerDict[player]
                print("Current Team 1: {}".format(team1))
                print("Current Team 1 Skill: {}".format(team1TotalSkill))
                print("Current Team2 : {}".format(team2))
                print("Current Team 2 Skill: {}".format(team2TotalSkill))

            elif playerDict[player] < globalAvg: #player skill is less than average
                print("player skill: lower than globalAvg")
                print("player name is: {}".format(player))
                print("player skill is: {}".format(playerDict[player]))
                team1.insert(0, player) #add to higher skilled team
                team1TotalSkill += playerDict[player]
                print("Current Team 1: {}".format(team1))
                print("Current Team 1 Skill: {}".format(team1TotalSkill))
                print("Current Team2 : {}".format(team2))
                print("Current Team 2 Skill: {}".format(team2TotalSkill))      
        else: #in the case that team 1 is the lower skilled team
            print("Low Average Team is: Team 1")
            if playerDict[player] > globalAvg:
                print("player skill: higher than globalAvg")
                print("player name is: {}".format(player))
                print("player skill is: {}".format(playerDict[player]))
                team1.insert(0, player)
                team1TotalSkill += playerDict[player]
                print("Current Team 1: {}".format(team1))
                print("Current Team 1 Skill: {}".format(team1TotalSkill))
                print("Current Team2 : {}".format(team2))
                print("Current Team 2 Skill: {}".format(team2TotalSkill))

            elif playerDict[player] < globalAvg:
                print("player skill: lower than globalAvg")
                print("player name is: {}".format(player))
                print("player skill is: {}".format(playerDict[player]))
                team2.insert(0, player)
                team2TotalSkill += playerDict[player]
                print("Current Team 1: {}".format(team1))
                print("Current Team 1 Skill: {}".format(team1TotalSkill))
                print("Current Team2 : {}".format(team2))
                print("Current Team 2 Skill: {}".format(team2TotalSkill))      


    #one last calculation to account for last added player
    team1Avg = team1TotalSkill / len(team1) 
    team2Avg = team2TotalSkill / len(team2)

    team1Formatted = ", ".join(team1)
    team2Formatted = ", ".join(team2)
    response = '\n**Team 1:** {team1} | Power Level: {team1skill}\n**-------------------------------**\n**Team 2:** {team2} | Power Level: {team2skill}'.format(
        team1 = team1Formatted, team2 = team2Formatted, team1skill = team1Avg, team2skill = team2Avg) 


    await context.respond(response)

