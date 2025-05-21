"""main"""
from src import Queue, Student

def main ():
    """Main function"""
    students = Queue[Student]()

    data: tuple[str, str, int, float, str] = ('John', 'Doe', 99, 4.00, 'john_doe@example.com')

    students.enqueue(Student(*data))
    print(students.dequeue())

if __name__ == '__main__':
    main()
