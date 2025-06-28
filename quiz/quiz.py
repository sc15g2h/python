import csv
import re

def validateInput(answer):
    # validate input 
    if(bool(re.findall('[ABCDabcd]',answer)) & len(answer)==1 ):
        return answer
    else:
        userin = input("Invalid input. Try again: ") 
        validateInput(userin)


def printQuestion(counter, row):
    print("Question " + str(counter) + " : " + re.sub('\"', '', row[0]))
    print("A: " + row[1])
    print("B: " + row[2])
    print("C: " + row[3])
    print("D: " + row[4])

def checkAnswer(input, answer):
    if(input.lower() == re.sub('\"', '', answer.lower())):
        print("Correct")
        return 1
    else:
        print("Incorrect")


def main():
    score = 0

    with open('quiz.csv', newline='') as csvfile:
        questions = csv.reader(csvfile, delimiter='\t', quotechar='|')
        counter = 0 
        for q in questions:
            counter+=1
            
            printQuestion(counter,q)
            userin = input("Choose your answer: ").strip()

            validin = validateInput(userin)

            score += checkAnswer(validin, q[5])

        print("You finished the quiz! Your score was " + str(score))

             
main()
