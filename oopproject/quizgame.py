import random

questions = [
   {
       "question": "what is the output of 2 +3",
       "options" : ["4", "2" , "5","7"],
       "answer"  :"C",
       "difficulty":"easy"
   },

   {
       "question" : "what is my name?",
       "options" : ["utsav" , "poudel", "someone"],
       "answer": "A",
       "difficulty":"medium"
   }
]

# def get_answer(message):
#      while True:
#          try:
#             return int(input("Enter your option"))
#          except ValueError:
#                 print("Please Enter a valid Option")


def choose_difficultylevel():
        while True:
               print("\n=== DIFFICULTY ===")
               print("1.Easy")
               print("2.Medium")
               print("3.Hard")

               choice = input("Choose Difficulty: ")
               if choice =="1":
                  return "easy"
     
               elif choice == "2":
                   return "medium"
    
               elif choice == "3":
                   return "hard"  
     
               else:
                   print("Invalid choice!")   
      


def start_game():
    score = 0

    difficulty = choose_difficultylevel()

    random.shuffle(questions)

    for question in questions:
      
         if question["difficulty"] != difficulty:
           continue    
         print("\n" + question["question"])

         for i, option in enumerate(question["options"]):
                 print(f"{chr(65 + i)}.{option}")

        
         answer = input("Choose your Option").upper()

         if answer == question["answer"]:
            print("correct")
            score += 1
         else:
              print("😑 Wrong")
              print(f"correct answer is {question["answer"]}")

    print(f"\nYour final score : {score}/{len(questions)}")

while True:
     print("\n ==== Python Quiz")
     print("1.Start Game")
     print("2.Instructions")
     print("3.Exit")

     choice = input("Enter Choice: ")

     if choice == "1":
         
         start_game()

     elif choice == "2":
          print("\n Answe your question by entering A,B,C & D")

     elif choice == "3":
          print("GoodByee✌🏼")
          break
     else:
          print("Invalid Choice")
