from copy import deepcopy
from random import randint


class MATRIX:
    """

    """

    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.matrix = [[1,3,0,1], [2,0,1,2], [1,2,1,5], [5,3,1,4]] # [[randint(0, 21) for _ in range(columns)] for _ in range(lines)]


    def is_square(self):

        """

        :return:
        """

        len_mat = len(self.matrix)
        len_vec = len(self.matrix[0])
        if len_mat == len_vec:
            return True
        else:
            return False


    def is_diagonal(self):

        """

        :return: return a tuple with True or False in the first position
                 and the diagonal in the second (empty list if False).
                 Return a note if not a square matrix
        """

        if not self.is_square():
            return "Not a Square matrix so it can't have a diagonal"
        is_diag = True
        diag = []
        for indexVec, vector in enumerate(self.matrix):
            for indexElem, element in enumerate(vector):
                if indexElem != indexVec and element != 0:
                    is_diag = False
                if indexVec == indexElem:
                    diag.append(element)

        return is_diag, diag


    def is_bottom_triangle(self):

        """

        :return: return True if the object attribute "matrix" is a bottom triangle False otherwise.
                 return a note if not a square matrix.
        """

        if not self.is_square():
            return "Not a Square matrix so it can't be triangle"
        is_bot_tri = True
        for indexVec, vector in enumerate(self.matrix):
            for indexElem, element in enumerate(vector):
                if indexVec < indexElem and element != 0:
                    is_bot_tri = False
        return is_bot_tri


    def is_top_triangle(self):

        """

        :return: return True if the object attribute "matrix" is a top triangle False otherwise.
                 return a note if not a square matrix.
        """

        if not self.is_square():
            return "Not a Square matrix so it can't be triangle"
        is_top_tri = True
        for indexVec, vector in enumerate(self.matrix):
            for indexElem, element in enumerate(vector):
                if indexVec > indexElem and element != 0:
                    is_top_tri = False
        return is_top_tri


    def is_triangle(self):

        """

        :return: True or False as if the matrix is Triangle or not (despite if it's top or bottom)
        """

        is_tri = False
        if self.is_top_triangle() or self.is_bottom_triangle():
            is_tri = True
        return is_tri


    def is_identity(self):

        """
        :return: True or False as if the matrix is Triangle or not (despite if it's top or bottom)
        """

        param_mat = self.is_diagonal()
        if param_mat[0] and all(i == 1 for i in param_mat[1]):
            return True
        else:
            return False


    def is_equal(self, matrix2):

        """
        :param matrix2: must be a second MATRIX Object
        :return: True if the first and the second matrix are equal. Return a note if matrix2 is not a MATRIX instance.
        """

        if not isinstance(matrix2, MATRIX):
            return "The second argument must be a matrix object"

        return True if self.matrix == matrix2.matrix else False


    def add_matt(self, matrix2):

        """
        :param matrix2: must be a second MATRIX Object
        :return: Return a new matrix that reflects the addition of the matrix.
        """

        len1, len2 = len(self.matrix), len(matrix2.matrix)
        len_vector1, len_vector2 = len(self.matrix[0]), len(matrix2.matrix[0])
        if len1 != len2 or len_vector1 != len_vector2:
            return "these matrices can't be added"

        added_matrix = []
        for i in range(0, len1):
            temp = []
            for j in range(0, len_vector1):
                temp.append(self.matrix[i][j] + matrix2.matrix[i][j])
            added_matrix.append(temp)

        return added_matrix


    def matrix_mult_by_r(self, real):

        """
        :param real: must be the real number that will be used to multiply the matrix.
        :return: Return a new matrix with all the element multiply by the real
        """

        if isinstance(real, float):
            mult_mat = deepcopy(self.matrix)
            for i in range(len(mult_mat)):
                for j in range(len(mult_mat[0])):
                    mult_mat[i][j] = mult_mat[i][j] * real
            return mult_mat
        else:
            return "Something went wrong with the multiplication by a real"


    def matrix_mult_by_matrix(self, matrix2):

        """
        :param matrix2: must be a second MATRIX Object
        :return: Return a new matrix with the result of the multiplication of two matrix.
        """

        if not isinstance(matrix2, MATRIX):
            return "The argument must be a MATRIX object it's actually not."
        res_matrix = []
        if len(self.matrix[0]) != len(matrix2.matrix):
            return "these matrix can't be multiplied by themselves"
        else:
            for index_m1, elem_m1 in enumerate(self.matrix):
                temp_vec = []
                temp_vec.extend(0 for i in range(len(matrix2.matrix[0])))
                for index_vec1, elem_vec1 in enumerate(elem_m1):
                    for index_vec2, elem_vec2 in enumerate(matrix2.matrix[index_vec1]):
                        temp_vec[index_vec2] += (elem_vec1 * elem_vec2)
                res_matrix.append(temp_vec)

        return res_matrix


    def exponential_matrix(self, exp):

        """

        :param exp: The exponential number for the matrix
        :return: Return a new matrix with the result
        """

        res = MATRIX(6,6)
        res.matrix = deepcopy(self.matrix)
        if self.is_square():
            for i in range(exp - 1):
                res.matrix = self.matrix_mult_by_matrix(res)
            return res.matrix
        else:
            return "Not possible to expose"


    def transpose_matrix(self):

        """

        :return: return the transposed matrix
        """

        transposed_matrix = []
        for i in range(len(self.matrix[0])):
            transposed_matrix.append([])
        for i in self.matrix:
            for index, elem in enumerate(i):
                transposed_matrix[index].append(elem)

        return transposed_matrix


    def cofactor_matrix(self):

        """

        :return: Return the cofactor matrix of object's matrix
        """

        cofactor_mat = []
        if len(self.matrix) == 2:
            return "no cofactor matrix for a range 2 matrix"

        for index_vector in range(len(self.matrix)):
            new_vector  = []
            for index_elem in range(len(self.matrix[index_vector])):
                temp_matrix = deepcopy(self.matrix)
                temp_matrix.pop(index_vector)
                temp_object = MATRIX(len(temp_matrix), len(temp_matrix[0]))
                temp_object.matrix = temp_matrix
                for i in temp_object.matrix:
                     i.pop(index_elem)
                if len(temp_object.matrix) == 2:
                    cofactor = temp_object.determinant_by_cofactor()
                    new_vector.append(cofactor)
                elif len(temp_matrix) > 2:
                    cofactor = temp_object.determinant_by_cofactor()
                    new_vector.append(cofactor)
            for i in range(len(new_vector)):
                new_vector[i] = new_vector[i] * ((-1) ** (i + index_vector))
            cofactor_mat.append(new_vector)

        return cofactor_mat


    def determinant_by_cofactor(self):

        """

        :return: Return the determinant of the object's matrix
        """

        if not self.is_square():
            return "You can't find a determinant"
        elif len(self.matrix[0]) == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
        else:
            determinant = 0
            vector = self.matrix[0]
            cofac_vector = self.cofactor_matrix()
            for i in range(len(vector)):
                determinant += (vector[i] * cofac_vector[0][i])

        return determinant


    def inverse_matrix(self):

        """

        :return: Return the inverse object's matrix
        """

        if self.determinant_by_cofactor() == 0:
            return "This matrix can't be inverted (determinant = 0)"
        else:
            det_mat = self.determinant_by_cofactor()
        cofactor_matrix = MATRIX(1,1)
        cofactor_matrix.matrix = self.cofactor_matrix()
        transposed_cofmat = MATRIX(1,1)
        transposed_cofmat.matrix = cofactor_matrix.transpose_matrix()
        #print(det_mat)
        return transposed_cofmat.matrix_mult_by_r(1/det_mat)


matrix_test = [[2], [6], [1], [0.25]]
test = MATRIX(6,6)
test2 = MATRIX(6,6)
test2.matrix = matrix_test
print(test.matrix)
print(20* "-")
print(test.cofactor_matrix())
print(20* "-")
print(test.determinant_by_cofactor())
print(20* "-")
print(test.transpose_matrix())
print(20* "-")
print(test.inverse_matrix())
print(20* "-")
print(test.add_matt(test2))
print(20* "-")
print(test.matrix_mult_by_r(1.2))
print(20* "-")
print(test.matrix_mult_by_matrix(test2))
print(20* "-")
print(test.matrix)
