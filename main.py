from src import *

def main ():
    students = ClassQueue[Student]()
    students.enqueue(Student("Will", 'Schweitzer', 28, 3.55, 'willschw@pdx.edu'))
    print(students.dequeue())

if __name__ == '__main__':
    main()