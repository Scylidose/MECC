from marshmallow import Schema, fields

class Chatbot():

    def __init__(self, dialogflow_client):
        self.dialogflow_client = dialogflow_client
        self.messages = []

    def get_messages(self):
        return self.messages

    def clear_message(self):
        self.messages = []

    def post_message(self, message):
        if isinstance(message, dict):
            self.messages = self.messages + [message]
        else:
            self.messages = self.messages + message

    def detect_intent(self, text):
        fullfilment_text = self.dialogflow_client.detect_intent_texts(text)

        return fullfilment_text

    def send_response(self, text):
        fullfilment_text = self.detect_intent(text)
        response = self.dialogflow_client.parse_query_output(fullfilment_text)

        return response
    

class ChatbotSchema(Schema):
    messages = fields.List(fields.Str())
