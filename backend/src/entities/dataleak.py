import subprocess as sub
from emailrep import EmailRep
import random
import re
import json

class DataLeakMECC():

    def __init__(self, emailrep_token, manipulation_answers):
        self.emailrep_token = emailrep_token
        self.manipulation_answers = manipulation_answers

    def post_manipulation_answers(self, manipulation_answers):
        self.manipulation_answers = manipulation_answers

    def get_from_scyllaDB(self):

        output = None
        email = self.manipulation_answers["email"]

        try:
            output = sub.check_output(
                        ["h8mail",
                         "-t",
                         email,
                         "-c",
                         "/app/backend/h8mail_config.ini",
                         "-j",
                         "/app/backend/OUTPUT_JSON.json"])
        except sub.CalledProcessError as e:
            output = e.output
    
        f = open('/app/backend/OUTPUT_JSON.json')
        
        data = json.load(f)

        breach = data["targets"][0]["data"][0]
        count = len(breach)

        if count > 0:
            response = f"Found {count} informations leak according " \
                        "to leaklookup page\nHeres a few random website :\n"
            for index, leak in enumerate(breach):
                if index < 6:
                    breach_site = leak.split("LEAKLOOKUP_PUB:")[1]
                    response += f"{breach_site}\n"
        else:
            response = "No informations seems to have leaked according " \
                       "to leaklookup page.\nCongrats!"
        return response

    def getAnswers(self):
        manipulation_answers = self.manipulation_answers
        quiz_answers = self.manipulation_answers["answer"]

        name = manipulation_answers.get("name")
        age = manipulation_answers.get("age")
        region = manipulation_answers.get("region")
        email = manipulation_answers.get("email")
        sex = manipulation_answers.get("sex")
        change_password = "True"

        if quiz_answers and quiz_answers[7] == "I dont think so":
            change_password = "False"

        scylla_res = self.get_from_scyllaDB()

        res = scylla_res

        res = f" Name: {name} \nAge: {age} \nRegion: {region} \n" \
              f"E-mail: {email} \nDo you change your password " \
              f"often : {change_password}\nBut I also recovered " \
              f"more data about you, such as :\nGender: {sex}\n" + res
        return res
