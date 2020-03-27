#!/usr/bin/env python3
import discord
from discord.ext import commands
import meme

# Get credentials from creds.cfg file
def get_creds():
    creds = []
    f = open('creds.cfg','r')
    for line in f.readlines():
        creds.append(line.rstrip())
    return creds

# Initialize some stuff
uname, pw, TOKEN = get_creds() # Get credentials for Discord and ImgFlip
template = ['11','61520','Futurama Fry'] # Set a default template
bot = commands.Bot(command_prefix='$', description='Virtual Mr Davis')
bot.remove_command("help") # Remove default help command so I can use my own

# Let us know when you are up
@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('--------')
  
# Help text 
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Big Boss Man Bot", description="Virtual Mr Davis. He loves meme! List of commands are:", color=0x76f211)
    embed.add_field(name="$memegame", value="Chooses a random meme for captioning", inline=True)
    embed.add_field(name='$caption "Text Box 1" "Text Box 2"', value="Provide text for the selected meme", inline=False)
    await ctx.send(embed=embed)

# Play the meme game
@bot.command()
async def memegame(ctx):
    global template
    template = meme.random_temp()
    k = "Let's play the random meme game!\nThe meme in play is: " + template[2] + '\nSend me $caption "Text Box 1" "Text Box 2"'
    await ctx.send(k)

# Caption a meme
@bot.command()
async def caption(ctx,box1, box2):
    global template
    await ctx.send(meme.make_meme(uname, pw, template[1],box1,box2))

# Let's start this party!
bot.run(TOKEN)
