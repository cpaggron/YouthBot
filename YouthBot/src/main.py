import discord
from discord.ext import commands
import random
from directory import Directory
import os
import json
import asyncio
from discord.ext import menus

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 'c+', intents=intents)

@client.event
async def on_ready():
    print('Bot is Ready')

if os.path.exists('info.json'):
    with open ('info.json', 'r') as ILoveYouYouLoveMeWeAreOneBigFamily:
        info = json.load(ILoveYouYouLoveMeWeAreOneBigFamily)
else:
    info = {}

@client.command()
async def ping(ctx):
    await ctx.send(f'({client.latency * 10000})ms pong!')

# Info Commands Below ----------------------------------------------------------------------------------------------------

@client.command(aliases=["info", "i"])
async def information(ctx, *, person=None):

    with open("info.json", "r") as file:
        info = json.load(file)

    if person == None:
        user = str(ctx.author.id)
        person = ctx.author
    else:
        user = str(person.id)

    discriminator = str(person)[-5:]

    embed = discord.Embed(title=f"{person.name}", description=f"*{discriminator}*", color=info[user]["color"])
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="Name", value=info[user]["name"], inline=True)
    embed.add_field(name="Address", value=f'||{info[user]["address"]}||', inline=True)
    embed.add_field(name="Age", value=info[user]["age"], inline=True)
    embed.add_field(name="Grade", value=info[user]["grade"], inline=True)
    embed.add_field(name="School", value=info[user]["school"], inline=True)
    embed.add_field(name="Birthday", value=info[user]["birthday"], inline=True)
    embed.add_field(name="Ice Cream/Frozen Yoghurt", value=info[user]["ice cream"], inline=True)
    embed.add_field(name="Description", value=info[user]["about"], inline=False)
    embed.set_footer(text="One Youth Fellowship")
    await ctx.send(embed=embed)

@client.command()
async def collectInfo(ctx):
    if ctx.author.id == 468476776104853505:
        await ctx.send("Collecting Info")
        guild = ctx.guild
        for users in guild.members:
            user = Directory(users.id)
            user.create()
        await ctx.send("Finished Collecting Info")
    else:
        await ctx.send("You aren't allowed to use that!")


@client.command()
async def update(ctx, *, select:str=None):

    # List of possible selections (I made the list to make future reference easier)
    selections = ["name", "age", "grade", "school", "email", "color", "birthday", "address", "ice cream", "about"]

    # Check for argument
    if select == None:
        q = ""
        for selection in selections:
            q += f"{selection}\n"
        embed = discord.Embed(title="Update", description=f"Here are the things you can update. (Type `c+update [category]`):\n```\n{q}\n```", color=0)
        await ctx.send(embed=embed)

    elif select in selections:
        user = Directory(ctx.author.id)

        if select == "name":
            await ctx.send("Type your name")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} You have set your name to `{value}`")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "ice cream":
            await ctx.send("What's your favorite ice cream")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} You have set your favorite ice cream to `{value}`")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "about":
            await ctx.send("Tell us a little about yourself.")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=600)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Changes saved")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "email":
            await ctx.send("Type your email")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Changes saved")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "grade":
            await ctx.send("Type your grade. (As integer)")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Your grade as been set to `{value}`")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "age":
            await ctx.send("Type your age. (As integer)")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Your age as been set to `{value}`")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "school":
            await ctx.send("What's your school?")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Your school as been set to `{value}`")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "address":
            await ctx.send("Enter your address. (123 Street Rd.)")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Your address as been set to ||`{value}`||")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "birthday":
            await ctx.send("Enter your birthday. ([M]M/[D]D/YYYY)")
            try:
                reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                value = str(reply.content)
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.author.mention} Your address as been set to `{value}`")
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} You took too long!")

        elif select == "color":
            # Create list of colors
            colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "white"]

            q = ''
            for color in colors:
                q += f"{color}\n"
                print(color)

            msg = await ctx.send(f"{ctx.author.mention} Type one of the following corresponding with your favorite color.\n```{q}\n```")
            # Add reactions
            
            reply = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)

            if str(reply) == "red":
                await msg.edit(content="Your color has been changed to red!")
                value = 15158332

            elif str(reply) == "orange":
                await msg.edit(content="Your color has been changed to orange!")
                value = 15105570

            elif str(reply) == "yellow":
                await msg.edit(content="Your color has been changed to yellow!")
                value = 15844367

            elif str(reply) == "green":
                await msg.edit(content="Your color has been changed to green!")
                value = 3066993

            elif str(reply) == "blue":
                await msg.edit(content="Your color has been changed to blue!")
                value = 3447003

            elif str(reply) == "purple":
                await msg.edit(content="Your color has been changed to purple!")
                value = 10181046

            elif str(reply) == "brown":
                await msg.edit(content="Your color has been changed to brown!")
                value = 11027200

            elif str(reply) == "black":
                await msg.edit(content="Your color has been changed to black!")
                value = 0

            elif str(reply) == "white":
                await msg.edit(content="Your color has been changed to white!")
                value = "#ffffff"

            else:
                await ctx.send(f"`{str(reply)}` is not a valid color!")
                value = 0

        try:      
            user.edit(select, value)
        except UnboundLocalError:
            pass

    else:
        await ctx.send(f"Invalid argument: `{select}`")

