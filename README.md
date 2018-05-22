# BeckBot
Discord.py bot


# my_bot2.py
This file is an example of a discord bot with the following features:
1. Prints when the bot logs in and displays itself as playing ";help for help".
2. When a user says "Good night", then the bot will respond saying "Good night @user".
3. When a user says "Sup", then the bot will respond with "Sup bitch?".
4. Users can use the command ";8ball" to get an answer to a yes or no question. This command has a description which shows when a user says ";help 8ball". This command has a brief which shows up in the general ";help" command. This command has aliases "eight_ball", "eightball" which are seperate ways for users to call the command.
5. Users can use the command ";daily" to receive daily bekcoins. The day is marked in "coins.txt" along with the amount of coins and the user's tag. This command uses pass_context=True in order to get the user who requested the daily coins.
6. Users can use the command ";coins" to check on his or her coin amount in "coins.txt". This command uses previously discussed methods.
7. The servers that the bot is currently active on are printed in list_servers() every 600 seconds or 10 minutes.

# coins.txt
This file is an example of a save file for the coins of users.
1. The example shown uses a user's mention tag first.
2. Second is the amount of coins.
3. Third is the last day that the user called ";daily"
