import requests
import json
import send
import graph
import os
import discord
import time

client = None

counter = 0

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

  
  # ------------------------LATEST[Provinces]----------------------------


  elif "%p latest" in cmd.lower():
    split = cmd.split()
    if len(split) != 3:
      return await send.send_message(message.channel, "Please specify a province.")
    prov = split[2].upper()

    response = requests.get("https://api.covid19tracker.ca/summary/split")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    found = False
    data = {}
    for i in range(len(jsonData)):
      if jsonData[i]["province"] == prov:
        found = True
        data = jsonData[i]
        break
    
    if not found:
      return await send.send_message(message.channel, "Could not find province `" + prov + "`.")
    
    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 (" + prov + ") as of: " + str(data["date"]) + "\n\n"), 

      # string
      "description" : ("Case count: `" + str(data["change_cases"]) + "`\n\n"
      
      + "Fatality count: `" + str(data["change_fatalities"]) + "`\n\n"
      
      + "Tests completed: `" + str(data["change_tests"]) + "`\n\n"
      
      + "Change in Hospitalizations: `" + str(data["change_hospitalizations"]) + "`\n\n"
      
      + "Change in Critical cases: `" + str(data["change_criticals"]) + "`\n\n"
      
      + "Recovery count: `" + str(data["change_recoveries"]) + "`\n\n\n"),
      
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

  
  # ------------------------TOTAL[Provincial]----------------------------


  elif "%p total" in cmd.lower():
    split = cmd.split()
    if len(split) != 3:
      return await send.send_message(message.channel, "Please specify a province.")
    prov = split[2].upper()

    response = requests.get("https://api.covid19tracker.ca/summary/split")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    found = False
    data = {}
    for i in range(len(jsonData)):
      if jsonData[i]["province"] == prov:
        found = True
        data = jsonData[i]
        break
    
    if not found:
      return await send.send_message(message.channel, "Could not find province `" + prov + "`.")

    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 Totals (" + prov + "): \n\n"), 

      # string
      "description" : ("Total cases: `" + str(data["total_cases"]) + "`\n\n"
      
      + "Total Fatalities: `" + str(data["total_fatalities"]) + "`\n\n"
      
      + "Total Tests: `" + str(data["total_tests"]) + "`\n\n"
      
      + "Total Hospitalizations: `" + str(data["total_hospitalizations"]) + "`\n\n"
      
      + "Total Critical cases: `" + str(data["total_criticals"]) + "`\n\n"

      + "Total Recoveries: `" + str(data["total_recoveries"]) + "`\n\n\n"),
      
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


  # ------------------------VACCINES[Provincial]----------------------------


  elif "%p vac" in cmd.lower():
    split = cmd.split()
    if len(split) != 3:
      return await send.send_message(message.channel, "Please specify a province.")
    prov = split[2].upper()

    response = requests.get("https://api.covid19tracker.ca/summary/split")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    found = False
    data = {}
    for i in range(len(jsonData)):
      if jsonData[i]["province"] == prov:
        found = True
        data = jsonData[i]
        break
    
    if not found:
      return await send.send_message(message.channel, "Could not find province `" + prov + "`.")

    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 Vaccinations (" + prov + "): \n\n"), 

      # string
      "description" : ("Date: " + str(data["date"]) + "\n\n"
        
      + "Change in Vaccinations: `" + str(data["change_vaccinations"]) + "`\n\n"
      
      + "Change in Vaccinated Persons: `" + str(data["change_vaccinated"]) + "`\n\n"
      
      + "Change in Distributed Vaccines: `" + str(data["change_vaccines_distributed"]) + "`\n\n"
      
      + "────────────────\n\n"
      
      + "Total Vaccinations: `" + str(data["total_vaccinations"]) + "`\n\n"
      
      + "Total Persons Vaccinated: `" + str(data["total_vaccinated"]) + "`\n\n"
      
      + "Total Vaccines Distributed: `" + str(data["total_vaccines_distributed"]) + "`\n\n\n"),
      
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


  # ------------------------GRAPH[Cases]----------------------------

  
  elif cmd.lower() == "%c graph cases":
    start = time.time() 

    response = requests.get("https://api.covid19tracker.ca/reports")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    
    xCoords = []
    yCoords = []
    for i in range(len(jsonData) - 1):
      xCoords.append(i)
      if jsonData[i]["change_cases"] != "null":
        yCoords.append(jsonData[i]["change_cases"])
      else:
        yCoords.append(0)
    
    earliestDate = jsonData[0]["date"]
    plot = await graph.createGraph(xCoords, yCoords, earliestDate)
    plot.title('Covid-19 Cases in Canada since ' + earliestDate)
    plot.xlabel('Days Since ' + earliestDate)
    plot.ylabel('Covid-19 Case Count')
    plot.savefig(fname='plot')
    file=discord.File("plot.png", filename = "plot.png")

    end = time.time()

    settings = {
      # ---------required------------
      # string
      "title" : "CovidTracker", 

      # string
      "description" : "Generated in " + '{0:.3f}'.format(end - start) + " seconds.",
      
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

      "footer": None,
      
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


  # ------------------------GRAPH[Fatalities]----------------------------

  
  elif cmd.lower() == "%c graph fatalities":
    start = time.time() 

    response = requests.get("https://api.covid19tracker.ca/reports")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    
    xCoords = []
    yCoords = []
    for i in range(len(jsonData) - 1):
      xCoords.append(i)
      if jsonData[i]["change_fatalities"] != "null":
        yCoords.append(jsonData[i]["change_fatalities"])
      else:
        yCoords.append(0)
    
    earliestDate = jsonData[0]["date"]
    plot = await graph.createGraph(xCoords, yCoords, earliestDate)
    plot.title('Covid-19 Fatalities in Canada since ' + earliestDate)
    plot.xlabel('Days Since ' + earliestDate)
    plot.ylabel('Covid-19 Fatality Count')
    plot.savefig(fname='plot2')
    file=discord.File("plot2.png", filename = "plot2.png")

    end = time.time()

    settings = {
      # ---------required------------
      # string
      "title" : "CovidTracker", 

      # string
      "description" : "Generated in " + '{0:.3f}'.format(end - start) + " seconds.",
      
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
      "image": "attachment://plot2.png",

      "footer": None,
      
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
    os.remove('plot2.png')



  # ------------------------GRAPH[Vaccinations]----------------------------

  
  elif cmd.lower() == "%c graph vac":
    start = time.time() 

    response = requests.get("https://api.covid19tracker.ca/reports")
    rawData = json.loads(response.text)
    jsonData = rawData["data"]
    
    xCoords = []
    yCoords = []
    for i in range(len(jsonData) - 1):
      xCoords.append(i)
      if jsonData[i]["change_vaccinations"] != "null":
        yCoords.append(jsonData[i]["change_vaccinations"])
      else:
        yCoords.append(0)
    
    earliestDate = jsonData[0]["date"]
    plot = await graph.createGraph(xCoords, yCoords, earliestDate)
    plot.title('Covid-19 Vaccinations in Canada since ' + earliestDate)
    plot.xlabel('Days Since ' + earliestDate)
    plot.ylabel('Covid-19 Vaccinations')
    plot.savefig(fname='plot3')
    file=discord.File("plot3.png", filename = "plot3.png")

    end = time.time()

    settings = {
      # ---------required------------
      # string
      "title" : "CovidTracker", 

      # string
      "description" : "Generated in " + '{0:.3f}'.format(end - start) + " seconds.",
      
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
      "image": "attachment://plot3.png",

      "footer": None,
      
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
    os.remove('plot3.png')
  

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
      "**%c latest [province code]** - Gets the latest Covid-19 information in a given province.\n" +
      "**%c total [province code]** - Provides cumulative statistics on Covid-19 in a given province.\n" +
      "**%c vac [province code]** - Gets the latest Covid-19 vaccination statistics in a given province.\n" + 
      "**%c graph cases** - Creates a graph of daily cases of Covid-19 in Canada.\n" +

      "**%c graph fatalities** - Creates a graph of daily cases of Covid-19 in Canada.\n"

      "**%c graph vac** - Creates a graph of daily cases of Covid-19 in Canada.\n",
      
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

      "footer": ("Version 1.4.1"),
      
      # field_list is a list of fields, 
      # each field in field_list has 3 indexes,
      # index 1: name of field
      # index 2: value of field
      # index 3: inline
      
      "new_field" : [] 
      # each field should have 3 indexes: "[name, value, inline]"
      
    }
    await send.send_embed(message.channel, settings)


  