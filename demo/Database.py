# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:41:05 2019

@author: Siddhi
"""

import sqlite3
Game=sqlite3.connect('Game.db')
cur=Game.cursor()
cur.execute(''' CREATE TABLE Questions (
QID INTEGER PRIMARY KEY,
QUESTION TEXT,
Option1 TEXT,
Option2 TEXT,
Option3 TEXT,
Option4 TEXT,
ANSWER TEXT);''')
Game.close()