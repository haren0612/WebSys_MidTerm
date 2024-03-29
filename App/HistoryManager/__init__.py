class HistoryManager:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def clear_history(self):
        self.records.clear()

    def show_history(self):
        if len(self.records) == 0:
            print("No records found")
        else:
            for record in self.records:
                print(record)