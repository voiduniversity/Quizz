import os

points = 0

# mainQuiz Function - Main quiz loop where the questions and user answers take place
def mainQuiz(questionsDictionary, answersDictionary, multichoiceDictionary, highscoresDictionary, quizzHighscore):
    global points
    if len(questionsDictionary) == 0:
        raise Exception("There are no questions. Add some questions!")
    
    points = 0 

    rightAnswers = 0
    wrongAnswers = []

    for key in questionsDictionary: 
        while key <= len(answersDictionary): 
            os.system('cls' if os.name == 'nt' else 'clear') 
            print(str(key) + ". " + questionsDictionary[key] + "\n") 

            choices = multichoiceDictionary[key] 
            choices = choices.split(",") 
            answer = answersDictionary[key] 

            for i in range(0, len(choices)): 
                print(choices[i]) 
            
            print(f"\nPOINTS: {points}") 
            userInput = input("What is your answer? ") 

            if userInput == answer or userInput == answer.lower(): 
                print("Correct!")
                points += 1 
                rightAnswers += 1 
                break
            else:
                print(f"Wrong! The right answer was: {answer}")
                wrongAnswers.append(f"Q.{key}") 
                break
    
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
    print(f"Summary: {rightAnswers}/{len(answersDictionary)}!")
    
    if wrongAnswers == []: 
        print("You have no wrong answers! Congrats!")
    else: 
        print(f"You have answered wrong at {wrongAnswers}")

    print("\nDo you wanna return to the menu?")
    print("Y - Goes to the menu\nN - Repeats the Quiz")

    userInput = str(input("Y/N: "))

    if userInput == "Y" or userInput == "y":
        addHighscore(quizzHighscore, highscoresDictionary)
    if userInput == "N" or userInput == "n":
        mainQuiz()

# addHighscore Function - Save & update the highscore in highscoresDictionary
def addHighscore(quizzHighscore, highscoresDictionary):
    name = str(input("Enter your name: "))
    score = points
    highscoresDictionary[name] = points

    updateHighscore(quizzHighscore, highscoresDictionary)

# updateHighscore Function - Save & Update the score in quizzHighscore.txt
def updateHighscore(quizzHighscore, highscoresDictionary):
    with open(quizzHighscore, "w") as highscoreFile:
        for key in highscoresDictionary:
            highscoreFile.write(f"{key} | {highscoresDictionary[key]}\n")