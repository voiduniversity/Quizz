# 📄 Quizz
Quizz is a Python Project in which you test yourself and your skills
in answering questions. It is a multiple answer Quiz at the moment.

## 💻 Functionality
- Quiz itself can be as long as you want it to be
- Highscore function so you can go against your friends (Has to be on the same device)
- Fully customisable

## ‼️ Important Information
You may be asked to "Trust this Publisher". Press it to allow the project to save and update your progress and to also read your questions inside the .txt files.

For this project to work, you have to follow a simple format for each text file.
Within each file, there will be an example so you can take a look at for yourself to see how it works. When you want to add your own stuff, delete everything in each file and follow the formats below:
- quizzQuestions.txt - Write it as you normally would. Each question has to be in it's own line
- quizzMultichoice.txt - This file follows the format of ```A. ExampleMulti1,B. ExampleMulti2,C. ExampleMulti3,D. ExampleMulti4```.Only "ExampleMulti" should be changed. If there's a space inbetween the multichoice answer and the comma or the comma and the character, then the project will break
- quizzAnswers.txt - On each line, only the character of right multichoice answer should be there
- quizzHighscore - Do NOT touch this. It's a memory file that keeps track of your scores

## 💫 Future Updates
- Insert & save quiz questions directly from the program itself
- GUI
- AI Explanation at answers you got wrong

## ⬇️ Installation
Download QuizzFolder and extract it wherever you think is best. After you do, get the *Directory Path* in which the folder is in.

Open Quizz.py inside the folder using your own IDE. Scroll down to the very bottom until you find `def currentDirectory()`. Inside that function, you will have to insert your *Directory Path* within the quotation marks. For example:
Download Folder Example:
- MacOs: os.chdir(r"/Users/YourUser/Downloads/QuizzV1")
- Windows: os.chdir(r"\Users\YourUser\Downloads\QuizzV1")

## ❓ Don't Have Python?
If you do not have python yet, make sure to install it from their official website:
- Windows: https://www.python.org/downloads/windows/
- MacOS: https://www.python.org/downloads/macos/

To check if you have Python, open the terminal on your Operating System and type:
- Windows: `python --version`
- MacOs: `python3 --version`

## ✍️ Authors
**paycheckbelfast**
- Github: https://github.com/paycheckbelfast
- Website: https://readymag.website/u3762128447/paycheckbelfastportfolio/
- LinkedIn: https://www.linkedin.com/in/david-mihai-5a8422381/
- StackOverflow: https://stackoverflow.com/users/32137262/paycheckbelfast
