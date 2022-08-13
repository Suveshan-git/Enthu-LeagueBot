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


#Commands to fetch player details from all the league regions
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

#Commands for champion title, lore and image
async def aatrox(ctx):
  champ_name = 'Aatrox'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt570145160dd39dca/5db05fa8347d1c6baa57be25/RiotX_ChampionList_aatrox.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def ahri(ctx):
  champ_name = 'Ahri'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt1259276b6d1efa78/5db05fa86e8b0c6d038c5ca2/RiotX_ChampionList_ahri.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def akali(ctx):
  champ_name = 'Akali'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt80ff58fe809777ff/5db05fa8adc8656c7d24e7d6/RiotX_ChampionList_akali.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def akshan(ctx):
  champ_name = 'Akshan'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltdd84b33ec501c137/60f9ede33f40e5481e85c0c6/RiotX_ChampionList_akshan_v2.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def alistar(ctx):
  champ_name = 'Alistar'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt3b366925d2fd8fdb/5db05fa856458c6b3fc1750b/RiotX_ChampionList_alistar.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def amumu(ctx):
  champ_name = 'Amumu'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt40dfbe48a61c439f/5db05fa80b39e86c2f83dbf9/RiotX_ChampionList_amumu.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def anivia(ctx):
  champ_name = 'Anivia'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt3d24a1482453088a/5db05fa8df78486c826dcce8/RiotX_ChampionList_anivia.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def annie(ctx):
  champ_name = 'Annie'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt28c708665427aef6/5db05fa89481396d6bdd01a6/RiotX_ChampionList_annie.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def aphelios(ctx):
  champ_name = 'Aphelios'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aphelios_0.jpg'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def ashe(ctx):
  champ_name = 'Ashe'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt943aae038e2dee98/5db05fa8e9effa6ba5295f91/RiotX_ChampionList_ashe.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def aurelionsol(ctx):
  champ_name = 'AurelionSol'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt5dd3569fc67d6664/5db05fa8bd24496c390ae4d8/RiotX_ChampionList_aurelionsol.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def azir(ctx):
  champ_name = 'Azir'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt0e3f847946232167/5db05fa889fb926b491ed7ff/RiotX_ChampionList_azir.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def bard(ctx):
  champ_name = 'Bard'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltbbe3ce0c0ae1305b/5db05fb23a326d6df6c0e7b3/RiotX_ChampionList_bard.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def belveth(ctx):
  champ_name = 'Belveth'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt9f765d79de67f50e/629ea266a3e9730f695d114a/RiotX_ChampionList_belveth.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def blitzcrank(ctx):
  champ_name = 'Blitzcrank'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltd7ef7e56ce1fe17b/5db05fb26af83b6d7032c8f8/RiotX_ChampionList_blitzcrank.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def brand(ctx):
  champ_name = 'Brand'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltc8ca2e9bba653dda/5db05fb2dc674266df3d5d30/RiotX_ChampionList_brand.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def braum(ctx):
  champ_name = 'Braum'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltd140e30fa86d6ddd/5db05fb2242f426df132f95d/RiotX_ChampionList_braum.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def caitlyn(ctx):
  champ_name = 'Caitlyn'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt014f4b6fc9bacd10/61b1eb901d158d4007de9685/RiotX_ChampionList_caitlyn_v2.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def camille(ctx):
  champ_name = 'Camille'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt413fcd7681fe0773/5db05fb089fb926b491ed805/RiotX_ChampionList_camille.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def cassiopeia(ctx):
  champ_name = 'Cassiopeia'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blte189be8189da97ea/5db05fb1bd24496c390ae4de/RiotX_ChampionList_cassiopeia.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@bot.command()
async def chogath(ctx):
  champ_name = 'Chogath'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt4dfb71de3ddc8166/5db05fb13a326d6df6c0e7ad/RiotX_ChampionList_chogath.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def corki(ctx):
  champ_name = 'Corki'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltdd918c4d0a86347a/5db05fb1df78486c826dccee/RiotX_ChampionList_corki.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def darius(ctx):
  champ_name = 'Darius'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt38b52be4a2cb1004/5db05fb19481396d6bdd01ac/RiotX_ChampionList_darius.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def diana(ctx):
  champ_name = 'Diana'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt56570083d2a5e20e/5db05fbc823d426762825fdf/RiotX_ChampionList_diana.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def drmundo(ctx):
  champ_name = 'DrMundo'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blte88a3d7e9e408904/61b1ea136a78b87751002a68/RiotX_ChampionList_drmundo_v2.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def draven(ctx):
  champ_name = 'Draven'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltc0be728e4cbb8f2a/5db05fbc89fb926b491ed80b/RiotX_ChampionList_draven.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def ekko(ctx):
  champ_name = 'Ekko'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltf22ba7e6328e4376/5db05fbd242f426df132f963/RiotX_ChampionList_ekko.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


@bot.command()
async def Karthus(ctx):
  champ_name = 'Karthus'
  API_Riot = 'http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion/' + champ_name + '.json'

  response = requests.get(API_Riot)
  jsonData = response.json()
  name = jsonData['data'][champ_name]['name']
  title = jsonData['data'][champ_name]['title']
  lore = jsonData['data'][champ_name]['lore']
  image = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt69b8fad9d1e78514/5db05fd7df78486c826dcd0c/RiotX_ChampionList_karthus.jpg?quality=90&width=250'
  embed = discord.Embed(title=name, description=title, color=0xFFD500)
  embed.add_field(name='Lore', value=lore)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)




  
#Ready status of bot on successful execution
@bot.event
async def on_ready():
  print('Ready...')


#run the bot with the discord bot token
keep_alive()
bot.run(os.environ['token'])
