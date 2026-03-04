


# def run_quiz(questions):
#   score = 0
#   for q in questions:
#     answer = input(q +'')
#     if answer == questions[q]:
#       score += 1
#     print(f"you got {score} out of {len(questions)}correct") 

# quiz = {
#         "What is the capital of France?": "Paris",
#         "What is 2 + 2?": "4",
#         "What color is the sky?": "Blue"}

# run_quiz(quiz)                   







# math_facts = {
#     "5+3": 8,
#     "3*4": 12,
#     "20-5": 15
# }
# for questions, answers in math_facts.items():
#     x= questions
#     y= answers
#     my_question = int(input(f"{x} is equal to :"))
#     if my_question == y:
#         print("well done")
#     else:
#         print("try again")    


# math_facts = {
#     "5+3": 8,
#     "3*4": 12,
#     "20-5": 15
# }

# for problem in math_facts:
#     user_answer = int(input("problem"+ ""))
#     if user_answer == math_facts[problem]:
#         print("correct")
#     else:
#         print("false")        

# math_facts = {
#     "5+3": 8,
#     "3*4": 12,
#     "20-5": 15
# }

# for question, answer in math_facts.items():
#     try:
#         user_answer = int(input(f"What is {question}? "))
#         if user_answer == answer:
#             print("✅ Well done!")
#         else:
#             print(f"❌ Try again! The correct answer is {answer}.")
#     except ValueError:
#         print("⚠️ Please enter a number.")



# def trivia_round(questions):
#     player_name = input("give me a name")
#     score = 0
#     for q in questions:
#     answer = input(q + "")
#     if answer == questions[q]:
#         print(f"well done {player_name}")
#     else:
#         print("try again")    
    
# quiz = {
#         "What is the capital city of Australia?": "Canberra",
#         "Who wrote the novel '1984'?": "George Orwell",
#     "What is the chemical symbol for gold?": "Au"
# }
# score = 0
# player_name = input("give me user name")
# for question, answer in quiz.items():
#     user_answer = input(f"answer me the following question \n{question}")  

#     if user_answer.strip().lower() == answer.lower():
#         print(f"well done {player_name}")
#         score += 1
#     else:
#         print("try again") 

# def trivia_round(questions):
#     score = 0
# quiz = {
#         "What is the capital city of Australia?": "Canberra",
#         "Who wrote the novel '1984'?": "George Orwell",
#     "What is the chemical symbol for gold?": "Au"
# }
  

# quiz = {
#          "What is the capital city of Australia?": "Canberra",
#          "Who wrote the novel '1984'?": "George Orwell",
#      "What is the chemical symbol for gold?": "Au"
#  }


# def trivia_round():    
#     player_name = input("player name") 
#     score = 0
    
#     for question, answer in quiz.items(): 
#         player_answer = input(f"anser me this : {question}")     
   
       
        
#         if player_answer.strip().lower() == answer.lower():
#             print(f"well done {player_name}")
#             score += 1
#         else:
#             print("try again")
    
#     print(f"{player_name} your final score is {score}/{len(quiz)}")

# trivia_round()

# import threading

# quiz = {
#          "What is the capital city of Australia?": "Canberra",
#          "Who wrote the novel '1984'?": "George Orwell",
#      "What is the chemical symbol for gold?": "Au"
#  }

# def input_with_timeout(promt,timeout):
#     answer = [None]

#     def get_input():
#         answer[0] = input(promt)

#     thread = threading.Thread(target=get_input)
#     thread.start()
#     thread.join(timeout)    

#     if thread.is_alive():
#         print("time's up!")
#     else:
#         return answer[0]

# def speed_quiz():
#     player_name = input("give my your name")
#     score = 0

#     for question, answer in quiz.items():
#         player_answer = input_with_timeout(f"answer me : {question}. You have 10 seconds" ,10)

#         if player_answer is None:
#             print("too slow.") 
        
#         elif player_answer.strip().lower() == answer.lower():
#             print(f"well done {player_name}")
#             score +=1

#         else:
#             print("try again")

#     print(f"{player_name}, your final score is {score}/{len(quiz)}")

# speed_quiz()        


