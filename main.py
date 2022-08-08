import discord
import os
import requests
from discord.ext import commands
from keep_alive import keep_alive
import json

#clears the spaces for the name for the API call
def clearNameSpaces(nameWithSpaces):
  result = ""
  for n in nameWithSpaces:
    result = result + ' ' + str(n)
  return result

#sets up the correct API to use depending on the region chosen for the summoner name
def getProfile(region, name):
  if region == 'euw1':
    API_Riot = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'eun1':
    API_Riot = 'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'br1':
    API_Riot = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'jp1':
    API_Riot = 'https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'kr':
    API_Riot = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'la1':
    API_Riot = 'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'la2':
    API_Riot = 'https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'na1':
    API_Riot = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'oc1':
    API_Riot = 'https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  if region == 'tr1':
    API_Riot = 'https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + os.environ['riotApiKeY']
  
    
  response = requests.get(API_Riot)
  jsonDataSummoner = response.json()
  encryptedSummonerId = jsonDataSummoner['id']
  sName = jsonDataSummoner['name']
  sLevel = "lvl. " + str(jsonDataSummoner['summonerLevel'])
  sIcon = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/img/profileicon/' + str(jsonDataSummoner['profileIconId']) + '.png'
  return (sName, sLevel, sIcon, encryptedSummonerId)

#get ranking of the summoner using the id
def fetchRanks(region, encryptedSummonerId):
  if region == 'euw1':
    API_Riot = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'eun1':
    API_Riot = 'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'br1':
    API_Riot = 'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'jp1':
    API_Riot = 'https://jp1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'kr':
    API_Riot = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'la1':
    API_Riot = 'https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'la2':
    API_Riot = 'https://la2.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'na1':
    API_Riot = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'oc1':
    API_Riot = 'https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  if region == 'tr1':
    API_Riot = 'https://tr1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + os.environ['riotApiKeY']
  
  
  response = requests.get(API_Riot)
  jsonDataSummoner = response.json()
  calls = {0:'queueType', 1:'tier', 2:'rank', 3:'leaguePoints', 4:'wins', 5:'losses'}
  ranks = []
  try:
    for i in range(3):
      for j in range(6):
        ranks.append(jsonDataSummoner[i][calls[j]])
  except:
    pass
  return ranks
  
#Set the bot prefix
    

#Set the bot command prefix and set the default help to None allowing for a custom help function to be created
bot = commands.Bot(command_prefix='$', help_command=None)

#Bot help function
@bot.command(name='help')
async def help(ctx):
  embed = discord.Embed(title='HELP', description='Commands available for the EnthuLOL Bot', color=discord.Color.red())
  embed.add_field(name='Available servers to use', value="`euw1`, `eun1`, `br1`, `jp1`, `kr`, `la1`, `la2`, `na1`, `oc1`, `ru`, `tr1`", inline=False)
  await ctx.send(embed=embed)

#gets the player level and icon
@bot.command()
async def euw1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('euw1', name)
  summonerRanking = fetchRanks('euw1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def eun1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('eun1', name)
  summonerRanking = fetchRanks('eun1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)


@bot.command()
async def br1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('br1', name)
  summonerRanking = fetchRanks('br1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def jp1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('jp1', name)
  summonerRanking = fetchRanks('jp1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def kr(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('kr', name)
  summonerRanking = fetchRanks('kr', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def la1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('la1', name)
  summonerRanking = fetchRanks('la1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def la2(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('la2', name)
  summonerRanking = fetchRanks('la2', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def na1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('na1', name)
  summonerRanking = fetchRanks('na1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def oc1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('oc1', name)
  summonerRanking = fetchRanks('oc1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def ru(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('ru', name)
  summonerRanking = fetchRanks('ru', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)

@bot.command()
async def tr1(ctx, *nameWithSpaces):
  name = clearNameSpaces(nameWithSpaces)
  summoner = getProfile('tr1', name)
  summonerRanking = fetchRanks('tr1', summoner[3])
  embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
  embed.set_thumbnail(url=summoner[2])

  #Flex
  try:
    tmp = f'{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}'
    embed.add_field(name=summonerRanking[0], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #Solo/Duo
  try:
    tmp = f'{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}'
    embed.add_field(name=summonerRanking[6], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)

    #TFT
  try:
    tmp = f'{summonerRanking[13]} {summonerRanking[14]} • LP: {summonerRanking[15]} • Wins: {summonerRanking[16]} • Losses: {summonerRanking[17]}'
    embed.add_field(name=summonerRanking[12], value=tmp, inline=False)
  except:
    embed.add_field(name='Not Found', value='Player is not ranked yet.', inline=False)
    
  await ctx.send(embed=embed)



@bot.command()
async def Aatrox(ctx):
  champ_name = 'Aatrox'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://avatarfiles.alphacoders.com/298/thumb-150-298650.jpg'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)
  
  
@bot.event
async def on_ready():
  print('Ready...')


#run the bot with the discord bot token
keep_alive()
bot.run(os.environ['token'])
