"""
Matching algorithm for FindMyForest. Rank the optimal clubs for a student
given the student's answers to the typeform questionaire and a list of data
about each club
"""

import numpy as np

class Club():
    def __init__(self, name, questions, answers):
        if len(questions) != len(answers):
            raise ValueError("Number of questions does not much number of answers!")
        self.name = name
        self.info = dict(zip(questions, answers))

    def __str__(self):
        return f"Club: {self.name}"

class Student():
    def __init__(self, name, questions, answers):
        if len(questions) != len(answers):
            raise ValueError("Number of questions does not much number of answers!")
        self.name = name
        self.info = dict(zip(questions, answers))

    def __str__(self):
        return  f"Student: {self.name}"

def categorical_loss(student, club):
    if student == club:
        return 0
    return -1

def numeric_loss(student, club):
    return -abs(student - club)

def get_loss_type(response):
    if isinstance(response, str):
        return categorical_loss
    elif isinstance(response, int) or isinstance(response, float):
        return numeric_loss
    else:
        raise ValueError(f"Student response is type {type(student)}. Similarity calculation is undefined")

# student - object of type Student
# club - object of type Club
def calculate_loss(student, club):
    loss = 0
    for q in student.info:
        f = get_loss_type(student.info[q])
        loss += f(student.info[q], club.info[q])
    return loss

def rank_clubs(student, clubs):
    losses = [calculate_loss(student, club) for club in clubs]
    ranks = zip(clubs, losses)
    ranks = sorted(ranks, key = lambda t: t[1], reverse = True)
    ranks = [t[0] for t in ranks]
    return ranks



