import random,requests,asyncio, time

from time import strftime, localtime

from discord import Game
from discord.ext.commands import Bot

PREFIX = ';'
TOKEN = 'XXXSECRETXXX'

client = Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name=";help for help"))
    print("Logged in as " + client.user.name)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('good night') or message.content.startswith('Good night') or message.content.startswith('Good Night'):
        msg = 'Good night {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('Sup') or message.content.startswith('sup'):
        msg = 'Sup bitch?'
        await client.send_message(message.channel, msg)
        
@client.command(name='8ball',
                description="Answers a yes or no question.",
                brief="Answers your questions.",
                aliases=['eight_ball', 'eightball'])

async def eight_ball():
    possible_responses = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "You can count on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Absolutely",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "I want to fuck you in the ass",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
        "Chances aren't good"
    ]
    await client.say(random.choice(possible_responses))

@client.command(name='daily',
                description="Daily income of 100 bekcoins.",
                brief="Daily income.",
                pass_context=True)

async def daily(context):
    text = ":)"
    try:
        number = 0
        with open("coins.txt", 'r') as f:
            data = f.readlines()
            content = data
            i = 0
            index = -1
            for line in content:
                line = line.split(',')
                if line[0] == context.message.author.mention:
                    number = int(line[1])
                    oldday = line[2]
                    index = i
                    break
                i += 1
                
        with open("coins.txt", 'w') as f:
            if index != -1:
                newday = strftime("%d", localtime())
                if newday == oldday:
                    text = "You have already received your daily 100 bekcoins for today."
                    number = 0
                    data[i] = context.message.author.mention + ',' + str(number + 100) + ',' + newday
                    f.writelines(data)
                else:
                    text = "You have received 100 bekcoins and now have a total of {} bekcoins.".format(str(number+100))
            else:
                text = "You have received 100 bekcoins and now have a total of 100 bekcoins."
                f.writelines(data)
                f.write(context.message.author.mention + ',100,' + (strftime("%d", localtime())))
            f.close()
        
    except(error):
        print("Error: File does not exist")
        
    await client.say(text)

@client.command(name='coins',
                description="Shows the amount of bekcoins you have.",
                brief="Answers your questions.",
                aliases=['bekcoins','bcoins'],
                pass_context=True)

async def coins(context):
    amount = '0'
    user = context.message.author.mention
    with open("coins.txt", 'r') as f:
        content = f.read().split('\n')
        for line in content:
            line = line.split(',')
            if line[0] == user:
                amount = line[1]
                break
    await client.say(amount + " bekcoins")


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)






















