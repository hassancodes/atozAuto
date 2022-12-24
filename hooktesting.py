from discordwebhook import Discord
from secret import urlhook 
print(urlhook)
discord = Discord(url=f"{urlhook}")
discord.post(content="LOL")