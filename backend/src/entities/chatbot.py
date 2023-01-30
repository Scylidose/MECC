from marshmallow import Schema, fields

class Chatbot():

    def __init__(self, dialogflow_client):
        self.dialogflow_client = dialogflow_client
        self.response = ""
        self.message = ""

    def get_message(self):
        return self.message
    
    def post_message(self, message):
        self.message = message
    
    def get_response(self):
        return self.response
    
    def post_response(self, response):
        self.response = response

    def detect_intent(self, text):
        fullfilment_text = self.dialogflow_client.detect_intent_texts(text)

        return fullfilment_text

    def send_message(self, fullfilment_text):
        response = self.dialogflow_client.parse_query_output(fullfilment_text)

        return response
    

class ChatbotSchema(Schema):
    message = fields.Str()
    response = fields.Str()
