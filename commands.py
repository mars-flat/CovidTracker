import requests
import json
import send
import graph
import os
import discord

client = None

async def getCommand(message):
  global client

  if message.author == client.user:
      return False
  cmd = message.content
  

  # ------------------------LATEST----------------------------


  if cmd.lower() == "%c latest":
    response = requests.get("https://api.covid19tracker.ca/summary")
    rawData = json.loads(response.text)
    jsonData = rawData["data"][0]
    # print(jsonData)
    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 (Canada) as of: " + jsonData["latest_date"] + "\n\n"), 

      # string
      "description" : ("Case count: `" + jsonData["change_cases"] + "`\n\n"
      
      + "Fatality count: `" + jsonData["change_fatalities"] + "`\n\n"
      
      + "Tests completed: `" + jsonData["change_tests"] + "`\n\n"
      
      + "Change in Hospitalizations: `" + jsonData["change_hospitalizations"] + "`\n\n"
      
      + "Change in Critical cases: `" + jsonData["change_criticals"] + "`\n\n"
      
      + "Recovery count: `" + jsonData["change_recoveries"] + "`\n\n\n"),
      
      # hex color code
      "color" : 0x3498db,

      # ---------optional(set to None if unneeded)------------
      # string url
      "titleurl" : None, 
      
      #Note if you have author description keys (ex. authorurl) filled you must have the author key filled as well
      
      # string 
      "author" : "CovidTracker",

      # string url
      "authorurl" : None,

      # string url
      "icon" : "https://cdn.discordapp.com/attachments/797302970210451498/812747573890514984/9k.png",
      
      # string url
      "thumbnail" : client.user.avatar_url,
      
      # string url
      "image": None,

      "footer": ("Data is taken from an API that updates as fast as possible. Actual counts may vary slightly."),
      
      # field_list is a list of fields, 
      # each field in field_list has 3 indexes,
      # index 1: name of field
      # index 2: value of field
      # index 3: inline
      
      "new_field" : [] 
      # each field should have 3 indexes: "[name, value, inline]"
      
    }
    await send.send_embed(message.channel, settings)


  # ------------------------TOTAL----------------------------


  elif cmd.lower() == "%c total":
    response = requests.get("https://api.covid19tracker.ca/summary")
    rawData = json.loads(response.text)
    jsonData = rawData["data"][0]
    # print(jsonData)
    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 Totals (Canada): \n\n"), 

      # string
      "description" : ("Total cases: `" + jsonData["total_cases"] + "`\n\n"
      
      + "Total Fatalities: `" + jsonData["total_fatalities"] + "`\n\n"
      
      + "Total Tests: `" + jsonData["total_tests"] + "`\n\n"
      
      + "Total Hospitalizations: `" + jsonData["total_hospitalizations"] + "`\n\n"
      
      + "Total Critical cases: `" + jsonData["total_criticals"] + "`\n\n"
      
      + "Total Recoveries: `" + jsonData["total_recoveries"] + "`\n\n\n"),
      
      # hex color code
      "color" : 0x3498db,

      # ---------optional(set to None if unneeded)------------
      # string url
      "titleurl" : None, 
      
      #Note if you have author description keys (ex. authorurl) filled you must have the author key filled as well
      
      # string 
      "author" : "CovidTracker",

      # string url
      "authorurl" : None,

      # string url
      "icon" : "https://cdn.discordapp.com/attachments/797302970210451498/812747573890514984/9k.png",
      
      # string url
      "thumbnail" : client.user.avatar_url,
      
      # string url
      "image": None,

      "footer": ("Data is taken from an API that updates as fast as possible. Actual counts may vary slightly."),
      
      # field_list is a list of fields, 
      # each field in field_list has 3 indexes,
      # index 1: name of field
      # index 2: value of field
      # index 3: inline
      
      "new_field" : [] 
      # each field should have 3 indexes: "[name, value, inline]"
      
    }
    await send.send_embed(message.channel, settings)


  # ------------------------VACCINES----------------------------


  elif cmd.lower() == "%c vac":
    response = requests.get("https://api.covid19tracker.ca/summary")
    rawData = json.loads(response.text)
    jsonData = rawData["data"][0]
    # print(jsonData)
    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 Vaccinations (Canada): \n\n"), 

      # string
      "description" : ("Date: " + jsonData["latest_date"] + "\n\n"
        
      + "Change in Vaccinations: `" + jsonData["change_vaccinations"] + "`\n\n"
      
      + "Change in Vaccinated Persons: `" + jsonData["change_vaccinated"] + "`\n\n"
      
      + "Change in Distributed Vaccines: `" + jsonData["change_vaccines_distributed"] + "`\n\n"
      
      + "────────────────\n\n"
      
      + "Total Vaccinations: `" + jsonData["total_vaccinations"] + "`\n\n"
      
      + "Total Persons Vaccinated: `" + jsonData["total_vaccinated"] + "`\n\n"
      
      + "Total Vaccines Distributed: `" + jsonData["total_vaccines_distributed"] + "`\n\n\n"),
      
      # hex color code
      "color" : 0x3498db,

      # ---------optional(set to None if unneeded)------------
      # string url
      "titleurl" : None, 
      
      #Note if you have author description keys (ex. authorurl) filled you must have the author key filled as well
      
      # string 
      "author" : "CovidTracker",

      # string url
      "authorurl" : None,

      # string url
      "icon" : "https://cdn.discordapp.com/attachments/797302970210451498/812747573890514984/9k.png",
      
      # string url
      "thumbnail" : "https://cdn.discordapp.com/attachments/797302970210451498/813054362477658112/1_5270930.png",
      
      # string url
      "image": None,

      "footer": ("Data is taken from an API that updates as fast as possible. Actual counts may vary slightly."),
      
      # field_list is a list of fields, 
      # each field in field_list has 3 indexes,
      # index 1: name of field
      # index 2: value of field
      # index 3: inline
      
      "new_field" : [] 
      # each field should have 3 indexes: "[name, value, inline]"
      
    }
    await send.send_embed(message.channel, settings)


  # ------------------------GRAPH----------------------------

  
  elif cmd.lower() == "%c graph":
    response = requests.get("https://api.covid19tracker.ca/reports")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    
    xCoords = []
    yCoords = []
    for i in range(len(jsonData) - 1):
      xCoords.append(i)
      yCoords.append(jsonData[i]["change_cases"])
    
    earliestDate = jsonData[0]["date"]
    plot = await graph.createGraph(xCoords, yCoords, earliestDate)
    plot.savefig(fname='plot')
    file=discord.File("plot.png", filename = "plot.png")

    settings = {
      # ---------required------------
      # string
      "title" : "CovidTracker", 

      # string
      "description" : "Graph",
      
      # hex color code
      "color" : 0x3498db,

      # ---------optional(set to None if unneeded)------------
      # string url
      "titleurl" : "https://api.covid19tracker.ca/", 
      
      #Note if you have author description keys (ex. authorurl) filled you must have the author key filled as well
      
      # string 
      "author" : "CovidTracker",

      # string url
      "authorurl" : None,

      # string url
      "icon" : "https://cdn.discordapp.com/attachments/797302970210451498/812747573890514984/9k.png",
      
      # string url
      "thumbnail" : None,
      
      # string url
      "image": "attachment://plot.png",

      "footer": ("Version 1.2.5"),
      
      # field_list is a list of fields, 
      # each field in field_list has 3 indexes,
      # index 1: name of field
      # index 2: value of field
      # index 3: inline
      
      "new_field" : [] 
      # each field should have 3 indexes: "[name, value, inline]"
      
    }
    await send.send_file_embed(message.channel, file, settings)
    plot.clf() 
    os.remove('plot.png')
  

  # ------------------------HELP----------------------------


  elif cmd.lower() == "%c help":
    settings = {
      # ---------required------------
      # string
      "title" : "CovidTracker", 

      # string
      "description" : "**API-based Covid 19 Tracker**\n" + 
      "This bot provides up-to-date(Based on API) information on Covid-19 in Canada.\n\n" + 

      "**Current Commands:** \n\n" + 
      "**%c latest** - Gets the latest Covid-19 information in Canada.\n" + 
      "**%c total** - Provides cumulative statistics on Covid-19 in Canada.\n" + 
      "**%c vac** - Gets the latest Covid-19 vaccination statistics in Canada.\n" +
      "**%c graph** - Creates a graph of daily cases of Covid-19 in Canada.\n",
      
      # hex color code
      "color" : 0x3498db,

      # ---------optional(set to None if unneeded)------------
      # string url
      "titleurl" : "https://api.covid19tracker.ca/", 
      
      #Note if you have author description keys (ex. authorurl) filled you must have the author key filled as well
      
      # string 
      "author" : "CovidTracker",

      # string url
      "authorurl" : None,

      # string url
      "icon" : "https://cdn.discordapp.com/attachments/797302970210451498/812747573890514984/9k.png",
      
      # string url
      "thumbnail" : None,
      
      # string url
      "image": None,

      "footer": ("Version 1.2.7"),
      
      # field_list is a list of fields, 
      # each field in field_list has 3 indexes,
      # index 1: name of field
      # index 2: value of field
      # index 3: inline
      
      "new_field" : [] 
      # each field should have 3 indexes: "[name, value, inline]"
      
    }
    await send.send_embed(message.channel, settings)


  