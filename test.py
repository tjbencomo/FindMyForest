from match import Student, Club
import match

QUESTIONS = ['q1', 'q2', 'q3']

def create_students():
    s1 = Student('Bob', QUESTIONS, ['weak ties', 5, 'none'])
    s2 = Student('Jill', QUESTIONS, ['strong ties', 3, 'candy'])
    s3 = Student('Jack', QUESTIONS, ['solo', 0, 'jam'])
    return [s1, s2, s3]

def create_clubs():
    c1 = Club('SSI', QUESTIONS, ['weak ties', 3, 'none'])
    c2 = Club('TBP', QUESTIONS, ['strong ties', 1, 'jam'])
    c3 = Club('TreeHacks', QUESTIONS, ['weak ties', 7, 'candy'])
    c4 = Club('Losers', QUESTIONS, ['no ties', 1000, 'popcorn'])
    return [c1, c2, c3, c4]

def test(students, clubs):
    for student in students:
        print(f"Ranking clubs for {student.name}")
        ranks = match.rank_clubs(student, clubs)
        print([str(club) for club in ranks])

def main():
    students = create_students()
    clubs = create_clubs()
    test(students, clubs)

if __name__ == '__main__':
    main()
