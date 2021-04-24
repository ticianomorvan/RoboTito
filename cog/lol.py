import discord
from discord.ext import commands

import datetime

import random

import json

with open('databases/db_leagueoflegends.json') as f:
    data = f.read()
    lol_ch = json.loads(data)


class Lol(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='champpick', aliases=['chpick', 'champick'])
    async def championpick(self, ctx, args):
        guild = ctx.guild

        if args in lol_ch['toplaner_input']:
            top_pick = random.randint(0, 49)
            top_name = lol_ch['toplaner'][top_pick]['name']
            top_header = lol_ch['toplaner'][top_pick]['header']
            top_icon = lol_ch['toplaner'][top_pick]['icon']
            top_ugg = lol_ch['toplaner'][top_pick]['u.gg']
            top_page = lol_ch['toplaner'][top_pick]['lol']

            embed = discord.Embed(
                title=top_name,
                description=top_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Builds, items, hechizos y más:',
                value=f'[U.GG]({top_ugg})',
                inline=False
            )
            embed.add_field(
                name='Información adicional del campeón:',
                value=f'[League of Legends]({top_page})',
                inline=False
            )
            embed.set_thumbnail(
                url=top_icon
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        elif args in lol_ch['jungler_input']:
            jg_pick = random.randint(0, 38)
            jg_name = lol_ch['jungler'][jg_pick]['name']
            jg_header = lol_ch['jungler'][jg_pick]['header']
            jg_icon = lol_ch['jungler'][jg_pick]['icon']
            jg_ugg = lol_ch['jungler'][jg_pick]['u.gg']
            jg_page = lol_ch['jungler'][jg_pick]['lol']

            embed = discord.Embed(
                title=jg_name,
                description=jg_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Builds, items, hechizos y más:',
                value=f'[U.GG]({jg_ugg})',
                inline=False
            )
            embed.add_field(
                name='Información adicional del campeón:',
                value=f'[League of Legends]({jg_page})',
                inline=False
            )
            embed.set_thumbnail(
                url=jg_icon
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        elif args in lol_ch['midlaner_input']:
            mid_pick = random.randint(0, 45)
            mid_name = lol_ch['midlaner'][mid_pick]['name']
            mid_header = lol_ch['midlaner'][mid_pick]['header']
            mid_icon = lol_ch['midlaner'][mid_pick]['icon']
            mid_ugg = lol_ch['midlaner'][mid_pick]['u.gg']
            mid_page = lol_ch['midlaner'][mid_pick]['lol']

            embed = discord.Embed(
                title=mid_name,
                description=mid_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Builds, items, hechizos y más:',
                value=f'[U.GG]({mid_ugg})',
                inline=False
            )
            embed.add_field(
                name='Información adicional del campeón:',
                value=f'[League of Legends]({mid_page})',
                inline=False
            )
            embed.set_thumbnail(
                url=mid_icon
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        elif args in lol_ch['adc_input']:
            adc_pick = random.randint(0, 21)
            adc_name = lol_ch['adc'][adc_pick]['name']
            adc_header = lol_ch['adc'][adc_pick]['header']
            adc_icon = lol_ch['adc'][adc_pick]['icon']
            adc_ugg = lol_ch['adc'][adc_pick]['u.gg']
            adc_page = lol_ch['adc'][adc_pick]['lol']

            embed = discord.Embed(
                title=adc_name,
                description=adc_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Builds, items, hechizos y más:',
                value=f'[U.GG]({adc_ugg})',
                inline=False
            )
            embed.add_field(
                name='Información adicional del campeón:',
                value=f'[League of Legends]({adc_page})',
                inline=False
            )
            embed.set_thumbnail(
                url=adc_icon
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        elif args in lol_ch['support_input']:
            supp_pick = random.randint(0, 32)
            supp_name = lol_ch['support'][supp_pick]['name']
            supp_header = lol_ch['support'][supp_pick]['header']
            supp_icon = lol_ch['support'][supp_pick]['icon']
            supp_ugg = lol_ch['support'][supp_pick]['u.gg']
            supp_page = lol_ch['support'][supp_pick]['lol']

            embed = discord.Embed(
                title=supp_name,
                description=supp_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Builds, items, hechizos y más:',
                value=f'[U.GG]({supp_ugg})',
                inline=False
            )
            embed.add_field(
                name='Información adicional del campeón:',
                value=f'[League of Legends]({supp_page})',
                inline=False
            )
            embed.set_thumbnail(
                url=supp_icon
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        elif args == 'random':
            random_pick = random.randint(0, 155)
            random_name = lol_ch['champions'][random_pick]['name']
            random_header = lol_ch['champions'][random_pick]['header']
            random_icon = lol_ch['champions'][random_pick]['icon']
            random_ugg = lol_ch['champions'][random_pick]['u.gg']
            random_page = lol_ch['champions'][random_pick]['lol']

            embed = discord.Embed(
                title=random_name,
                description=random_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Builds, items, hechizos y más:',
                value=f'[U.GG]({random_ugg})',
                inline=False
            )
            embed.add_field(
                name='Información adicional del campeón:',
                value=f'[League of Legends]({random_page})',
                inline=False
            )
            embed.set_thumbnail(
                url=random_icon
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        else:
            pass


def setup(bot):
    bot.add_cog(Lol(bot))
