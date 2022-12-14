# TeamSplitter-DiscordBot
A discord bot meant to help distribute players into teams for competitive gaming.

# Dependencies

Python 3.9.7

Discord Hikari API Wrapper

Discord Lightbulb Library for Hikari

It is recommended that Hikari and Lightbulb are installed in a Python virtual environment.

# Start-Up

1. Enter a discord bot token into the token field of the "bot" declaration, located at the top of "bot.py".

2. Invite the bot to a discord server, and grant the bot permissions to use text channels.

3. Run "bot.py" to start the bot.

# Operation

This bot utilizes "/" (slash) commands to execute its functions. Entering a "/" in any text channel should allow for 
the usage of this bot's commands.

The commands are as follows:

1. "split" 

This command splits a list of players(strings) into two teams randomly. 

Options: "players" - The list of players to be split. Input must be seperated by a space, such as "player1 player2".

Example input: dylan kelly trevor mark john jin

![Screenshot (295)](https://user-images.githubusercontent.com/78335264/196010575-92abf0fc-c560-4943-93b4-181dd5fc975f.png)

2. "fair_split" 

This command splits a list of players(strings,skill) into two teams based on total skill level

Options: "players" - The list of players to be split. Input must be a list of players, seperated by a space, and their respective skill levels
represented as integers, such as "player1,4 player2,1".

Example input: dylan,5 john,8 mark,7 kelly,7 trevor,4 jin,6

![Screenshot (296)](https://user-images.githubusercontent.com/78335264/196010647-c5702fff-62ba-4e4e-8058-0b28dbbf1320.png)

3. "fair_split_2" 

This command splits a list of players(strings,skill) into two teams based on average skill level. The players' skill level and the team they
are assigned to are calculated differently when compared to "fair_split".

Options: "players" - The list of players to be split. Input must be a list of players, seperated by a space, and their respective skill levels
represented as integers, such as "player1,4 player2,1".

Example input: dylan,5 john,8 mark,7 kelly,7 trevor,4 jin,6

![Screenshot (297)](https://user-images.githubusercontent.com/78335264/196010672-5eb754ae-d38a-49cd-8f68-cb2fd1ceb0cf.png)
