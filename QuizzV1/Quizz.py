# Questions Quiz
# Import OS - Manipulate & Read files
import os
import random

# Global Variables - Stores the amount of points the user earns whilst on the app
points = 0

# Global Files - needed to load the questions, answers and multichoices & to store current highscore
quizzQuestions = "quizzQuestions.txt"
quizzAnswers = "quizzAnswers.txt"
quizzMultichoice = "quizzMultichoice.txt"
quizzHighscore = "quizzHighscore.txt"

# Global Dictionaries - Stores the Questions, Answers and the Multiple Choice answers based on the key index
questionsDictionary = {

}

answersDictionary = {

}

multichoiceDictionary = {

}

highscoresDictionary = {

}

# mainQuiz Function - Main quiz loop where the questions and user answers take place
def mainQuiz():
    global points, questionsDictionary, answersDictionary, multichoiceDictionary

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
    print("\nCongrats on answering the questions!")
    print(f"You have answered {rightAnswers}/{len(answersDictionary)}!")
    
    if wrongAnswers == []: 
        print("You have no wrong answers! Congrats!")
    else: 
        print(f"You have answered wrong at {wrongAnswers}")

    print("Do you wanna return to the menu?")
    print("Y - Goes to the menu\nN - Repeats the Quiz")

    userInput = str(input("Y/N: "))

    if userInput == "Y" or userInput == "y":
        addHighscore()
    if userInput == "N" or userInput == "n":
        mainQuiz()

# menu Function - Displays the Main Menu
def menu():
    global randomTip

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal

        print("=== Computer Technologies Quiz ===")
        print("Welcome to Quizz!")
        print("This project was made to help with your current studies. Please read `readMe.md` to set up the quiz.")
        print("// Made by paycheckbelfast")
        print("\nWhat would you like to choose?")
        print("\n1. Start Quiz")
        print("2. High Scores")
        print("3. Exit")

        userInput = int(input("Type your choice: "))

        while userInput != 0:
            if userInput == 1:
                mainQuiz()
            elif userInput == 2:
                highscores()
            elif userInput == 3:
                exit()
            else:
                print("Choose a valid number between 1-3")
                userInput = int(input("Type your choice: "))

# highscores Function - Display highscores // If there are none, display a message
def highscores():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(highscoresDictionary) == 0:
            print("There are no scores yet!")
            userInput = str(input("Type R/r to return: "))

            if userInput == "R" or userInput == "r":
                menu()
            else:
                print("Please type either R or r to return.")
                userInput = str(input("Type R/r to return: "))
        else:
            print("=== Highscores ===")
            for point in highscoresDictionary:
                name = point
                currentPoints = highscoresDictionary[point]

                print(f"{name} | {currentPoints} PTS")

            userInput = str(input("Type R/r to return: "))

            if userInput == "R" or userInput == "r":
                menu()
            else:
                print("Please type either R or r to return.")
                userInput = str(input("Type R/r to return: "))

# addHighscore Function - Save & update the highscore in highscoresDictionary
def addHighscore():
    global points, highscoresDictionary

    name = str(input("Enter your name: "))
    score = points
    highscoresDictionary[name] = points

    updateHighscore()

# updateHighscore Function - Save & Update the score in quizzHighscore.txt
def updateHighscore():
    global quizzHighscore
    
    with open(quizzHighscore, "w") as highscoreFile:
        for key in highscoresDictionary:
            highscoreFile.write(f"{key} | {highscoresDictionary[key]}\n")
                
    menu()

# quizzLoader Function - Load the .txt files for the quiz to work
def quizzLoader():
    global quizzAnswers, quizzQuestions, quizzMultichoice

    with open(quizzAnswers) as answerFile:
        n = 1
        for answer in answerFile:
            answersDictionary[n] = answer.strip()
            n += 1

    with open(quizzQuestions) as questionFile:
        n = 1
        for question in questionFile:
            questionsDictionary[n] = question.strip()
            n += 1
    
    with open(quizzMultichoice) as multichoiceFile:
        n = 1
        for option in multichoiceFile:
            multichoiceDictionary[n] = option.strip()
            n += 1

# highscoreLoader Function - Load quizzHighscore.txt to load saved progress
def highscoreLoader():
    with open(quizzHighscore) as highscoreFile:
        for highscore in highscoreFile:
            splitLine = highscore.split(" ")
            if len(splitLine) == 3:
                name = splitLine[0]
                point = splitLine[2]
                highscoresDictionary[name] = point.strip()
            else:
                raise Exception("The name should not contain a space.")

# currentDirectory Function - Change "YourDirectory" to the Directory Path
# that this folder is currently in
def currentDirectory():
    os.chdir(r"YourDirectory")

def main():
    # Call the corresponding functions
    currentDirectory()
    highscoreLoader()
    quizzLoader()
    menu()
main()