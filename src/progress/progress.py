class Progress:
    def __init__(self, user_id, course_id, percent_complete):
        self.user_id = user_id
        self.course_id = course_id
        self.percent_complete = percent_complete

    def show_progress(self):
        print(f"User {self.user_id} has completed {self.percent_complete}% of course {self.course_id}")
