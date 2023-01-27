from dotenv import load_dotenv
from src import dialogflow_mecc
from src.discord import discord_mecc

import os

load_dotenv()

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

DIALOGFLOW_PROJECT_ID = os.environ["DIALOGFLOW_PROJECT_ID"]
DIALOGFLOW_SESSION_ID = os.environ["DIALOGFLOW_SESSION_ID"]
DIALOGFLOW_LANGUAGE_CODE = os.environ["DIALOGFLOW_LANGUAGE_CODE"]

def main():

    texts = "Hello"
    dialogflow_client = dialogflow_mecc.DialogflowMECC(DIALOGFLOW_PROJECT_ID, DIALOGFLOW_SESSION_ID, DIALOGFLOW_LANGUAGE_CODE)
    
    discord_client = discord_mecc.DiscordMECC(dialogflow_client, DISCORD_BOT_TOKEN)
    discord_client.run_discord_bot()

    fullfilment_text = dialogflow_client.detect_intent_texts(texts)

    response = dialogflow_client.parse_query_output(fullfilment_text)
    print(response)

main()