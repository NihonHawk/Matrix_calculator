# -*- coding: utf-8 -*-
from sre_compile import isstring
import numpy as np  # библиотека для работы с матрицами 


def converter(matrix_string):
    # Преобразование строки в массив для модуля numpy
    matrix_array = matrix_string.replace("\n"," ").replace("\t", " ").split()

    # Проверка размера матрицы
    if len(matrix_array) ** 0.5 % 1  != 0:
        return 'Некорректный размер матрицы'

    # Проверка наличия цифр в матрице и последующее преобразование в массив
    for items in range(len(matrix_array)):
        if not matrix_array[items].isdigit():
            return 'Ошибка ввода'
        else:
            matrix_array[items] = int(matrix_array[items])

    size = int(len(matrix_array) ** 0.5)
    return np.array(matrix_array).reshape(size, size)


def oneMatrix(matrix, function, number=None):
    # Операции над 1 матрицой
    match function:
        case 'Определитель':
            return np.around(np.linalg.det(matrix), decimals=3, out=None)
        case 'Транспонирование':
            result = matrix.transpose()
        case 'Обратная':
            result = np.around(np.linalg.inv(matrix), decimals=3, out=None)
        case 'Скаляр':
            result = matrix * number
    return '\n'.join(['   '.join(map(str, result[i])) for i in range(len(result))])

    

def twoMatrix(matrixA, function, matrixB):
    # Операции над 2 матрицами
    if isinstance(matrixA, str):
        return matrixA
    if isinstance(matrixB, str):
        return matrixB
    else:    
        if len(matrixA) != len(matrixB):
            return 'Разный размер матриц'
        else:
            match function:
                case 'Сложение':
                    result = matrixA + matrixB
                case 'Вычитание':
                    result = matrixA - matrixB 
                case 'Умножение':     
                    result = np.matmul(matrixA, matrixB)
            
            return '\n'.join(['   '.join(map(str, result[i])) for i in range(len(result))])
