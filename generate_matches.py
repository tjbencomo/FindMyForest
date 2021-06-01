"""
Generates matches given a CSV file with student and 
club info from Qualtrics survery. Questions in the CSV files
must align with the question IDs found in loader.py.
"""

import loader
import match
import csv


def rank(students, clubs, weighted = False):
    matches = {}
    for student in students:
        ranks = match.rank_clubs(student, clubs, weighted)
        matches[student] = ranks
    return matches

def display_matches(student, clubs):
    print(f"The top matches for {student.name} are:")
    n = min(3, len(clubs))
    for i in range(n):
        print(f"{i+1}. {clubs[i][0].name} ({clubs[i][1]})")

def save_matches(fp, matches):
    with open(fp, 'w', newline='\n') as f:
        writer = csv.writer(f)
        cols = ['studentName', 'studentEmail', 'club1Name', 'club1Description', 'club1Email', 'club2Name', 'club2Description', 'club2Email', 'club3Name', 'club3Description', 'club3Email']
        writer.writerow(cols)
        for student in matches:
            out = [student.name, student.email]
            for i in range(3):
                club = matches[student][i][0]
                out = out + [club.name, club.description, club.contact_email]
            writer.writerow(out)

def main():
    # clubs_fp = 'test-data/clubs.csv'
    # students_fp = 'test-data/students.csv'
    clubs_fp = 'final-data/clubs.csv'
    students_fp = 'final-data/students.csv'
    student_qs, club_qs, qids = loader.get_questions()
    students = loader.load_students(students_fp, student_qs, qids)
    clubs = loader.load_clubs(clubs_fp, club_qs, qids)
    matches = rank(students, clubs)
    weighted_matches = rank(students, clubs, weighted = True)
    # for student in matches:
    #     print("Unweighted:")
    #     display_matches(student, matches[student])
    #     print("Weighted:")
    #     display_matches(student, weighted_matches[student])
    save_matches('unweighted_matches.csv', matches)
    save_matches('weighted_matches.csv', weighted_matches)

if __name__ == '__main__':
    main()
