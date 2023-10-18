class QuizBrain:
    def __init__(self, question_list, question_number):
        self.question_list = question_list
        self.question_number = question_number
        self.score = 0

    def next_question(self, question, answer):
        user_answer = input(question + ' True or False? ')
        self.check_answer(answer, user_answer)


    def check_answer(self, answer, user_answer):
        
        if (user_answer.lower() == answer.lower()):
            print('Correct!')
            self.score += 1
        else:
            print('Incorrect!')


