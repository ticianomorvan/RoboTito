import discord
from cog.functions import rbColor
from datetime import datetime, timedelta, timezone
from discord.ext import commands


timezone_icon = '''
https://cdn.discordapp.com/avatars/447266583459528715/bc6d8794326ef2fd57690a852eefde1b.png?size=512
'''


def get_local_time(hours):
    time = str(datetime.now(timezone(timedelta(hours=hours))))[10:][:6]
    return time


class Time(commands.Cog,
           name='Tiempo',
           description='Conoce el tiempo actual.'):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(aliases=['utc', 'greenwich'],
                      help='Conoce la hora (del meridiano de Greenwich)')
    async def utctime(self, ctx):
        e = discord.Embed(title=f'Son las{str(datetime.utcnow())[10:][:6]}'
                                ' (UTC)',
                          color=rbColor())
        e.set_author(name='Tiempo del meridiano de Greenwich',
                     url='https://time.is/es/UTC',
                     icon_url=timezone_icon)
        await ctx.send(embed=e)

    @commands.command(aliases=['tiempodelbot', 'bothour'],
                      help='Conoce la hora de la región del bot.')
    async def bottime(self, ctx):
        e = discord.Embed(title=f'Son las{str(datetime.now())[10:][:6]}',
                          color=rbColor())
        e.set_author(name='Tiempo de la zona horaria del bot',
                     icon_url=timezone_icon)
        await ctx.send(embed=e)

    @commands.command(aliases=['tiempolocal', 'local'],
                      help='Conoce la hora de tu zona horaria.')
    async def localtime(self, ctx, hours: int = None):
        if not hours:
            await ctx.send('Para averiguar la hora de tu zona horaria,'
                           ' ingresá la cantidad de horas de diferencia'
                           ' con el tiempo del meridiano de Greenwich.'
                           ' Por ejemplo, para Argentina (UTC -3)'
                           ' ingresá `-3` después del comando.')
        else:
            e = discord.Embed(title=f'Son las{get_local_time(hours)}',
                              color=rbColor())
            e.set_author(name='Tiempo de tu zona horaria',
                         icon_url=timezone_icon)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Time(bot))
