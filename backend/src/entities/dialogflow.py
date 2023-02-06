from google.cloud import dialogflow
import gender_guesser.detector as gender


class DialogflowMECC:

    def __init__(self, project_id, session_id, language_code, dataleak_object):
        self.project_id = project_id
        self.session_id = session_id
        self.language_code = language_code
        self.dataleak_object = dataleak_object
        self.answers = {"answer":[]}

    def get_answers(self):
        return self.answers["answer"]

    def detect_intent_texts(self, text):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversation."""
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)
        if text:
            text_input = dialogflow.TextInput(text=text, language_code=self.language_code)

            query_input = dialogflow.QueryInput(text=text_input)

            response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )

            intent = response.query_result.intent.display_name

            if "quiz" in intent:
                if "start" in intent:
                    self.answers["region"] =  text
                if text != "Start the quiz":
                    self.answers["answer"].append(text)

                elements = response.query_result.fulfillment_messages
                res = []
                for element in elements:
                    df_res = self.create_df_response(element, "quiz")
                    res.append(df_res)
                return res

            if "train" in intent:
                if "start" in intent:
                    self.answers["answer"].append(text)

                elements = response.query_result.fulfillment_messages
                res = []
                for element in elements:
                    df_res = self.create_df_response(element, "train")
                    res.append(df_res)
                return res

            if "manipulation" in intent:
                if "q2" in intent:
                    gend = gender.Detector()
                    sex = gend.get_gender(name=text)
                    self.answers["sex"] =  sex
                    self.answers["name"] =  text
                if "q3" in intent:
                    self.answers["age"] =  text

                elements = response.query_result.fulfillment_messages
                res = []
                for element in elements:
                    df_res = self.create_df_response(element, "manipulation")
                    res.append(df_res)

                if "finish" in intent:
                    self.answers["email"] =  text
                    manipulation_results = self.answers
                    print("MANIPULATION : ", manipulation_results)
                    self.dataleak_object.post_manipulation_answers(manipulation_results)
                    quiz_results = manipulation_results["answer"]

                    print("QUIZ RESULTS ", quiz_results)

                    credentials = self.dataleak_object.getAnswers()

                    print("CREDENTIALS ", credentials)

                    df_res = self.create_df_response(
                        credentials, "text")
                    res.append(df_res)

                return res

            df_response = self.create_df_response(
                response.query_result.fulfillment_text, "text")

            return df_response

    def parse_query_output(self, messages):
        responses = []
        if isinstance(messages, dict):
            responses.append(messages)
        else:
            for message in messages:
                responses.append(message)
        return responses

    def create_df_response(self, element, res_type):

        df_response = {}

        if res_type == "text":
            df_response["df_type"] = "text"
            df_response["text"] = element

        if res_type == "quiz" or res_type == "train":

            if element.text.text:
                df_response["df_type"] = "text"
                df_response["text"] = element.text.text[0]

            if element.quick_replies.title:
                df_response["df_type"] = "quick_replies"
                df_response["text"] = element.quick_replies.title
                df_response["quick_replies"] = element.quick_replies.quick_replies

        if res_type == "manipulation":
            if element.text.text:
                df_response["df_type"] = "text"
                df_response["text"] = element.text.text[0]

        return df_response
