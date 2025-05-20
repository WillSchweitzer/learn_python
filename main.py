"""main"""
from src import Queue, Student

def main ():
    """Main function"""
    students = Queue[Student]()

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
