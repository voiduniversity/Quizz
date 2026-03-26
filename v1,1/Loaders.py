# quizzLoader Function - Load the .txt files for the quiz to work
def quizzLoader(quizzAnswers, quizzQuestions, quizzMultichoice, answersDictionary, questionsDictionary, multichoiceDictionary):

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
def highscoreLoader(quizzHighscore, highscoresDictionary):
    with open(quizzHighscore) as highscoreFile:
        for highscore in highscoreFile:
            splitLine = highscore.split(" ")
            if len(splitLine) == 3:
                name = splitLine[0]
                point = splitLine[2]
                highscoresDictionary[name] = point.strip()
            else:
                raise Exception("The name should not contain a space.")