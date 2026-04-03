# Questions Quiz
# Import OS - Manipulate & Read files
import os
import random
from ownQuestions import *
from loaders import *
from quizzFile import *

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

# menu Function - Displays the Main Menu
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal

        print("=== Computer Technologies Quiz ===")
        print("Welcome to Quizz!")
        print("This project was made to help with your current studies. Please read `readMe.md` to set up the quiz.")
        print("// Made by paycheckbelfast")
        print("\nWhat would you like to choose?")
        print("\n1. Start Quiz")
        print("2. High Scores")
        print("3. Make your own Quiz")
        print("4. Exit")

        userInput = int(input("Type your choice: "))
        
        if userInput == 1:
            mainQuiz(questionsDictionary, answersDictionary, multichoiceDictionary, highscoresDictionary, quizzHighscore)
        elif userInput == 2:
            highscores()
        elif userInput == 3:
            questionMenu(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary)
        elif userInput == 4:
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

# currentDirectory Function // Connect modules inside the folder path
def currentDirectory():
    try:
        os.chdir(r"YourDicrectory") # Change to your directory
    except Exception as e:
        print("Please enter your file directory in this function: currentDirectory()")
        exit()

def main():
    # Call the corresponding functions
    currentDirectory()
    highscoreLoader(quizzHighscore, highscoresDictionary)
    quizzLoader(quizzAnswers, quizzQuestions, quizzMultichoice, answersDictionary, questionsDictionary, multichoiceDictionary)
    menu()
main()