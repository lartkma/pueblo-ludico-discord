import argparse
import discord

argument_parser = argparse.ArgumentParser(description="Inicia el bot de Pueblo Ludico")
argument_parser.add_argument('--tokenfile', help="El token indentificador de bot (privado). Argumento requerido", required=True)

args = argument_parser.parse_args()
discord_token = None

with open(args.tokenfile, "r") as token_file:
    discord_token = token_file.readline().strip()

class PuebloLudicoBotClient(discord.Client):

    # Events

    async def on_ready(self):
        print("The bot is ready!")

    async def on_member_join(self, member):
        general_channel = discord.utils.get(member.guild.channels, name="general")
        with open("./resources/welcome.md", "r", encoding="utf-8") as text_file:
            welcome_message = ''.join(text_file.readlines())
            welcome_message = welcome_message.format(link_usuario=member.mention)
            await general_channel.send(welcome_message)

    # async def on_message(self, message):
    #    if message.author == self.user:
    #         return

# NO DEBE POSTEARSE EL TOKEN NUNCA
PuebloLudicoBotClient().run(discord_token)
