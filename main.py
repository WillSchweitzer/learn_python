"""main"""
from src import ClassQueue, Student

def main ():
    """Main function"""
    students = ClassQueue[Student]()

    data: dict[str, str | int | float] = {
        'first' : 'Will',
        'last' : 'Schweitzer',
        'age' : 28,
        'gpa' : 3.55,
        'email' : 'willschw@pdx.edu'
    }

    students.enqueue(Student(data))
    print(students.dequeue())

if __name__ == '__main__':
    main()
