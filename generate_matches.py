"""
Generates matches given a CSV file with student and 
club info from Qualtrics survery. Questions in the CSV files
must align with the question IDs found in loader.py.
"""

import loader
import match


def rank(students, clubs):
    matches = {}
    for student in students:
        ranks = match.rank_clubs(student, clubs)
        matches[student] = ranks
    return matches

def display_matches(student, clubs):
    print(f"The top matches for {student.name} are:")
    n = min(5, len(clubs))
    for i in range(n):
        print(f"{i+1}. {clubs[i].name}")

def main():
    clubs_fp = 'test-data/clubs.csv'
    students_fp = 'test-data/students.csv'
    student_qs, club_qs, qids = loader.get_questions()
    students = loader.load_students(students_fp, student_qs, qids)
    clubs = loader.load_clubs(clubs_fp, club_qs, qids)
    matches = rank(students, clubs)
    for student in matches:
        display_matches(student, matches[student])
    

if __name__ == '__main__':
    main()