# --------------------------------------------------------------------------------------------------------------------

@client.command()
async def poll(ctx, question, *options):
    lll = 0
    await ctx.channel.purge(limit=1)
    reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
    if len(options) > len(reactions):
        await ctx.send('You cannot have more than 10 options in your poll!')
    elif len(options) == 1:
        await ctx.send('You need more than one option in your poll!')
    elif len(options) == None:
        embed = discord.Embed(title=question, description="Yes/No", color=0)
        embed.set_footer(text=f"Poll made by {ctx.author.name}")
        hi = await ctx.send(embed=embed)
        await hi.add_reaction("✅")
        await hi.add_reaction("❌")
    elif question == None:
        await ctx.send('You need a question for your poll!')
    else:
        q = ''
        for i in range(len(options)):
            q += f'__{reactions[lll]} {options[i]}__\n\n'
            lll += 1
        embed = discord.Embed(title=question, description=q, color=0)
        embed.set_footer(text=f"Poll made by {ctx.author.name}")
        hi = await ctx.send(embed=embed)
        lll = 0
        for x in range(len(options)):
            await hi.add_reaction(reactions[x])

# Sends welcome message and updates info when a member joins the server
@client.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}!")
    user = Directory(member.id)
    user.create()

# This code below looks like beginner code but I made this command when I just started python 
# and just copy and pasted it here. Too much work to convert it into random.choice().
# I might change it after I release this.
@client.command()
async def verse(ctx):
    verse = random.randint(1, 100)
    if verse == 1:
        embed = discord.Embed(title="Random Bible Verse", description="Here is the random Bible verse", color=11027200)
        embed.add_field(name="John 3:16", value="For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.", inline=False)
        await ctx.send(embed=embed)
    if verse == 2:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Corinthians 13:4-5", value="Love is patient and kind; love does not envy or boast; it is not arrogant or rude. It does not insist on its own way; it is not irritable or resentful.")
        await ctx.send(embed=embed)
        
    if verse == 3:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Thesselonians 5:16-18", value="Rejoice always, pray without ceasing, give thanks in all circumstances; for this is the will of God in Christ Jesus for you.")
        await ctx.send(embed=embed)
    
    if verse == 4:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Philipians 4:6-7", value="Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.")
        await ctx.send(embed=embed)
    
    if verse == 5:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Deuteronomy 6:6-7", value="And these words that I command you today shall be on your heart. You shall teach them diligently to your children, and shall talk of them when you sit in your house, and when you walk by the way, and when you lie down, and when you rise.")
        await ctx.send(embed=embed)

    if verse == 6:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Mark 11:24", value="Therefore I tell you, whatever you ask in prayer, believe that you have received it, and it will be yours.")
        await ctx.send(embed=embed)

    if verse == 7:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Corinthians 16:14", value="Let all that you do be done in love.")
        await ctx.send(embed=embed)

    if verse == 8:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 16:3", value="Commit your work to the Lord, and your plans will be established.")
        await ctx.send(embed=embed)

    if verse == 9:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Ephesians 3:16-17", value="That according to the riches of his glory he may grant you to be strengthened with power through his Spirit in your inner being, so that Christ may dwell in your hearts through faith—that you, being rooted and grounded in love.")
        await ctx.send(embed=embed)

    if verse == 10:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 143:8", value="Let me hear in the morning of your steadfast love, for in you I trust. Make me know the way I should go, for to you I lift up my soul.")
        await ctx.send(embed=embed)

    if verse == 11:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Numbers 6:24-26", value="The Lord bless you and keep you; the Lord make his face to shine upon you and be gracious to you; the Lord lift up his countenance upon you and give you peace.")
        await ctx.send(embed=embed)

    if verse == 12:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Ephesians 4:2", value="With all humility and gentleness, with patience, bearing with one another in love.")
        await ctx.send(embed=embed)

    if verse == 13:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Corinthians 5:7", value="For we walk by faith, not by sight.")
        await ctx.send(embed=embed)

    
    if verse == 14:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Isaiah 41:10", value="Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.")
        await ctx.send(embed=embed) 

    if verse == 15:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Exodus 23:25", value="You shall serve the Lord your God, and he will bless your bread and your water, and I will take sickness away from among you.")
        await ctx.send(embed=embed)

    if verse == 16:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Acts 16:31", value="And they said, Believe in the Lord Jesus, and you will be saved, you and your household.")
        await ctx.send(embed=embed)

    if verse == 17:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Isaiah 40:31", value="But they who wait for the Lord shall renew their strength; they shall mount up with wings like eagles; they shall run and not be weary; they shall walk and not faint.")
        await ctx.send(embed=embed)

    if verse == 18:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Jeremiah 29:11", value="For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.")
        await ctx.send(embed=embed)

    if verse == 19:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Hebrews 11:1", value="Now faith is the assurance of things hoped for, the conviction of things not seen.")
        await ctx.send(embed=embed)

    if verse == 20:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 20:4", value="May he grant you your heart's desire and fulfill all your plans!")
        await ctx.send(embed=embed)

    if verse == 21:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Colossions 3:23-24", value="Whatever you do, work heartily, as for the Lord and not for men, knowing that from the Lord you will receive the inheritance as your reward. You are serving the Lord Christ.")
        await ctx.send(embed=embed)

    if verse == 22:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 3:3-4", value="Let not steadfast love and faithfulness forsake you; bind them around your neck; write them on the tablet of your heart. So you will find favor and good success in the sight of God and man.")
        await ctx.send(embed=embed)

    if verse == 23:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans 15:13", value="May the God of hope fill you with all joy and peace in believing, so that by the power of the Holy Spirit you may abound in hope.")
        await ctx.send(embed=embed)

    if verse == 24:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Corinthians 9:7", value="Each one must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver.")
        await ctx.send(embed=embed)

    if verse == 25:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Colossions 3:14", value="And above all these put on love, which binds everything together in perfect harmony.")
        await ctx.send(embed=embed)

    if verse == 26:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 John 5:14", value="And this is the confidence that we have toward him, that if we ask anything according to his will he hears us.")
        await ctx.send(embed=embed)

    if verse == 27:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 3:5-6", value="Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.")
        await ctx.send(embed=embed)

    if verse == 28:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 John 4:16", value="So we have come to know and to believe the love that God has for us. God is love, and whoever abides in love abides in God, and God abides in him.")
        await ctx.send(embed=embed)

    if verse == 29:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 121:7-8", value="The Lord will keep you from all evil; he will keep your life. The Lord will keep your going out and your coming in from this time forth and forevermore.")
        await ctx.send(embed=embed)

    if verse == 30:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 20:4", value="May he grant you your heart's desire and fulfill all your plans!")
        await ctx.send(embed=embed)

    if verse == 31:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 56:3", value="When I am afraid, I put my trust in you.")
        await ctx.send(embed=embed)

    if verse == 32:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 20:4", value="May he grant you your heart's desire and fulfill all your plans!")
        await ctx.send(embed=embed)

    if verse == 33:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Chronicles 7:14", value="If my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land.")
        await ctx.send(embed=embed)

    if verse == 34:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 20:4", value="May he grant you your heart's desire and fulfill all your plans!")
        await ctx.send(embed=embed)

    if verse == 35:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Corinthians 15:58", value="Therefore, my beloved brothers, be steadfast, immovable, always abounding in the work of the Lord, knowing that in the Lord your labor is not in vain.")
        await ctx.send(embed=embed)

    if verse == 36:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Galatians 3:26-27", value="For in Christ Jesus you are all sons of God, through faith. For as many of you as were baptized into Christ have put on Christ.")
        await ctx.send(embed=embed)

    if verse == 37:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="John 11:25-26", value="Jesus said to her, “I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live, and everyone who lives and believes in me shall never die. Do you believe this?”")
        await ctx.send(embed=embed)

    if verse == 38:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 17:9", value="Whoever covers an offense seeks love, but he who repeats a matter separates close friends.")
        await ctx.send(embed=embed)

    if verse == 39:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans 12:12", value="Rejoice in hope, be patient in tribulation, be constant in prayer.")
        await ctx.send(embed=embed)

    if verse == 40:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Isaiah 43:2", value="When you pass through the waters, I will be with you; and through the rivers, they shall not overwhelm you; when you walk through fire you shall not be burned, flame shall not consume you.")
        await ctx.send(embed=embed)

    if verse == 41:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Corinthians 1:10", value="I appeal to you, brothers, by the name of our Lord Jesus Christ, that all of you agree, and that there be no divisions among you, but that you be united in the same mind and the same judgment.")
        await ctx.send(embed=embed)

    if verse == 42:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 11:25", value="Whoever brings blessing will be enriched, and one who waters will himself be watered.")
        await ctx.send(embed=embed)

    if verse == 43:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Mark 9:23", value="And Jesus said to him, “‘If you can’! All things are possible for one who believes.”")
        await ctx.send(embed=embed)

    if verse == 44:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Corinthians 13:13", value="So now faith, hope, and love abide, these three; but the greatest of these is love.")
        await ctx.send(embed=embed)

    if verse == 45:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Colossians 4:2", value="Continue steadfastly in prayer, being watchful in it with thanksgiving.")
        await ctx.send(embed=embed)

    if verse == 46:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Isaiah 25:1", value="O Lord, you are my God; I will exalt you; I will praise your name, for you have done wonderful things, plans formed of old, faithful and sure.")
        await ctx.send(embed=embed)

    if verse == 47:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Ephesians 5-15:16", value="Look carefully then how you walk, not as unwise but as wise, making the best use of the time, because the days are evil.")
        await ctx.send(embed=embed)

    if verse == 48:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="John 16:33", value="I have said these things to you, that in me you may have peace. In the world you will have tribulation. But take heart; I have overcome the world.")
        await ctx.send(embed=embed)

    if verse == 49:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Joshua 1:9", value="Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go.")
        await ctx.send(embed=embed)

    if verse == 50:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Chronicles 29:14", value="But who am I, and what is my people, that we should be able thus to offer willingly? For all things come from you, and of your own have we given you.")
        await ctx.send(embed=embed)

    if verse == 51:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Deuteronomy 31:8", value="It is the Lord who goes before you. He will be with you; he will not leave you or forsake you. Do not fear or be dismayed.")
        await ctx.send(embed=embed)

    if verse == 52:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="James 1:6", value="But let him ask in faith, with no doubting, for the one who doubts is like a wave of the sea that is driven and tossed by the wind.")
        await ctx.send(embed=embed)

    if verse == 53:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Corinthians 1:3-4", value="Blessed be the God and Father of our Lord Jesus Christ, the Father of mercies and God of all comfort, who comforts us in all our affliction, so that we may be able to comfort those who are in any affliction, with the comfort with which we ourselves are comforted by God.")
        await ctx.send(embed=embed)

    if verse == 54:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Isaiah 49:15-16", value="Can a woman forget her nursing child, that she should have no compassion on the son of her womb? Even these may forget, yet I will not forget you. Behold, I have engraved you on the palms of my hands; your walls are continually before me.")
        await ctx.send(embed=embed)

    if verse == 55:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Hebrews 4:12", value="For the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart.")
        await ctx.send(embed=embed)

    if verse == 56:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Ephesians 4:32", value="Be kind to one another, tenderhearted, forgiving one another, as God in Christ forgave you.")
        await ctx.send(embed=embed)

    if verse == 57:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 133:1", value="Behold, how good and pleasant it is when brothers dwell in unity!")
        await ctx.send(embed=embed)

    if verse == 58:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans Proverbs 21:21", value="Whoever pursues righteousness and kindness will find life, righteousness, and honor.")
        await ctx.send(embed=embed)

    if verse == 59:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 2:6", value="For the Lord gives wisdom ;from his mouth come knowledge and understanding. Rejoice in hope, be patient in tribulation, be constant in prayer.")
        await ctx.send(embed=embed)

    if verse == 60:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 22:6", value="Train up a child in the way he should go; even when he is old he will not depart from it.")
        await ctx.send(embed=embed)

    if verse == 61:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Hebrews 10:24-25", value="And let us consider how to stir up one another to love and good works, not neglecting to meet together, as is the habit of some, but encouraging one another, and all the more as you see the Day drawing near.")
        await ctx.send(embed=embed)

    if verse == 62:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Jeremiah 29:12", value="Then you will call upon me and come and pray to me, and I will hear you.")
        await ctx.send(embed=embed)

    if verse == 63:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 18:16", value="A man's gift makes room for him and brings him before the great.")
        await ctx.send(embed=embed)

    if verse == 64:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 6:20", value="My son, keep your father's commandment, and forsake not your mother's teaching.")
        await ctx.send(embed=embed)

    if verse == 65:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Acts 16:25", value="About midnight Paul and Silas were praying and singing hymns to God, and the prisoners were listening to them.")
        await ctx.send(embed=embed)

    if verse == 66:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 150:6", value="Let everything that has breath praise the Lord! Praise the Lord!")
        await ctx.send(embed=embed)

    if verse == 67:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="James 1:22", value="But be doers of the word, and not hearers only, deceiving yourselves.")
        await ctx.send(embed=embed)

    if verse == 68:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="John 11:40", value="Jesus said to her, “Did I not tell you that if you believed you would see the glory of God?”")
        await ctx.send(embed=embed)

    if verse == 69:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 73:26", value="My flesh and my heart may fail, but God is the strength of my heart and my portion forever.")
        await ctx.send(embed=embed)

    if verse == 70:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Thessalonians 15:1", value="Therefore encourage one another and build one another up, just as you are doing.")
        await ctx.send(embed=embed)

    if verse == 71:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="John 15:13", value="Greater love has no one than this, that someone lay down his life for his friends.")
        await ctx.send(embed=embed)

    if verse == 72:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 John 4:19", value="We love because he first loved us.")
        await ctx.send(embed=embed)

    if verse == 73:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Ephesians 5:25-26", value="Husbands, love your wives, as Christ loved the church and gave himself up for her, that he might sanctify her, having cleansed her by the washing of water with the word.")
        await ctx.send(embed=embed)

    if verse == 74:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans 11:36", value="For from him and through him and to him are all things. To him be glory forever. Amen.")
        await ctx.send(embed=embed)

    if verse == 75:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 peter 3:3-4", value="Do not let your adorning be external—the braiding of hair and the putting on of gold jewelry, or the clothing you wear— but let your adorning be the hidden person of the heart with the imperishable beauty of a gentle and quiet spirit, which in God's sight is very precious.")
        await ctx.send(embed=embed)

    if verse == 76:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Timothy 3:16-17", value="AAll Scripture is breathed out by God and profitable for teaching, for reproof, for correction, and for training in righteousness, that the man of God may be complete, equipped for every good work.")
        await ctx.send(embed=embed)

    if verse == 77:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 27:19", value="As in water face reflects face, so the heart of man reflects the man.")
        await ctx.send(embed=embed)

    if verse == 78:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Chronicles 16:34", value="Oh give thanks to the Lord, for he is good; for his steadfast love endures forever!")
        await ctx.send(embed=embed)

    if verse == 79:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Matthew 19:14", value="But Jesus said, “Let the little children come to me and do not hinder them, for to such belongs the kingdom of heaven.”")
        await ctx.send(embed=embed)

    if verse == 80:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 147:3", value="A man's gift makes room for him and brings him before the great.")
        await ctx.send(embed=embed)

    if verse == 81:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Galatians 5:22-23", value="But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control; against such things there is no law.")
        await ctx.send(embed=embed)

    if verse == 82:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 42:11", value="Why are you cast down, O my soul, and why are you in turmoil within me? Hope in God; for I shall again praise him, my salvation and my God.")
        await ctx.send(embed=embed)

    if verse == 83:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 Corinthians 6:9-10", value="Or do you not know that the unrighteous will not inherit the kingdom of God? Do not be deceived: neither the sexually immoral, nor idolaters, nor adulterers, nor men who practice homosexuality, nor thieves, nor the greedy, nor drunkards, nor revilers, nor swindlers will inherit the kingdom of God.")
        await ctx.send(embed=embed)

    if verse == 84:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Philipians 2:3", value="Do nothing from selfish ambition or conceit, but in humility count others more significant than yourselves.")
        await ctx.send(embed=embed)

    if verse == 85:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 4:23", value="Keep your heart with all vigilance, for from it flow the springs of life.")
        await ctx.send(embed=embed)

    if verse == 86:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Psalm 119:105", value="Your word is a lamp to my feet and a light to my path.")
        await ctx.send(embed=embed)

    if verse == 87:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Jeremiah 33:3", value="Call to me and I will answer you, and will tell you great and hidden things that you have not known.")
        await ctx.send(embed=embed)

    if verse == 88:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Timothy 1:7", value="For God gave us a spirit not of fear but of power and love and self-control.")
        await ctx.send(embed=embed)

    if verse == 89:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 John 1:9", value="If we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.")
        await ctx.send(embed=embed)

    if verse == 90:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans 12:16", value="Live in harmony with one another. Do not be haughty, but associate with the lowly. Never be wise in your own sight.")
        await ctx.send(embed=embed)

    if verse == 91:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Hebrews 4:16", value="Let us then with confidence draw near to the throne of grace, that we may receive mercy and find grace to help in time of need.")
        await ctx.send(embed=embed)

    if verse == 92:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans 2:6", value="He will render to each one according to his works.")
        await ctx.send(embed=embed)

    if verse == 93:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Matthew 6:14", value="For if you forgive others their trespasses, your heavenly Father will also forgive you.")
        await ctx.send(embed=embed)

    if verse == 94:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="2 Corinthians 8:12", value="For if the readiness is there, it is acceptable according to what a person has, not according to what he does not have.")
        await ctx.send(embed=embed)

    if verse == 95:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Matthew 11:28", value="Come to me, all who labor and are heavy laden, and I will give you rest.")
        await ctx.send(embed=embed)

    if verse == 96:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Ephesians 6:11", value="Put on the whole armor of God, that you may be able to stand against the schemes of the devil.")
        await ctx.send(embed=embed)

    if verse == 97:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Romans 12:2", value="Do not be conformed to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect.")
        await ctx.send(embed=embed)

    if verse == 98:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="1 John 4:20", value="If anyone says, “I love God,” and hates his brother, he is a liar; for he who does not love his brother whom he has seen cannot love God whom he has not seen.")
        await ctx.send(embed=embed)

    if verse == 99:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Philipians 4:13", value="I can do all things through him who strengthens me.")
        await ctx.send(embed=embed)

    if verse == 100:
        embed = discord.Embed(title="Random Bible Verse", description="Here is your random Bible verse", color=11027200)
        embed.add_field(name="Proverbs 14:29", value="Whoever is slow to anger has great understanding, but he who has a hasty temper exalts folly.")
        await ctx.send(embed=embed)


client.run("ODE0OTA3MzMzNjY2Mjc1Mzg5.YDkrmA.LlNrhAg6JyETUYART6Lz8jXtAb0")
