from copy import deepcopy
from random import randint


class MATRIX:
    """

    """

    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.matrix = [[1,3,0,1], [2,0,1,2], [1,2,1,5], [5,3,1,4]] # [[randint(0, 21) for _ in range(columns)] for _ in range(lines)]

    # @classmethod
    # def is_matrix(cls, matrix):
    #     """
    #
    #     :param self:
    #     :return:
    #     """
    #     if isinstance(matrix, int):
    #         return False
    #     print(matrix)
    #     len_vector = len(matrix)
    #     is_mat = True
    #     for i in range(0, len(matrix)):
    #         if len(matrix[i]) != len_vector:
    #             is_mat = False
    #
    #     return is_mat


    @classmethod
    def is_square(cls, matrix):
        """

        :param matrix:
        :return:
        """

        len_mat = len(matrix)
        len_vec = len(matrix[0])
        if len_mat == len_vec:
            return True
        else:
            return False


    @classmethod
    def is_diagonal(cls, matrix):
        """

        :param matrix: must be a square matrix
        :return: True or False as if the matrix is diagonal or not
        """
        is_diag = True
        diag = []
        for indexVec, vector in enumerate(matrix):
            for indexElem, element in enumerate(vector):
                if indexElem != indexVec and element != 0:
                    is_diag = False
                if indexVec == indexElem:
                    diag.append(element)

        return is_diag, diag


    @classmethod
    def is_bottom_triangle(cls, matrix):
        """

        :param matrix: must be a square matrix
        :return: True or False as if the matrix is Bottom Triangle or not
        """

        is_bot_tri = True
        for indexVec, vector in enumerate(matrix):
            for indexElem, element in enumerate(vector):
                if indexVec < indexElem and element != 0:
                    is_bot_tri = False
        return is_bot_tri


    @classmethod
    def is_top_triangle(cls, matrix):
        """

        :param matrix: must be a square matrix
        :return: True or False as if the matrix is Top Triangle or not
        """

        is_top_tri = True
        for indexVec, vector in enumerate(matrix):
            for indexElem, element in enumerate(vector):
                if indexVec > indexElem and element != 0:
                    is_top_tri = False
        return is_top_tri


    @classmethod
    def is_triangle(cls, matrix):
        """

        :param matrix: must be a square matrix
        :return: True or False as if the matrix is Triangle or not (despite if it's top or bottom)
        """

        is_tri = False
        if cls.is_top_triangle(matrix) or cls.is_bottom_triangle(matrix):
            is_tri = True
        return is_tri


    @classmethod
    def is_identity(cls, matrix):
        """

        :param matrix: must be a square matrix
        :return: True or False as if the matrix is Triangle or not (despite if it's top or bottom)
        """
        param_mat = cls.is_diagonal(matrix)
        if param_mat[0] and all(i == 1 for i in param_mat[1]):
            return True
        else:
            return False


    @classmethod
    def is_equal(cls, matrix1, matrix2):
        """

        :param matrix1:
        :param matrix2:
        :return:
        """
        return True if matrix1.matrix == matrix2.matrix else False


    @classmethod
    def add_matt(cls, matrix1, matrix2):
        """

        :param matrix1:
        :param matrix2:
        :return:
        """
        len1, len2 = len(matrix1), len(matrix2)
        len_vector1, len_vector2 = len(matrix1[0]), len(matrix2[0])
        if len1 != len2 or len_vector1 != len_vector2:
            return "these matrix can't be added"

        added_matrix = []
        for i in range(0, len1):
            temp = []
            for j in range(0, len_vector1):
                temp.append(matrix1[i][j] + matrix2[i][j])
            added_matrix.append(temp)


        return added_matrix


    @classmethod
    def matrix_mult_by_r(cls, matrix1, real):
        """

        :param matrix1:
        :param real:
        :return:
        """

        if isinstance(real, float):
            for i in range(0, len(matrix1)):
                for j in range(0, len(matrix1[0])):
                    matrix1[i][j] = matrix1[i][j] * real
            return matrix1
        else:
            return "Something went wrong with the multiplication by a real"


    @classmethod
    def matrix_mult_by_matrix(cls, matrix1, matrix2):

        res_matrix = []
        if len(matrix1[0]) != len(matrix2):
            return "these matrix can't be multiplied by themselves"
        else:
            for index_m1, elem_m1 in enumerate(matrix1):
                temp_vec = []
                temp_vec.extend(0 for i in range(len(matrix2[0])))
                for index_vec1, elem_vec1 in enumerate(elem_m1):
                    for index_vec2, elem_vec2 in enumerate(matrix2[index_vec1]):
                        temp_vec[index_vec2] += (elem_vec1 * elem_vec2)
                res_matrix.append(temp_vec)

        return res_matrix


    @classmethod
    def exponential_matrix(cls, matrix, exp):
        """

        :param exp:
        :param matrix:
        :return:
        """
        res = matrix
        if cls.is_square(matrix):
            for i in range(exp - 1):
                res = cls.matrix_mult_by_matrix(res, matrix)
            return res
        else:
            return "Not possible to expose"


    @classmethod
    def transpose_matrix(cls, matrix1):
        """

        :param matrix1:
        :return:
        """
        transposed_matrix = []
        for i in range(len(matrix1[0])):
            transposed_matrix.append([])
        for i in matrix1:
            for index, elem in enumerate(i):
                transposed_matrix[index].append(elem)
        return transposed_matrix


    @classmethod
    def cofactor_matrix(cls, matrix1):
        """

        :param matrix1:
        :return:
        """
        cofactor_mat = []
        if len(matrix1) == 2:
            return "no cofactor matrix for a range 2 matrix"

        for index_vector in range(len(matrix1)):
            new_vector  = []
            for index_elem in range(len(matrix1[index_vector])):
                temp_matrix = deepcopy(matrix1)
                temp_matrix.pop(index_vector)
                temp_object = MATRIX(len(temp_matrix), len(temp_matrix[0]))
                temp_object.matrix = temp_matrix
                for i in temp_object.matrix:
                     i.pop(index_elem)
                if len(temp_object.matrix) == 2:
                    cofactor = cls.determinant_by_cofactor(temp_object.matrix)
                    new_vector.append(cofactor)
                elif len(temp_matrix) > 2:
                    cofactor = cls.determinant_by_cofactor(temp_object.matrix)
                    new_vector.append(cofactor)
            for i in range(len(new_vector)):
                new_vector[i] = new_vector[i] * ((-1) ** (i + index_vector))
            cofactor_mat.append(new_vector)

        return cofactor_mat


    # def matrix_determinant(self):
    #     """
    #
    #     :param self:
    #     :return:
    #     """
    #     if not self.is_square():
    #         return "You can't find a determinant"
    #     elif len(self.matrix[0]) == 2:
    #         return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])


    @classmethod
    def determinant_by_cofactor(cls, matrix):
        """

        :param matrix:
        :return:
        """

        if not cls.is_square(matrix):
            return "You can't find a determinant"
        elif len(matrix[0]) == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        else:
            determinant = 0
            vector = matrix[0]
            cofac_vector = cls.cofactor_matrix(matrix)
            for i in range(len(vector)):
                determinant += (vector[i] * cofac_vector[0][i])

        return determinant


    @classmethod
    def inverse_matrix(cls, matrix):
        """

        :param matrix:
        :return:
        """

        if len(matrix) == 2:
            if cls.determinant_by_cofactor(matrix) == 0:
                return "This matrix can't be inverted (determinant = 0)"
            else:
                det_mat = cls.determinant_by_cofactor(matrix)
        else:
            if cls.determinant_by_cofactor(matrix) == 0:
                return "This matrix can't be inverted (determinant = 0)"
            else:
                det_mat = cls.determinant_by_cofactor(matrix)
        cofactor_matrix = MATRIX(1,1)
        cofactor_matrix.matrix = cls.cofactor_matrix(matrix)
        transposed_cofmat = MATRIX(1,1)
        transposed_cofmat.matrix = cls.transpose_matrix(cofactor_matrix.matrix)
        #print(det_mat)
        return cls.matrix_mult_by_r(transposed_cofmat.matrix, 1/det_mat)


test = MATRIX(6,6)
print(test.matrix)
print(20* "-")
print(MATRIX.cofactor_matrix(test.matrix))
print(20* "-")
print(test.determinant_by_cofactor(test.matrix))
print(20* "-")
print(MATRIX.transpose_matrix(test.matrix))
print(20* "-")
print(MATRIX.inverse_matrix(test.matrix))
