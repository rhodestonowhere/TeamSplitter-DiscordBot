
import hikari
import lightbulb
import random

bot = lightbulb.BotApp(token='', 
    default_enabled_guilds=(1014672301914067014))

@bot.listen(hikari.StartedEvent)
async def startUp(event):
    print('bot online')

@bot.command
@lightbulb.command('ping', 'return pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond("pong")

@bot.command
@lightbulb.option('n1', 'the first number', type=int)
@lightbulb.option('n2', 'the 2nd number', type=int)
@lightbulb.command('add', 'adds two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(context):
    await context.respond(context.options.n1 + context.options.n2)

@bot.command
@lightbulb.option('players', 'Input: player|the list of players to split', type=str)
@lightbulb.command('split', 'randomly splits a list players into 2 teams. enter the list a player names seperated by a space')
@lightbulb.implements(lightbulb.SlashCommand)
async def split(context):
    playerList = context.options.players.split() #splits user input into list of strings
    #print(playerList)
    team1 = [] #team objects returned at the end
    team2 = []
    teamBit = True #alternate bit to assign player to a team
    teamSize = len(playerList) / 2

    while not len(playerList) == 0: #while the length of player list is not 0 (while playerList still has elements)

        player = random.choice(playerList) #randomly select player
        
        if teamBit == True and len(team1) < teamSize:
            teamBit == False
            team1.insert(0, player) #invert bit
        else:
            teamBit == True
            team2.insert(0, player) #invert bit

        playerList.remove(player) #remove player from list

    team1Formatted = ", ".join(team1)
    team2Formatted = ", ".join(team2)

    response = '\n**Team 1:** {team1}\n**-------------------------------**\n**Team 2:** {team2}'.format(team1 = team1Formatted, team2 = team2Formatted) 

    await context.respond(response)

@bot.command
@lightbulb.option('player_skill', 'Input: player,skill| list of players with skills to be split')
@lightbulb.command('fair_split', 'splits a list of players into two most balanced teams based on skill level.')
@lightbulb.implements(lightbulb.SlashCommand)
async def fair_split(context):
    playerList = context.options.player_skill.split() #initial list of (player,skill) tuples

    #this method seems wildly haphazard...depends too heavliy on the correct input of data
    #maybe try splitting it into two options?

    playerDict = {} #declare dictionary 
    for tuple in playerList: #for each tuple in player list,
        pair = tuple.split(",") #split tuple using "," delimiter to seperate player name and skill
        playerDict.setdefault(pair[0], pair[1]) #add player's name and according skill to dictionary

    #variable delcaration
    team1 = []
    team2 = []
    team1skill = 0
    team2skill = 0
    iter1 = 0
    for key in playerDict: #for each key in the dictionary,
        value = int(playerDict[key]) #gets val associated with key, typecasts to int()
        if iter1 == 0: #checks if this is the first iteration
            team1.insert(0, key) #in which case, just add first key into team 1
            team1skill += value #add skill level of current player to overall team skill
            iter1 = 1 #change value to not trigger conditional
            continue #iterate again
        if team1skill > team2skill:#case where team 1's skill level exceeds team 2's
            team2.insert(0, key) #give team 2 the new member
            team2skill += value
        elif team1skill == team2skill: #case where teams' skill levels are equal
            num = random.randrange(1,2) #randomly assign new member to a team
            #no switch statements in python 3.9, so if-elif it is
            if num == 1:
                team1.insert(0, key) 
                team1skill += value
            else:
               team2.insert(0, key)
               team2skill += value 
        else: #in the case that team 2's skill exceeds team 1
            team1.insert(0, key) #give team 1 new member
            team1skill += value
        #algorithm does have issues, as it does not always create the most equal teams
        #ex: "a,5 b,1 c,2 d,4" creates a team split as 5-7, when it should be 6-6
        
        
        
    team1Formatted = ", ".join(team1)
    team2Formatted = ", ".join(team2)
    response = '\n**Team 1:** {team1} | Power Level: {team1skill}\n**-------------------------------**\n**Team 2:** {team2} | Power Level: {team2skill}'.format(
        team1 = team1Formatted, team2 = team2Formatted, team1skill = team1skill, team2skill = team2skill) 
    await context.respond(response)
    


@bot.command
@lightbulb.option('player_skill', 'Input: player,skill| list of players with skills to be split')
@lightbulb.command('fair_split_2', 'splits a list of players into two most balanced teams using averages.')
@lightbulb.implements(lightbulb.SlashCommand)
async def fair_split_2(context):
    
    playerList = context.options.player_skill.split() #initial list of (player,skill) tuples
    playerDict = {} #declare dictionary 
    for tuple in playerList: #for each tuple in player list,
        pair = tuple.split(",") #split tuple using "," delimiter to seperate player name and skill
        playerDict.setdefault(pair[0], int(pair[1])) #add player's name and according skill to dictionary

    globalAvg = sum(playerDict.values()) / len(playerDict) #global average is sum of dictionary values over number of elements in dictionary
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
        team1Avg = team1TotalSkill / len(team1) #calculate the average skill of both teams
        team2Avg = team2TotalSkill / len(team2)

        if len(team1) == (len(playerDict)+2) / 2: #check if the length of either team has reached roughly half of the total players
            team2.insert(0, player) #if so, then add player to opposite team
            team2TotalSkill += playerDict[player] #add skill to team's total skill
            continue

        elif len(team2) == (len(playerDict)+2) / 2:       
            team1.insert(0, player)
            team1TotalSkill += playerDict[player]
            continue

        if team1Avg > team2Avg: #in the case that team 2 is lower skilled team
            if playerDict[player] > globalAvg: #if player skill is higher than the global average
                team2.insert(0, player) #add player to lower skilled team
                team2TotalSkill += playerDict[player]

            elif playerDict[player] < globalAvg: #player skill is less than average
                team1.insert(0, player) #add to higher skilled team
                team1TotalSkill += playerDict[player]
    
        else: #in the case that team 1 is the lower skilled team
            if playerDict[player] > globalAvg:
                team1.insert(0, player)
                team1TotalSkill += playerDict[player]

            elif playerDict[player] < globalAvg:
                team2.insert(0, player)
                team2TotalSkill += playerDict[player] 


    #one last calculation to account for last added player
    team1Avg = team1TotalSkill / len(team1) 
    team2Avg = team2TotalSkill / len(team2)

    team1Formatted = ", ".join(team1)
    team2Formatted = ", ".join(team2)
    response = '\n**Team 1:** {team1} | Power Level: {team1skill}\n**-------------------------------**\n**Team 2:** {team2} | Power Level: {team2skill}'.format(
        team1 = team1Formatted, team2 = team2Formatted, team1skill = team1Avg, team2skill = team2Avg) 


    await context.respond(response)

bot.run()