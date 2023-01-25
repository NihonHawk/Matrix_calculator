# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class ui_page2(object):
    def setupUi(self, page2):
        page2.setObjectName("MatrixCalc")
        page2.resize(850,460)
        page2.setStyleSheet("*{background-color:rgb(54,54,54);color:white;font-family:Times New Roman;}\n"
        "QTextEdit{border:1px solid rgba(0, 128, 255, 1);border-radius:10px;}\n"
        "QPushButton{border: 1px solid rgba(0, 128, 255, 1); color:white;font-size:17px}\n"
        "QPushButton:hover{color:rgba(0, 128, 255, 1);}\n"
        "QPushButton:pressed{color:red;}\n"
        "QLabel{background-color:none}\n"
        "QLineEdit{border:1px solid rgba(0, 128, 255, 1)}\n"
        "")
        self.centralwidget = QtWidgets.QWidget(page2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 870, 480))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        page2.setCentralWidget(self.centralwidget)

        self.retranslateUi(page2)
        QtCore.QMetaObject.connectSlotsByName(page2)

    def retranslateUi(self, page2):
        _translate = QtCore.QCoreApplication.translate
        page2.setWindowTitle(_translate("MatrixCalc", "MainWindow"))
        self.label.setText(_translate("MatrixCalc", "Руководство по использованию матричного калькулятора: \n"
        "\n"
        "На начальном экране представлены 2 текстовых поля для ввода значений матриц. \n"
        "Ниже текстового поля представлены все реализованные функции над матрицей.\n"
        "Между матрицей А и матрицей В представлены действия с 2 матрицами.\n"
        "\n"
        "Для ввода элементов матрицы необходимо:\n"
        "вводить каждый элемент через пробел или Tab.\n"
        "\n"
        "Пример:\n"
        "1  2  3  4  5\n"
        "11 22 33 44 55\n"
        " 21 22 23 24 25\n"
        "............\n"
        "\n"
        "Количество пробелов может быть любым,\n"
        "и если Вам не хватает строки для ввода строки Вы можете перенести ее на следующую строку,\n"
        "программа подбирает размер матрицы взависимости от количества элементов\nОднако кол-во столбцов и строк должно совпадать!"))
