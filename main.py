# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

from page1 import Ui_MatrixCalc
from page2 import ui_page2
from calc import converter, oneMatrix, twoMatrix


class page1(QtWidgets.QMainWindow):
    def __init__(self):
        super(page1, self).__init__()
        self.ui = Ui_MatrixCalc()
        self.ui.setupUi(self)

        #BUTTONS
        self.ui.Question.clicked.connect(self.quest)

        self.ui.plus.clicked.connect(self.addition)
        self.ui.mult.clicked.connect(self.multiplication)
        self.ui.minus.clicked.connect(self.subtraction)
        
        self.ui.A_Transpose.clicked.connect(self.transposeA)
        self.ui.B_Transpose.clicked.connect(self.transposeB)

        self.ui.A_Reverse.clicked.connect(self.reverseA)
        self.ui.B_Reverse.clicked.connect(self.reverseB)

        self.ui.A_Det.clicked.connect(self.A_Det)
        self.ui.B_Det.clicked.connect(self.B_Det)

        self.ui.A_Mult.clicked.connect(self.scalarA)
        self.ui.B_Mult.clicked.connect(self.scalarB)

    #Two matrix addition
    def addition(self):
        matrix1 = converter(self.ui.A_Matrix_Input.toPlainText())
        matrix2 = converter(self.ui.B_Matrix_Input.toPlainText())
        try:
            result = twoMatrix(matrix1, 'Сложение', matrix2)
        except:
            self.ui.label.setText('Error')
        else:
            self.ui.label.setText(result)

    #Two matrix multiplication
    def multiplication(self):
        matrix1 = converter(self.ui.A_Matrix_Input.toPlainText())
        matrix2 = converter(self.ui.B_Matrix_Input.toPlainText())
        try:
            result = twoMatrix(matrix1, 'Умножение', matrix2)
        except:
            self.ui.label.setText('Error')
        else:                
            self.ui.label.setText(result) 

    #Two matrix subtraction
    def subtraction(self):
            matrix1 = converter(self.ui.A_Matrix_Input.toPlainText())
            matrix2 = converter(self.ui.B_Matrix_Input.toPlainText())
            try:
                res = twoMatrix(matrix1, 'Вычитание', matrix2)
            except:
                self.ui.label.setText('Error')
            else:
                self.ui.label.setText(res)

    # One matrix scalar
    def scalarA(self):
        matrix = converter(self.ui.A_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            try:
                number = int(self.ui.A_Input.text())
            except:
                self.ui.label.setText("Error:\n Скаляр не цифра или не задан")
            else:
                self.ui.label.setText(oneMatrix(matrix, "Скаляр", number)) 

    def scalarB(self):
        matrix = converter(self.ui.B_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            try:
                number = int(self.ui.B_Input.text())
            except:
                self.ui.label.setText("Error:\n Скаляр не цифра или не задан")
            else:
                self.ui.label.setText(oneMatrix(matrix, "Скаляр", number)) 

    # One matrix det 
    def A_Det(self):
        matrix = converter(self.ui.A_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            res = oneMatrix(matrix, 'Определитель')
            self.ui.label.setText(str(oneMatrix(matrix, 'Определитель')))

    def B_Det(self):
        matrix = converter(self.ui.B_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            self.ui.label.setText(str(oneMatrix(matrix, 'Определитель')))

    # One matrix transpose
    def transposeA(self):
        matrix = converter(self.ui.A_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            self.ui.label.setText(oneMatrix(matrix, 'Транспонирование'))

    def transposeB(self):
        matrix = converter(self.ui.B_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            self.ui.label.setText(oneMatrix(matrix,'Транспонирование'))

    # One matrix reverse
    def reverseA(self):
        matrix = converter(self.ui.A_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)  
        else:
            try:
                res = oneMatrix(matrix,'Обратная')
            except:
                self.ui.label.setText('Error:\nНевозможно обратить')
            else:
                self.ui.label.setText(res)

    def reverseB(self):
        matrix = converter(self.ui.B_Matrix_Input.toPlainText())
        if isinstance(matrix, str):
            self.ui.label.setText(matrix)
        else:
            try:
                res = oneMatrix(matrix,'Обратная')
            except:
                self.ui.label.setText('Error:\nНевозможно обратить')
            else:
                self.ui.label.setText(res)   

    # Help
    def quest(self):
        self.question = page2()
 
class page2(QtWidgets.QMainWindow):
    def __init__(self):
        super(page2, self).__init__()
        self.ui = ui_page2()
        self.ui.setupUi(self)
        self.show()

app = QtWidgets.QApplication([])
application = page1()
application.show()

sys.exit(app.exec())