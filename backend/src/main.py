from dotenv import load_dotenv

from .entities.dialogflow import DialogflowMECC
from .entities.chatbot import Chatbot, ChatbotSchema

from flask_cors import CORS
from flask import Flask, jsonify, request

import os

load_dotenv()

DIALOGFLOW_PROJECT_ID = os.environ["DIALOGFLOW_PROJECT_ID"]
DIALOGFLOW_SESSION_ID = os.environ["DIALOGFLOW_SESSION_ID"]
DIALOGFLOW_LANGUAGE_CODE = os.environ["DIALOGFLOW_LANGUAGE_CODE"]

app = Flask(__name__)
CORS(app)

dialogflow_client = DialogflowMECC(DIALOGFLOW_PROJECT_ID, DIALOGFLOW_SESSION_ID, DIALOGFLOW_LANGUAGE_CODE)
chatbot_object = Chatbot(dialogflow_client)

@app.route('/')
def main():
    with app.app_context():
        
        schema = ChatbotSchema()
        chatbot = schema.dump(chatbot_object)

        return jsonify(chatbot)

@app.route('/message', methods=['POST'])
def add_message():
    message = request.get_json()['messages']

    chatbot_object.post_message(message)

    chatbot_object.post_message(chatbot_object.send_response(message))
    new_chatbot = ChatbotSchema().dump(chatbot_object)

    return jsonify(new_chatbot), 201

main()