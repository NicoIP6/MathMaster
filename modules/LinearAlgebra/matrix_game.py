from random import randint
from modules.abstract_game import AbstractGame
from algèbre_lineaire import MATRIX
from modules.StudyMaster.revision_master import Revision


# questions = {
#     1: "Multiply the matrix 1 with the matrix 2",
#     2: "Add the matrix 1 with the matrix 2",
#     3: "Is the matrix square ?",
#     4: "Is the matrix identity ?",
#     5: "Is the matrix is triangle ? If yes what kind of triangle ?",
#     6: "Is the matrix diagonal ?",
#     7: "Multiply the matrix with the real",
#     8: "Add the real to the matrix",
#     9: "Find the determinant of the matrix",
#     10: "Find the cofactor matrix of this matrix",
#     11: "Is this matrix inversable ? If yes find it"
# }
class MatrixGame(Revision):
    """

    """
    _registry = []
    score = 0
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry.append(cls)

    @classmethod
    def get_questions(cls):
        return cls._registry

class MultiplyMatbyMat(MatrixGame, AbstractGame):
    """

    """

    def __init__(self):
        self.matrix1 = MATRIX(2,2)
        self.matrix2 = MATRIX(columns=randint(2, 2), lines=self.matrix1.columns)
        super().__init__("nico")
        print(self.show_question())
        print(self.verify_answer())

    def show_question(self):
        """

        :return:
        """
        mata = "\n".join(str(row) for row in self.matrix1.matrix)  # This make more readable and "Mathematical" the matrix
        matb = "\n".join(str(row) for row in self.matrix2.matrix)
        return f"Multiply the matrix 1\n{mata}\nwith the matrix 2\n{matb}"

    def answer(self, mat1, mat2):
        """

        :param mat1: Should be a MATRIX Object (the first  one in the multiplication)
        :param mat2: Should be a MATRIX Object (the second  one in the multiplication)
        :return:
        """

        return mat1.matrix_mult_by_matrix(mat2)

    def get_answer(self):
        count = 0
        user_answer = []
        print("Enter your response for the vector separate only by a whitespace ex : '36 28 22' :\n")
        while count < self.matrix1.lines:
            ans = input(f"Vector {count + 1} :\n")
            ans = ans.strip().split(" ")
            if any([i.isalpha() or i.isspace() or i in ("-", "+", "*") for i in ans]):
                print("you enter a character which is not a numeric or to much whitespace, try again for this vector only")
            else:
                ans = [int(i) for i in ans]
                user_answer.append(ans)
                count += 1

        return user_answer


    def verify_answer(self):
        sys_ans = self.answer(self.matrix1, self.matrix2)
        use_ans = self.get_answer()
        if use_ans == sys_ans:
            Revision.total_score += 1
            MatrixGame.score += 1
            return "Well Done !"
        else:
            return f"sorry the answer was {sys_ans}"




if __name__ == "__main__":
    MultiplyMatbyMat()
