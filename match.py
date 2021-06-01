"""
Matching algorithm for FindMyForest. Rank the optimal clubs for a student
given the student's answers to the typeform questionaire and a list of data
about each club
"""
import math
import numpy as np

weighted_questions = list(range(10)) + [12, 16] + list(range(17, 21))

class Club():
    def __init__(self, name, contact_name, contact_email, description, questions, answers):
        if len(questions) != len(answers):
            raise ValueError("Number of questions does not much number of answers!")
        self.name = name
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.description = description
        self.info = dict(zip(questions, answers))

    def __str__(self):
        return f"Club: {self.name}"

class Student():
    def __init__(self, name, email, affinity, questions, answers):
        if len(questions) != len(answers):
            raise ValueError("Number of questions does not much number of answers!")
        self.name = name
        self.email = email
        self.interestedInAffinity = affinity
        self.info = dict(zip(questions, answers))

    def __str__(self):
        return  f"Student: {self.name}"

def categorical_loss(student, club, weight):
    # print(f"Categorical loss: {student}, {club}")
    if student == club:
        # print(1)
        return 1 * weight
    # print(-1)
    return -1 * weight

def numeric_loss(student, club, weight):
    # print(f"Numeric Loss: {student}, {club}")
    # print(-abs(student - club))
    return -abs(student - club) * weight

def list_loss(student, club, weight):
    # print(f"Student: {student}, dtype: {type(student)}")
    # print(f"Club: {club}, dtype: {type(club)}")
    if isinstance(student, float) or isinstance(student, int):
        slist = set([student])
    else:
        slist = set(student.split(','))
    if isinstance(club, float) or isinstance(club, int):
        clist = set([club])
    else:
        clist = set(club.split(','))
    # print(len(slist & clist))
    return len(slist & clist) * weight

def get_loss_type(studentResponse, clubResponse):
    if isinstance(studentResponse, str) or isinstance(clubResponse, str):
        studentResponse = str(studentResponse)
        clubResponse = str(clubResponse)
    if isinstance(studentResponse, str):
        if ',' in studentResponse or ',' in clubResponse:
            return list_loss
        else:
            return categorical_loss
    elif isinstance(studentResponse, int) or isinstance(studentResponse, float):
        return numeric_loss
    else:
        raise ValueError(f"Student response is type {type(student)}. Similarity calculation is undefined")

# student - object of type Student
# club - object of type Club
def calculate_loss(student, club, weighted): 
    loss = 0
    for q in student.info:
        if weighted and q in weighted_questions:
            w = 3
        else:
            w = 1
        # print(f'Assessing {q}')
        f = get_loss_type(student.info[q], club.info[q])
        loss += f(student.info[q], club.info[q], w)
    # print(f"Loss: {loss}")
    return loss

def rank_clubs(student, clubs, weighted):
    losses = [calculate_loss(student, club, weighted) for club in clubs]
    ranks = zip(clubs, losses)
    ranks = sorted(ranks, key = lambda t: t[1], reverse = True)
    return ranks