# fancy_words = {
#     "eloquent": "able to express ideas clearly and beautifully in speech or writing",
#     "ephemeral": "lasting for a very short time",
#     "serendipity": "finding something good without looking for it",
#     "ineffable": "too great or extreme to be described in words"}
# score = 0
# player = input("give your name")

# for words, meaning in fancy_words.items():
    
#     answer = input(f"do you know what {words} mean ,{player}? ")
#     if meaning == answer:
#         print(f"well done {player}")
#         score += 1
#     else:
#         print(f"try again")

# print(f"{player}, your final score is {score} / {len(fancy_words)}")             

# def all_caps_quiz():
#     dictionary = {"What is the capital of France?": "Paris",
#     "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
#     "What is the largest planet in our solar system?": "Jupiter"}
    
    
#     player_name = input("player name").strip()
#     p = player_name.upper()
    
#     for q, answer in dictionary.items():
#         a = q.upper()
        
#         player_answer = input(f"Can you tell me {a}, {p}" ).strip()

#         if player_answer.lower() == answer.lower():
#             print(f"well gone {p}")

#         else:
#             print("try again")    



# all_caps_quiz()


# def all_caps_quiz(qset):
#     score = 0
#     for q in qset:
#        answer = input(q + "")
#        if answer.upper() == qset[q].upper():
#            score+= 1
#     print("Score :",score)       


# questions = {"What is the capital of France?": "Paris",
#     "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
#     "What is the largest planet in our solar system?": "Jupiter"}    

# all_caps_quiz(questions)


# questions = {"What is the capital of France?": "Paris",
#     "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
#     "What is the largest planet in our solar system?": "Jupiter"}   




# def all_caps_quiz(qset):
#     score = 0
#     total = len(qset)
   
#     for q, correct_answer in qset.items():
#         answer = input(q + "").strip()
#         if answer.upper() == correct_answer.upper():
#             print("correct")
#             score += 1
#         else:
#             print("try again")    

#     print(f"\n final score is {score}/ {total}")


# all_caps_quiz(questions)
     
# common_errors = {
#     "NameError": "Occurs when you try to use a variable or function name that hasn’t been defined.",
#     "TypeError": "Happens when an operation or function is applied to an object of the wrong type.",
#     "ValueError": "Raised when a function gets a valid type but an inappropriate value (e.g., int('abc'))."}
# score = 0
# player = input("name")

# for error, definition in common_errors.items():
#     answer = input(error + "").strip()
#     if answer == definition:
#         print(f"well done {player}")
#         score += 1
#     else:
#         print(f"nope, the answer is {definition}")

#     print(f"so far your score is {score}/ {len(common_errors)}")


# common_errors = {
#     "NameError": "Occurs when you try to use a variable or function name that hasn’t been defined.",
#     "TypeError": "Happens when an operation or function is applied to an object of the wrong type.",
#     "ValueError": "Raised when a function gets a valid type but an inappropriate value (e.g., int('abc'))."}
# score =0
# total = len(common_errors)
# for e, meaning in common_errors.items():
#     quess = input(e + "").strip()
#     if quess.lower() == meaning.lower():
#         print(f"well done, so far your score is {score}/{total}")
#         score += 1
#     else:
#         print("try again")    

# print(f"Final score : {score}/ {total}")    

# quiz = {":-)": "smile", ":D":"happy", ":-(":"sad"}
# score = 0
# total = len(quiz)

# for emoji, meaning in quiz.items():
#     guess = input(emoji + "").strip()
#     if guess.lower() == meaning.lower():
#         print(f"well done, your score is {score}/ {total}")
#         score +=10
#     else:
#         print(f"try again, your score is {score}/ {total}")
#         score -=5
# print(f"your final score is {score} / {total}")

# quiz = {":-)": "smile", ":D":"happy", ":-(":"sad"}
# score = 0

# for q in quiz:
#     guess = input(q + "")
#     if guess == quiz[q]:
#         print ("well done")
#         score += 1
#     else:
#         print("try again")

#     print(f"you score is {score}")    



# def custom_flashcards():
#     custom = {}
#     for i in range(3):
#         question = input("enter a question")
#         answer = input("enter the answer")
#         custom[question] = answer

#     for q in custom:
#         user = input(q + "")
#         if user == custom[q]:
#             print("correct")
#         else:
#             print("incorrect")
# custom_flashcards()                    