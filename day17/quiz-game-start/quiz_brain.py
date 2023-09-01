class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.quest_list = q_list

def next_question(self):
    current_question = self.quest_list[self.q_number]
    
    input(f"Q.{self.q_number} : {current_question.text} T/F")

