class Revision:
    total_score = 0
    def __init__(self, name):
        self.name = name
        self.score = 0
    # def ask_question(self):
    #     pass
    @staticmethod
    def show_score():
        return f"Total score = {Revision.total_score}"