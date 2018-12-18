#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:15:33 2018

@author: jacobpelletier
"""
"""
Criteria:
    1) Game has 3 or more levels and each level contains 4 or more blanks to fill in
    2) Immediately after running the program, the user should be prompted to select a difficulty level
    3) Once a level is selected, game displays a fill-in-the-blan promt to fill in the first blank
    4) When player guesses correctly, new promt shows correct answer in the previous blank and a new promt for the next blank
    5) when player guesses incorrectly, they are promted to try again.
"""
def global_greeting(user_name):
   #input: takes in user's name
   #output: displays greeting with user's name
    return ('Hello' + ' ' + user_name + '! ' + 'Welcome to Jake\'s Udacity Quiz'
           'Game. This quiz game covers topics in Python.')
def ans_in_question(question, answer): #1
    #input: takes in a string question, and a list of answers
    #output: if a word in answer is in answer (ans), return ans, otherwise return none
    for ans in answer: #2
        if ans in question: #3
            return ans #4
    return None #5
def easyquestions(question, answer):
    #takes in a question as a string, and a list of answers
    #makes strings into lists, whereby common word (answer) is found, and allows matching input to the answer
    #if input is not == to answer, prompts redo as determined by difficulty
    question_with_blank = []
    question_with_ans = []
    question = question.split()
    answer = answer.split()
    count = 2
    for blank in question:
        replace_blank = ans_in_question(question, answer)
        if replace_blank != None:
            blank = blank.replace(replace_blank, '______')
            question_with_blank.append(blank + " ")
        else:
            question_with_blank.append(blank + " ")
    for word in question:
        replace_word = ans_in_question(question, answer)
        if replace_word != None:
            word = word.replace(replace_word, (''.join(answer)))
            question_with_ans.append(word + " ")
        else:
            question_with_ans.append(word + " ")  
    question_with_blank = ''.join(question_with_blank)
    question_with_ans = ''.join(question_with_ans)
    print ('\n')
    print (question_with_blank)
    user_answer = input('Fill in the blank with the correct answer: ')
    while count > 0:
        if user_answer == (''.join(answer)):
            print ('Correct!' + ' ' + question_with_ans)
            return
        else:
            user_answer = input('Fill in the blank with the correct answer: ')
            count -= 1
        if count == 0:   
            print ('Wrong. ' + question_with_ans)
            print ('Try again!')
            return ('Try again!')
    
def moderatequestions(question, answer):
    #takes in a question as a string, and a list of answers
    #makes strings into lists, whereby common word (answer) is found, and allows matching input to the answer
    #if input is not == to answer, prompts redo as determined by difficulty
    question_with_blank = []
    question_with_ans = []
    question = question.split()
    answer = answer.split()
    count = 1
    for blank in question:
        replace_blank = ans_in_question(question, answer)
        if replace_blank != None:
            blank = blank.replace(replace_blank, '______')
            question_with_blank.append(blank + " ")
        else:
            question_with_blank.append(blank + " ")
    for word in question:
        replace_word = ans_in_question(question, answer)
        if replace_word != None:
            word = word.replace(replace_word, (''.join(answer)))
            question_with_ans.append(word + " ")
        else:
            question_with_ans.append(word + " ")  
    question_with_blank = ''.join(question_with_blank)
    question_with_ans = ''.join(question_with_ans)
    print ('\n')
    print (question_with_blank)
    user_answer = input('Fill in the blank with the correct answer: ')
    while count > 0:
        if user_answer == (''.join(answer)):
            print ('Correct!' + ' ' + question_with_ans)
            return
        else:
            user_answer = input('Fill in the blank with the correct answer: ')
            count -= 1
        if count == 0:   
            print ('Wrong. ' + question_with_ans)
            print ('Try again!')
            return ('Try again!')
    
def hardquestions(question, answer):
    #takes in a question as a string, and a list of answers
    #makes strings into lists, whereby common word (answer) is found, and allows matching input to the answer
    #if input is not == to answer, prompts redo as determined by difficulty
    question_with_blank = []
    question_with_ans = []
    question = question.split()
    answer = answer.split()
    count = 0
    for blank in question:
        replace_blank = ans_in_question(question, answer)
        if replace_blank != None:
            blank = blank.replace(replace_blank, '______')
            question_with_blank.append(blank + " ")
        else:
            question_with_blank.append(blank + " ")
    for word in question:
        replace_word = ans_in_question(question, answer)
        if replace_word != None:
            word = word.replace(replace_word, (''.join(answer)))
            question_with_ans.append(word + " ")
        else:
            question_with_ans.append(word + " ")  
    question_with_blank = ''.join(question_with_blank)
    question_with_ans = ''.join(question_with_ans)
    print ('\n')
    print (question_with_blank)
    user_answer = input('Fill in the blank with the correct answer: ')
    if user_answer == (''.join(answer)):
        return ('Correct!' + ' ' + question_with_ans)
    else:
        print ('Wrong. ' + question_with_ans)
        print ('Try again!')
        return ('Try again!')
        count == 0
def easy():
    #function to introduce easy mode
    return ('\nWelcome to easy mode! Here, we will cover using variables in python,'
            ' data types, and lists. You have three chances per question. Each'
            ' question is worth one point each!'
            ' Fill in the blank with the appropriate answers:')
def moderate():
    #function to introduce moderate mode
    return ('\nWelcome to moderate mode! Here, we will cover the use of loops and index.' 
            ' You have two chances per question. Each question is worth two points each!'
            ' Fill in the blank with the appropriate answers:')
def hard():
    #function to introduce hard mode
    return ('\nWelcome to hard mode! Here, we will cover functions in python,'
          ' data types, and lists. You have one chance per question.' 
          ' Each question is worth three points each!'
          ' Fill in the blank with the appropriate answers:')    
user_name = (input('What is your name? ' + ''))
print (global_greeting(user_name))
about_intro = (input('Would you like to know more about this game? Please enter "yes" or "no": '))
while about_intro != 'yes' or 'no':
    if about_intro == 'yes':
        print ('\nThe purpose of this game is to quiz your knowledge of Python!'
               ' There are three difficulty levels you may choose from. 1) Easy difficulty'
               ' covers python basics. 2) Moderate difficulty covers iterative looping.'
               ' 3) Hard difficulty covers functions.')
        break
    elif about_intro == 'no':
        print ('Ok then, here we go!')
        break
    else:
        about_intro = (input('Would you like to know more about this game? Please enter "yes" or "no": '))
while choosing_difficulty != '1' or '2' or '3':
    choosing_difficulty = (input('Enter difficulty level: "1", "2", or "3": '))
    if choosing_difficulty == '1':
        print (easy())
        if (easyquestions('a variable approximates the value', 'variable')) != 'Try again!':
            if (easyquestions('a string is a series of characters', 'string')) != 'Try again!':
                if (easyquestions('an integer is a number without a decimal point', 'integer')) != 'Try again!':
                    if (easyquestions('a float is a number with a decimal point', 'float')) != 'Try again!':
                        print ('\n')
                        print ('Are you ready for the next difficulty?')
                        next_level = (input('"yes" or "no": '))
                        print ('\n')
                        if next_level == 'yes':
                            choosing_difficulty = (input('Enter difficulty level "2" or "3": '))
                        elif next_level == 'no':
                            print ('Try again!')
                        else: 
                            choosing_difficulty = (input('Enter difficulty level "2" or "3": '))  
    if choosing_difficulty == '2':
        print (moderate())
        if (moderatequestions('an index starts at 0, not 1', 'index')) != 'Try again!':
            if (easyquestions('the append method allows you to add to the end of a list', 'append')) != 'Try again!':
                if (easyquestions('Is it FOR or WHILE? for number in range(0-4)','for')) != 'Try again!':
                    if (easyquestions('Is it FOR or WHILE? while number < 0', 'while')) != 'Try again!':
                        print ('\n')
                        print ('Are you ready for the next difficulty?')
                        next_level = (input('"yes" or "no": '))
                        print ('\n')
                        if next_level == 'yes':
                            choosing_difficulty = (input('Enter difficulty level "3": '))
                        elif next_level == 'no':
                                print ('Try again!')
                        else: 
                            choosing_difficulty = (input('Enter difficulty level "3": '))
 
    if choosing_difficulty == '3':
        print (hard())
        if (hardquestions('a function is a block of code designed to do a specific job', 'function')) != 'Try again!':
            if (easyquestions('when you want to use a particular function, you call it\'s name', 'call')) != 'Try again!':
                if (easyquestions('an argument is what you pass into the function', 'argument')) != 'Try again!':
                    if (easyquestions('to begin DEFINING a function, you type the three letters: def', 'def')) != 'Try again!':
                        print ('\nCongrats' + ' ' + user_name.title() + '! ' + 'You win the game!')
                        print ('Play again!')
                    else:
                        print ('Try again!')
    
    
    
                           

  
    
    
    