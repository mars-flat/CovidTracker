import requests
import json
import send

client = None

async def getCommand(message):
  global client

  if message.author == client.user:
      return False
  cmd = message.content
  

  # ------------------------TODAY----------------------------


  if cmd.lower() == "%c today":
    response = requests.get("https://api.covid19tracker.ca/summary")
    rawData = json.loads(response.text)
    jsonData = rawData["data"][0]
    # print(jsonData)
    settings = {
      # ---------required------------
      # string
      "title" : ("COVID-19 Today (Canada): " + jsonData["latest_date"] + "\n\n"), 

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
      "author" : client.user,

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
      "author" : client.user,

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