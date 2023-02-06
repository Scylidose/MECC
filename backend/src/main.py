from dotenv import load_dotenv

from entities.dialogflow import DialogflowMECC
from entities.quiz import QuizMECC
from entities.dataleak import DataLeakMECC
from entities.chatbot import Chatbot, ChatbotSchema

from flask_cors import CORS
from flask import Flask, jsonify, request

import os

load_dotenv()

DIALOGFLOW_PROJECT_ID = os.environ["DIALOGFLOW_PROJECT_ID"]
DIALOGFLOW_SESSION_ID = os.environ["DIALOGFLOW_SESSION_ID"]
DIALOGFLOW_LANGUAGE_CODE = os.environ["DIALOGFLOW_LANGUAGE_CODE"]

EMAILREP_TOKEN = os.getenv('EMAILREP_TOKEN')

app = Flask(__name__)
CORS(app)

dataleak_object = DataLeakMECC(EMAILREP_TOKEN, [])
quiz_object = QuizMECC()
dialogflow_client = DialogflowMECC(DIALOGFLOW_PROJECT_ID, DIALOGFLOW_SESSION_ID, DIALOGFLOW_LANGUAGE_CODE, dataleak_object)
chatbot_object = Chatbot(dialogflow_client, quiz_object)

@app.route('/')
def main():
    with app.app_context():
        
        schema = ChatbotSchema()
        chatbot = schema.dump(chatbot_object)

        return jsonify(chatbot)

@app.route('/message', methods=['POST'])
def add_message():
    message = [request.get_json()['messages'][0]['text']]

    chatbot_object.post_message(message)
    response = chatbot_object.send_response(message)
    chatbot_object.clear_message()

    chatbot_object.post_message(response)

    new_chatbot = ChatbotSchema().dump(chatbot_object)

    return jsonify(new_chatbot), 201
