"""This module receives json files and makes it possible to receive information from them."""
import json


class QuestionHeap:
    def __init__(self):
        with open("questions.json", 'r', encoding="utf-8") as file:
            self.dictionary = json.load(file)
        self.score = 0
        self.player_answer = ""

    def get_title(self):
        return self.dictionary["title"]

    def get_hello_message(self):
        return self.dictionary["hello_message"]

    def get_question_amount(self):
        return self.dictionary["question_amount"]

    def get_type(self, number):
        return self.dictionary["questions"][number]["question_type"]

    def get_question(self, number):
        return self.dictionary["questions"][number]["question"]

    def get_answer(self, number):
        return self.dictionary["questions"][number]["right_answer"]

    def get_options(self, number):
        return self.dictionary["questions"][number]["question_options"]
