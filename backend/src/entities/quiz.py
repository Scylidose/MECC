import json

f = open('/app/backend/config/answers.json')


class QuizMECC:

    def __init__(self):
        self.score = []
        self.answers = []
        self.global_score = 0
        self.data = json.load(f)

    def saveQuizAnswer(self, msg):
        if not self.answers:
            self.answers = []
        self.answers.append(msg)

    def getAnswers(self):
        return self.answers

    def saveAnswers(self, answers):
        self.answers = answers

    def initializeQuiz(self):
        self.answers = []

    def get_results(self):

        true_answer = self.data['true_answer']
        topic_list = self.data['topic_list']

        self.score = {
            "password": 3,
            "data_save": 3,
            "phishing": 3,
            "ransomware": 3,
            "social": 3,
            "global_score": 0
        }

        results = {
            "score": {},
            "topic_list": [],
            "quiz_result": [],
            "true_answer": []
        }
        quiz_result = []

        quiz_answers = self.answers

        if not quiz_answers:
            quiz_answers = []

        for i, answer in enumerate(quiz_answers):
            if i < 15:
                if true_answer[i] != answer:
                    quiz_result.append("False")
                    self.score[topic_list[i]] -= 1
                else:
                    quiz_result.append("True")

        results["score"] = self.score
        results["quiz_result"] = quiz_result
        results["topic_list"] = topic_list
        results["user_answer"] = quiz_answers
        results["true_answer"] = true_answer

        return results

    def calculate_score(self):

        true_answer = self.data['true_answer']
        topic_list = self.data['topic_list']

        self.score = {
            "password": 3,
            "data_save": 3,
            "phishing": 3,
            "ransomware": 3,
            "social": 3,
            "global_score": 0
        }

        quiz_answers = self.answers

        if not quiz_answers:
            quiz_answers = []

        for i, answer in enumerate(quiz_answers):
            if i < 15:
                if true_answer[i] != answer:
                    self.score[topic_list[i]] -= 1
                else:
                    self.global_score += 1

        if len(quiz_answers) > 0:

            self.global_score /= len(quiz_answers)

            self.score["global_score"] = self.global_score

    def analyze_answer(self):
        self.calculate_score()

        topic_list = self.data['topic_intent']

        intent_phrase = ""

        self.scores = list(self.score.values())[:-1]
        min_index = [i for i, x in enumerate(
            self.scores) if x == min(self.scores) and x != 3]

        if len(min_index) == len(topic_list) or len(min_index) == 0:
            intent_phrase = "mecc.train.all1"
        else:
            intent_phrase = topic_list[min_index[0]]

        return intent_phrase
