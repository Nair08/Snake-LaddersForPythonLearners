# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:42:25 2019

@author: Siddhi
"""


#from tkinter import *


import sqlite3
import random
import pygame

pygame.init()


conn=sqlite3.connect('SnakesandLadder.db')

def read_from_db():
# =============================================================================
#     c.execute('SELECT Option2 FROM Answers where QID is 2')
#     data6= c.fetchall()
# =============================================================================
    
   

    #selection = "You selected the option " + str(var.get())
   #label.config(text = selection)
    
    


# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
    



    snakes = {
         98: 79,
         95: 75,
         93: 73,
         87: 36,
         64: 60,
         62: 19,
         54: 34,
         17: 7
       
        
    }

# ladder takes you up from 'key' to 'value'
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
}


display_width = 800
display_height = 750
board_y = 40
board_x = 150
dude_start_x = 100
dude_start_y = 500
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
screen = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()
outer_crashed = False
board: object = pygame.image.load('Snakes-and-Ladders-Bigger.jpg')
dude = pygame.image.load('chotabheem.png')
outer_score = 0

def getanswer():
# =============================================================================
#     c.execute('SELECT Option2 FROM Answers where QID is 2')
#     data6= c.fetchall()
# =============================================================================
    c=conn.cursor()
    c.execute('SELECT QID FROM QandA')
    id= c.fetchall()
    n= random.choice(id)
    print(n)
    c.execute('SELECT Question FROM QandA where QID is (?)', (n))
    que= c.fetchall()
    print("1." , que)
    
    c.execute('SELECT Option1 FROM QandA where QID is (?)', (n))
    opt1= c.fetchall()
    print("A. " ,opt1)
    
    c.execute('SELECT Option2 FROM QandA where QID is (?)', (n))
    opt2= c.fetchall()
    print("B. " ,opt2)
    
    c.execute('SELECT Option3 FROM QandA where QID is (?)', (n))
    opt3= c.fetchall()
    print("C. ",opt3)
    
    c.execute('SELECT Option4 FROM QandA where QID is (?)', (n))
    opt4= c.fetchall()
    print("D. ",opt4)
    
    c.execute('SELECT ANSWER FROM QandA where QID is (?)', (n))
    ans=c.fetchall()
    answer = ans[0][0]
   
    
    userInput = input(" Choose A B C or D: ")
    
    if userInput == answer:
        return True
    else:
        return False
   
   
   
def getscore(score,answer):


        if answer == True:
            if None != (snakes.get(score)):
                score = score + 1

                i = score
                print("i1", i)
            elif None != ladders.get(score):
                score = ladders.get(score)

                print("score2", score)
                i = score
                print("i2", i)
            else:
                score = score + 1

                print("score3", score)
                i = score
                print("i3", i)

        else:

            if None != (snakes.get(score)):
                score = snakes.get((score))
                i = score
                print("i1", i)
                print("score4", score)
                print("hello")

        return score
def move(x, y):
    screen.blit(dude, (x, y))


def displayboard(x, y):
    screen.blit(board, (x, y))

def get_position(score):
    l1 = [[115, 490], [165, 490], [215, 490], [265, 490], [315, 490], [365, 490], [415, 490], [465, 490], [515, 490],
          [565, 490], [615, 490],
        [615, 440],[565, 440], [515, 440], [465, 440], [415, 440], [365, 440], [315, 440], [265, 440], [215, 440],[165, 440],
        [165, 390],[215, 390], [265, 390], [315, 390], [365, 390], [415, 390], [465, 390], [515, 390], [565, 390],[615, 390],
        [615, 340],[565, 340], [515, 340], [465, 340], [415, 340], [365, 340], [315, 340], [265, 340], [215, 340],[165, 340],
        [165, 290],[215, 290], [265, 290], [315, 290], [365, 290], [415, 290], [465, 290], [515, 290], [565, 290],[615, 290],
        [615, 240],[565, 240], [515, 240], [465, 240], [415, 240], [365, 240], [315, 240], [265, 240], [215, 240],[165, 240],
        [165, 190],[215, 190], [265, 190], [315, 190], [365, 190], [415, 190], [465, 190], [515, 190], [565, 190],[615, 190],
        [615, 140],[565, 140], [515, 140], [465, 140], [415, 140], [365, 140], [315, 140], [265, 140], [215, 140],[165, 140],
        [165, 90],[215, 90], [265, 90], [315, 90], [365, 90], [415, 90], [465, 90], [515, 90], [565, 90],[615, 90],
        [615, 50],[565, 50], [515, 50], [465, 50], [415, 50], [365, 50], [315, 50], [265, 50], [215, 50],[165, 50]
        ]
    l2 = l1[score]
    x = l2[0]
    y = l2[1]
    return x, y

def game_loop(crashed,score):
    bheema_x = 115
    bheema_y = 490
    x_change=0
    direction = 'right'

    while not crashed and score < 100:
        displayboard(board_x, board_y)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                   answer=getanswer()
                   score = getscore(score, answer)
                   print("score---", score)
                   bheema_x, bheema_y = get_position(score)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        screen.fill((0, 0, 0))
        displayboard(board_x, board_y)

        move(bheema_x, bheema_y)
        pygame.display.update()
        clock.tick(10)


game_loop(outer_crashed,outer_score)
pygame.quit()
quit()

import pygame

pygame.init()
snakes = {
    98: 79,
    95: 75,
    93: 73,
    87: 36,
    64: 60,
    62: 19,
    54: 34,
    17: 7
}

# ladder takes you up from 'key' to 'value'
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
}


display_width = 800
display_height = 750
board_y = 40
board_x = 150
dude_start_x = 100
dude_start_y = 500
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
screen = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()
outer_crashed = False
board: object = pygame.image.load('Snakes-and-Ladders-Bigger.jpg')
dude = pygame.image.load('chotabheem.png')
outer_score = 0

def getscore(score):

        answer = 5
        answer2: int = 6
        if answer == answer2:
            if None != (snakes.get(score)):
                score = score + 1

                i = score
                print("i1", i)
            elif None != ladders.get(score):
                score = ladders.get(score)

                print("score2", score)
                i = score
                print("i2", i)
            else:
                score = score + 1

                print("score3", score)
                i = score
                print("i3", i)

        else:

            if None != (snakes.get(score)):
                score = snakes.get((score))
                i = score
                print("i1", i)
                print("score4", score)
                print("hello")

        return score
def move(x, y):
    screen.blit(dude, (x, y))


def displayboard(x, y):
    screen.blit(board, (x, y))

def get_position(score):
    l1 = [[115, 490], [165, 490], [215, 490], [265, 490], [315, 490], [365, 490], [415, 490], [465, 490], [515, 490],
          [565, 490], [615, 490],
        [615, 440],[565, 440], [515, 440], [465, 440], [415, 440], [365, 440], [315, 440], [265, 440], [215, 440],[165, 440],
        [165, 390],[215, 390], [265, 390], [315, 390], [365, 390], [415, 390], [465, 390], [515, 390], [565, 390],[615, 390],
        [615, 340],[565, 340], [515, 340], [465, 340], [415, 340], [365, 340], [315, 340], [265, 340], [215, 340],[165, 340],
        [165, 290],[215, 290], [265, 290], [315, 290], [365, 290], [415, 290], [465, 290], [515, 290], [565, 290],[615, 290],
        [615, 240],[565, 240], [515, 240], [465, 240], [415, 240], [365, 240], [315, 240], [265, 240], [215, 240],[165, 240],
        [165, 190],[215, 190], [265, 190], [315, 190], [365, 190], [415, 190], [465, 190], [515, 190], [565, 190],[615, 190],
        [615, 140],[565, 140], [515, 140], [465, 140], [415, 140], [365, 140], [315, 140], [265, 140], [215, 140],[165, 140],
        [165, 90],[215, 90], [265, 90], [315, 90], [365, 90], [415, 90], [465, 90], [515, 90], [565, 90],[615, 90],
        [615, 50],[565, 50], [515, 50], [465, 50], [415, 50], [365, 50], [315, 50], [265, 50], [215, 50],[165, 50]
        ]
    l2 = l1[score]
    x = l2[0]
    y = l2[1]
    return x, y

def game_loop(crashed,score):
    bheema_x = 115
    bheema_y = 490
    x_change=0
    direction = 'right'

    while not crashed and score < 100:
        displayboard(board_x, board_y)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    

                    score=getscore(score)
                    print("score---",score)
                    bheema_x,bheema_y= get_position(score)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        screen.fill((0, 0, 0))
        displayboard(board_x, board_y)

        move(bheema_x, bheema_y)
        pygame.display.update()
        clock.tick(10)


game_loop(outer_crashed,outer_score)
pygame.quit()
quit()

