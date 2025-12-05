class Course:
    def __init__(self, course_id, title, instructor):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor

    def course_info(self):
        print(f"Course ID: {self.course_id}, Title: {self.title}, Instructor: {self.instructor}")
