from marshmallow import Schema, fields

class Chatbot():

    def __init__(self, dialogflow_client, quiz_object):
        self.dialogflow_client = dialogflow_client
        self.quiz_object = quiz_object
        self.messages = []

    def get_quiz_object(self):
        return self.quiz_object

    def post_quiz_object(self, quiz_object):
        self.quiz_object = quiz_object

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
        text = text[0]
        if text == "Yes, teach me !":
            answers = self.dialogflow_client.get_answers()
            if len(answers) > 15:
                del answers[1::2]
            self.quiz_object.saveAnswers(answers)
            text = self.quiz_object.analyze_answer()

        fullfilment_text = self.dialogflow_client.detect_intent_texts(text)

        return fullfilment_text

    def send_response(self, text):
        fullfilment_text = self.detect_intent(text)
        response = self.dialogflow_client.parse_query_output(fullfilment_text)

        return response
    

class ChatbotSchema(Schema):
    messages = fields.List(fields.Str())
