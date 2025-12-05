from user.user import User
from course.course import Course
from progress.progress import Progress
from payment.payment import Payment
from database.database import Database

def main():
    # Tạo các đối tượng User
    user1 = User(1, "Nguyen Van A", "a@example.com")
    user2 = User(2, "Tran Thi B", "b@example.com")

    # Tạo các đối tượng Course
    course1 = Course(101, "Python Programming", "Mr. Smith")
    course2 = Course(102, "Data Structures", "Ms. Johnson")

    # Tạo các đối tượng Progress
    progress1 = Progress(1, 101, 50)
    progress2 = Progress(2, 102, 80)

    # Tạo các đối tượng Payment
    payment1 = Payment(1001, 1, 49.99)
    payment2 = Payment(1002, 2, 59.99)

    # Tạo đối tượng Database
    db = Database("OnlineLearningDB", ["users", "courses", "progress", "payments"])

    # Hiển thị thông tin
    user1.display_info()
    user2.display_info()

    course1.course_info()
    course2.course_info()

    progress1.show_progress()
    progress2.show_progress()

    payment1.display_payment()
    payment2.display_payment()

    db.show_tables()

if __name__ == "__main__":
    main()
#comment commit 
