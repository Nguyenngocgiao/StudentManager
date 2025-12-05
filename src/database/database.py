class Database:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables  # list of table names

    def show_tables(self):
        print(f"Database '{self.name}' has tables: {', '.join(self.tables)}")
        #Just a little bit change
        