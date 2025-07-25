# from modules.StudyMaster.revision_master import Revision
#
# class LinearAlgebra(Revision):
#     def __init__(self, name):
#         super().__init__(name)
#         print("Module under construction")
def is_square(matrix):
    """

    :param matrix:
    :return:
    """

    if not is_matrix(matrix):
        print("Not a Matrix")
        return False
    len_mat = len(matrix)
    len_vec = len(matrix[0])
    if len_mat == len_vec:
        print("You have a square matrix")
        return True
    else:
        print(f"You have a matrix with {len_mat} lines and {len_vec} colones")
        return False


def is_diagonal(matrix):
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


def is_bottom_triangle(matrix):
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


def is_top_triangle(matrix):
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


def is_triangle(matrix):
    """

    :param matrix: must be a square matrix
    :return: True or False as if the matrix is Triangle or not (despite if it's top or bottom)
    """

    is_tri = False
    if is_top_triangle(matrix) or is_bottom_triangle(matrix):
        is_tri = True
    return is_tri


def is_identity(matrix):
    """

    :param matrix: must be a square matrix
    :return: True or False as if the matrix is Triangle or not (despite if it's top or bottom)
    """
    param_mat = is_diagonal(matrix)
    if param_mat[0] and all(i == 1 for i in param_mat[1]):
        return True
    else:
        return False

def is_equal(matrix1, matrix2):
    """

    :param matrix1:
    :param matrix2:
    :return:
    """
    return True if matrix1 == matrix2 else False


def is_matrix(matrix):
    """

    :param matrix:
    :return:
    """

    len_vector = len(matrix[0])
    is_mat = True
    for i in range(0, len(matrix)):
        if len(matrix[i]) != len_vector:
            is_mat = False

    return is_mat

def add_matt(matrix1, matrix2):
    """

    :param matrix1:
    :param matrix2:
    :return:
    """
    len1, len2 = len(matrix1), len(matrix2)
    len_vector1, len_vector2 = len(matrix1[0]), len(matrix2[0])
    if len1 != len2:
        return "these matrix can't be added"
    if not is_matrix(matrix1) or not is_matrix(matrix2):
        return "one or more parameters given are not a matrix"
    if len_vector1 != len_vector2:
        return "these matrix can't be added"
    added_matrix = []
    for i in range(0, len1):
        temp = []
        for j in range(0, len_vector1):
            temp.append(matrix1[i][j] + matrix2[i][j])
        added_matrix.append(temp)


    return added_matrix


def matrix_mult_by_r(matrix, real):
    """

    :param matrix:
    :param real:
    :return:
    """

    if is_matrix(matrix) and isinstance(real, int):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                matrix[i][j] = matrix[i][j] * real
        return matrix
    else:
        return "Something went wrong with the multiplication by a real"



def matrix_mult_by_matrix(matrix1, matrix2):

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


def exponential_matrix(matrix,exp):
    """

    :param exp:
    :param matrix:
    :return:
    """
    res = matrix
    if is_square(matrix):
        for i in range(exp - 1):
            res = matrix_mult_by_matrix(res, matrix)
        return res
    else:
        return "Not possible to expose"


def transpose_matrix(matrix):
    """

    :param matrix:
    :return:
    """
    transposed_matrix = []
    if not is_matrix(matrix):
        return False
    else:
        for i in range(len(matrix[0])):
            transposed_matrix.append([])
        for i in matrix:
            for index, elem in enumerate(i):
                transposed_matrix[index].append(elem)
        return transposed_matrix


test_matrix = [[2,8,1,1], [1,2,3,1], [1,1,7,1], [2,5,6,1]]
test_matrix2 = [[2,0,0,1,1,1,1], [0,2,0,1,1,1,1], [0,0,2,1,1,1,1]]
print(transpose_matrix(test_matrix2))


# b = """def matrix_mult_by_matrix(matrix1, matrix2):
#     # Vérifie si la multiplication est possible
#     if len(matrix1[0]) != len(matrix2):
#         return "these matrix can't be multiplied by themselves"
#
#     result = []
#
#     # Pour chaque ligne de la première matrice
#     for i in range(len(matrix1)):
#         row_result = []
#
#         # Pour chaque colonne de la deuxième matrice
#         for j in range(len(matrix2[0])):
#             total = 0
#
#             # Effectue le produit scalaire de la ligne i et de la colonne j
#             for k in range(len(matrix2)):
#                 total += matrix1[i][k] * matrix2[k][j]
#
#             row_result.append(total)
#
#         result.append(row_result)
#
#     return result
#
#
# test_matrix = [[2,8,1], [1,2,3], [1,1,7], [2,5,6]]
# test_matrix2 = [[2,0,0,1,1,1,1], [0,2,0,1,1,1,1], [0,0,2,1,1,1,1]]
# print(matrix_mult_by_matrix(test_matrix, test_matrix2))"""
# from timeit import Timer
# t = Timer(a)
# exec2 = t.timeit(100)
# print(exec2)
