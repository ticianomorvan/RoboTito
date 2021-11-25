import json
import random
import nextcord as n
from datetime import datetime

# this function is temporary, until I can set the color of the role
def rColor():
    return random.randint(0, 255)

with open('databases/db_gifs.json', mode='r', encoding='utf-8') as a:
    data = a.read()
    gifs = json.loads(data)

def HugEmbed(author, member, guildName, guildIcon):
    e = n.Embed(
        color=n.Color.from_rgb(rColor(), rColor(), rColor()),
        timestamp=datetime.utcnow()
    )
    e.add_field(
        name='Hugs for all of you',
        value=f'{author} sent a hug to {member}'
    )
    e.set_image(
        url=random.choice(gifs["hug"])
    )
    e.set_footer(text=guildName, icon_url=guildIcon)

    return e