from question import Question
from quiz_brain import QuizBrain
from data import question_data
import random

current_round = 0
correct_answers = 0
rounds = int(input("How many rounds do you want to play?"))
quiz_brain = QuizBrain([], 1)

for i in range(rounds):
    
    current_round += 1

    random.shuffle(question_data)

    question = Question(question_data[0]['question'], question_data[0]['correct_answer'])

    #print(f'Round: {current_round}')

    quiz_brain.next_question(question.question, question.answer)

    

    print(f"\nCorrect Answers: {quiz_brain.score}/{current_round}\n")
    
    question_data.pop(0)


print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{current_round}\n")


