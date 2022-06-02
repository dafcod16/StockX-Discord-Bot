import discord
from stockx import search

token = "OTgyMDA2ODQ3NzM1MjAxODYy.GeSeZ4.NNujRGlcNKfdPVRTs_T5Afpykd19JezLUPPniI"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.split(' ')[0] == '!stockx':
        query = message.content.replace('!stockx ', '')

        item = search(query)

        embed = discord.Embed(
            title=item['title'],
            url='https://stockx.com/en-gb/' + item['urlKey']
        )
        embed.set_thumbnail(
            url=item['media']['imageUrl']
        )
        embed.add_field(
            name='Colorway',
            value=item['colorway']
        )
        embed.add_field(
            name='Style ID',
            value=item['styleId']
        )
        embed.add_field(
            name='Lowest Ask',
            value= "$" + str(item['market']['lowestAsk'])
        )
        embed.add_field(
            name='Highest Bid',
            value= "$" + str(item['market']['highestBid'])
        )
        embed.add_field(
            name='Last Sale',
            value= "$" + str(item['market']['lastSale'])
        )
        embed.add_field(
            name='Sales Last 72 Hours',
            value=item['market']['salesLast72Hours']
        )
        await message.channel.send(embed=embed)

client.run(token)