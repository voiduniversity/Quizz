def questionMenu(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary):
    while True:
        print("==== Question Maker ====")
        print("1. Add a new Question, Answer and Multichoice Picks")
        print("2. Remove a Question, Answer and Multichoice Picks")
        print("3. Remove all Questions, Answers, and Multichoice Picks")
        print("4. Return to the menu")

        userInput = int(input("Enter your choice: "))
        if userInput != 0:
            if userInput == 1:
                makeQuestiion(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary)
                break
            if userInput == 2:
                removeQuestion(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary)
                break
            if userInput == 3:
                removeAll(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary)
                break
            if userInput == 4:
                break


def makeQuestiion(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary):
    num = int(input("How many questions would you like to add? "))
    lastNum = list(answersDictionary)[-1]

    for i in range(num):
        lastNum += 1
        question = str(input("Enter the question you want to add: "))

        multichoice1 = str(input("Enter your first multichoice answer: "))
        multichoice2 = str(input("Enter your second multichoice answer: "))
        multichoice3 = str(input("Enter your third multichoice answer: "))
        multichoice4 = str(input("Enter your fourth multichoice answer: "))

        answer = str(input("Enter the answer: "))

        questionsDictionary[lastNum] = question

        answersDictionary[lastNum] = answer.upper()

        multichoiceDictionary[lastNum] = f"A. {multichoice1},B. {multichoice2},C. {multichoice3},D. {multichoice4}"

    with open(quizzQuestions, "w") as questionFile:
        for key in questionsDictionary:
            questionFile.write(f"{questionsDictionary[key]}\n")

    with open(quizzAnswers, "w") as answersFile:
        for key in answersDictionary:
            answersFile.write(f"{answersDictionary[key]}\n")
    
    with open(quizzMultichoice, "w") as multichoiceFile:
        for key in multichoiceDictionary:
            multichoiceFile.write(f"{multichoiceDictionary[key]}\n")
    
def removeQuestion(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary):
    key = int(input("Enter the question number you want to delete: "))
    inDictionary = False
    
    for keys in questionsDictionary:
        inDictionary = False
        if key == keys:
            inDictionary = True
    
    if inDictionary == True:
        del questionsDictionary[key]
        del answersDictionary[key]
        del multichoiceDictionary[key]

    with open(quizzQuestions, "w") as questionFile:
        for key in questionsDictionary:
            questionFile.write(f"{questionsDictionary[key]}\n")

    with open(quizzAnswers, "w") as answersFile:
        for key in answersDictionary:
            answersFile.write(f"{answersDictionary[key]}\n")
    
    with open(quizzMultichoice, "w") as multichoiceFile:
        for key in multichoiceDictionary:
            multichoiceFile.write(f"{multichoiceDictionary[key]}\n")

def removeAll(quizzAnswers, quizzMultichoice, quizzQuestions, questionsDictionary, answersDictionary, multichoiceDictionary):
    userInput = str(input("Are you sure? Y/N: "))
    if userInput == "Y" or userInput == "y":
        questionsDictionary.clear()
        answersDictionary.clear()
        multichoiceDictionary.clear()

        with open(quizzQuestions, "w") as questionFile:
            for key in questionsDictionary:
                questionFile.write()

        with open(quizzAnswers, "w") as answersFile:
            for key in answersDictionary:
                answersFile.write()
        
        with open(quizzMultichoice, "w") as multichoiceFile:
            for key in multichoiceDictionary:
                multichoiceFile.write()
    elif userInput == "N" or userInput == "n":
        return
    else:
        raise Exception("Invalid Character Input.")