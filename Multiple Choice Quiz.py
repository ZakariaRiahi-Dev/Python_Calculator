class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts =  [
    "What is the capital of Australia?\n A. Sydney\n B. Melbourne\n C. Canberra\n D. Brisbane\n",
    "What planet is known as the Red Planet?\n A. Venus\n B. Mars\n C. Jupiter\n D. Saturn\n",
    "Who was the first President of the United States?\n A. George Washington\n B. Abraham Lincoln\n C. Thomas Jefferson\n D. John Adams\n",
    "Which country has won the most FIFA World Cups?\n A. Brazil\n B. Germany\n C. Italy\n D. Argentina\n"
]

question = [
    Question(question_prompts[0], "C"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "A"),
    Question(question_prompts[3], "A")
]


def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(question_prompts)) + " correct")

run_test(question)
    