import discord

async def send_message(recipient, message):
  return await recipient.send(message)

# Required: title, description, color, author
# Optional: authorurl, icon, thumbnail, image, footer
# new_field: [(name, value, optional boolean), (name, value, optional boolean)]
async def send_embed(recipient, settings):
  test = await recipient.send(embed=get_embed(settings))
  return test

def get_embed(settings):
  if not settings:
    return
  embedVar = discord.Embed(title=settings["title"], description=settings["description"], color=settings["color"]) #required

  e_url = get_optional(settings, "authorurl")
  e_icon_url = get_optional(settings, "icon")
  e_thumbnail = get_optional(settings, "thumbnail")
  e_image = get_optional(settings, "image")
  e_footer_text = get_optional(settings, "footer")

  embedVar.set_author(name=settings["author"], url=e_url, icon_url=e_icon_url)
  embedVar.set_thumbnail(url=e_thumbnail)
  embedVar.set_image(url=e_image)
  embedVar.set_footer(text=e_footer_text)
  
  field_list = settings["new_field"] if "new_field" in settings and settings["new_field"] else []
  
  # field_list is a list of fields, 
  # each field in field_list has 3 indexes,
  # index 1: name of field
  # index 2: value of field
  # index 3: inline (never used and none of us know what the heck this is :100: :monkey:)

  for field in field_list:
    is_inline = field[2] if len(field) > 2 else False
    embedVar.add_field(name=field[0], value=field[1], inline=is_inline)
    
  return embedVar

def get_optional(settings, wanted):
  return settings[wanted] if wanted in settings and settings[wanted] else discord.Embed().Empty


'''feel free to copy from here

# EMBED SETTINGS

settings = {
  # ---------required------------
  # string
  "title" : "[PLACEHOLDER]", 

  # string
  "description" : f"[PLACEHOLDER]",
  
  # hex color code
  "color" : 0x3498db,

  # ---------optional(set to None if unneeded)------------
  # string url
  "titleurl" : None, 
  
  #Note if you have author description keys (ex. authorurl) filled you must have the author key filled as well
  
  # string 
  "author" : None,

  # string url
  "authorurl" : None,

  # string url
  "icon" : None,
  
  # string url
  "thumbnail" : None,
  
  # string url
  "image": None,

  "footer": None,
  
  # field_list is a list of fields, 
  # each field in field_list has 3 indexes,
  # index 1: name of field
  # index 2: value of field
  # index 3: inline
  
  "new_field" : [] 
  # each field should have 3 indexes: "[name, value, inline]"
  
}

'''