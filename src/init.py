from http import client
import discord
import logging
import os

class CreateAddonHubBot(discord.Client):

    async def on_ready(self):
        logging.info(f'Logged in as {client.user}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    try:
        client = CreateAddonHubBot(intents=intents)
        client.run(os.environ.get('TOKEN'))
    except EnvironmentError as e:
        logging.error("Failed to read token")
        logging.error(e)
    finally:
        logging.info(discord.__version__)
        logging.info(discord.version_info)

