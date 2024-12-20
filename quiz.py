# Python Quiz Game

questions = ("What is Martian's real name?: ",
             "What is Martian's dog's name?: ",
             "What is Martian's Boyfriend's name?: ",
             "What is Martian's Cat's name?: ")

options = (("A. David", "B. Benjimin", "C. Uylisys", "D. DeMarvis"), 
           ("A. Oliver", "B. Oscar", "C. Andrew", "D. Fido"), 
           ("A. Steven", "B. Armando", "C. Richard", "D. Roberto"), 
           ("A. Mrs. Kittyfuck", "B. Chelsea", "C. Ms. Purrdy", "D. Rachel"))

answers = ("D", "A", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions: 
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else: print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------------")
print("            RESULTS             ")
print("--------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is:{score}%")
