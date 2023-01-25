from dotenv import load_dotenv
from src import dialogflow
import os

load_dotenv()

DIALOGFLOW_PROJECT_ID = os.environ["DIALOGFLOW_PROJECT_ID"]
DIALOGFLOW_SESSION_ID = os.environ["DIALOGFLOW_SESSION_ID"]
DIALOGFLOW_LANGUAGE_CODE = os.environ["DIALOGFLOW_LANGUAGE_CODE"]

def main():
    texts = "Hello"
    fullfilment_text = dialogflow.detect_intent_texts(DIALOGFLOW_PROJECT_ID, DIALOGFLOW_SESSION_ID, texts, DIALOGFLOW_LANGUAGE_CODE)

    print(dialogflow.parse_query_output(fullfilment_text))

main()