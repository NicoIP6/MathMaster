from abc import ABC, abstractmethod
class AbstractGame(ABC):
    """

    """

    @abstractmethod
    def show_question(self):
        pass

    @abstractmethod
    def answer(self, *args):
        pass

    @abstractmethod
    def get_answer(self):
        pass

    @abstractmethod
    def verify_answer(self):
        pass
