import subprocess as sub
from emailrep import EmailRep
import random
import re

class DataLeakMECC():

    def __init__(self, email, emailrep_token, manipulation_answers):
        self.email = email
        self.emailrep_token = emailrep_token
        self.manipulation_answers = manipulation_answers

    def post_manipulation_answers(self, manipulation_answers):
        self.manipulation_answers = manipulation_answers

    def get_from_scyllaDB(self):

        output = None

        try:
            print("EMAIL : ", self.email)
            output = sub.check_output(["h8mail", "-t",self.email,"-c", "/app/backend/h8mail_config.ini"])
        except sub.CalledProcessError as e:
            print("ERROR")
            output = e.output
        print("OUTPUT ", output)
        output = output.decode("utf8",).split("\n")

        count = 0
        start_count = 0
        end_count = 0
        breach = []
        
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

        for line in output:
            splitted_line = line.split(">")[-1]

            if 'Showing results for' in splitted_line:
                start_count = count + 1
            if '_____' in splitted_line:
                if start_count > end_count:
                    end_count = count-1
            count += 1

        for i in range(start_count, end_count):
            breach.append(ansi_escape.sub('', output[i].split(">")[-1]))

        if len(breach) > 0:
            response = f"Found {len(breach)} informations leak according to leaklookup page\nHeres a few random website :\n"
            for index, leak in enumerate(breach):
                if index < 6:
                    response += f"{leak}\n"
        else:
            response = "No informations seems to have leaked according to leaklookup page.\nCongrats!"
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

        if quiz_answers and quiz_answers[7] == "Of course not !":
            change_password = "False"

        scylla_res = self.get_from_scyllaDB()

        res = scylla_res
        
        res = f" Name: {name} \nAge: {age} \nRegion: {region} \nE-mail: {email} \nDo you change your password often : {change_password}\n\nBut I also recovered more data about you, such as :\nGender: {sex}\n" + res

        return res
