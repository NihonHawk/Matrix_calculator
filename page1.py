# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatrixCalc(object):
    def setupUi(self, MatrixCalc):
        MatrixCalc.setObjectName("MatrixCalc")
        MatrixCalc.resize(854, 640)
        MatrixCalc.setStyleSheet("*{background-color:rgb(54,54,54);color:white;font-family:Times New Roman;}\n"
"QTextEdit{border:1px solid rgba(0, 128, 255, 1);border-radius:10px;}\n"
"QPushButton{border: 1px solid rgba(0, 128, 255, 1); color:white;font-size:17px}\n"
"QPushButton:hover{color:rgba(0, 128, 255, 1);}\n"
"QPushButton:pressed{color:red;}\n"
"QLabel{background-color:none}\n"
"QLineEdit{border:1px solid rgba(0, 128, 255, 1)}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MatrixCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.A_Matrix_Input = QtWidgets.QTextEdit(self.centralwidget)
        self.A_Matrix_Input.setGeometry(QtCore.QRect(40, 30, 331, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.A_Matrix_Input.setFont(font)
        self.A_Matrix_Input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.A_Matrix_Input.setToolTipDuration(0)
        self.A_Matrix_Input.setObjectName("A_Matrix_Input")
        self.B_Matrix_Input = QtWidgets.QTextEdit(self.centralwidget)
        self.B_Matrix_Input.setGeometry(QtCore.QRect(490, 30, 331, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.B_Matrix_Input.setFont(font)
        self.B_Matrix_Input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.B_Matrix_Input.setToolTipDuration(0)
        self.B_Matrix_Input.setObjectName("B_Matrix_Input")
        self.matrixA = QtWidgets.QLabel(self.centralwidget)
        self.matrixA.setGeometry(QtCore.QRect(40, 10, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.matrixA.setFont(font)
        self.matrixA.setStyleSheet("")
        self.matrixA.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixA.setObjectName("matrixA")
        self.matrixB = QtWidgets.QLabel(self.centralwidget)
        self.matrixB.setGeometry(QtCore.QRect(490, 10, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.matrixB.setFont(font)
        self.matrixB.setStyleSheet("")
        self.matrixB.setAlignment(QtCore.Qt.AlignCenter)
        self.matrixB.setObjectName("matrixB")
        self.A_Transpose = QtWidgets.QPushButton(self.centralwidget)
        self.A_Transpose.setGeometry(QtCore.QRect(40, 240, 331, 23))
        self.A_Transpose.setObjectName("A_Transpose")
        self.A_Det = QtWidgets.QPushButton(self.centralwidget)
        self.A_Det.setGeometry(QtCore.QRect(40, 270, 331, 23))
        self.A_Det.setObjectName("A_Det")
        self.A_Reverse = QtWidgets.QPushButton(self.centralwidget)
        self.A_Reverse.setGeometry(QtCore.QRect(40, 300, 331, 23))
        self.A_Reverse.setObjectName("A_Reverse")
        self.A_Mult = QtWidgets.QPushButton(self.centralwidget)
        self.A_Mult.setGeometry(QtCore.QRect(40, 330, 331, 21))
        self.A_Mult.setObjectName("A_Mult")
        self.A_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.A_Input.setGeometry(QtCore.QRect(180, 360, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.A_Input.setFont(font)
        self.A_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.A_Input.setObjectName("A_Input")
        self.B_Det = QtWidgets.QPushButton(self.centralwidget)
        self.B_Det.setGeometry(QtCore.QRect(490, 270, 331, 23))
        self.B_Det.setObjectName("B_Det")
        self.B_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.B_Input.setGeometry(QtCore.QRect(630, 360, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.B_Input.setFont(font)
        self.B_Input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.B_Input.setStyleSheet("QLineEdit{\n"
"text-align:center;\n"
"}")
        self.B_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.B_Input.setObjectName("B_Input")
        self.B_Mult = QtWidgets.QPushButton(self.centralwidget)
        self.B_Mult.setGeometry(QtCore.QRect(490, 330, 331, 21))
        self.B_Mult.setObjectName("B_Mult")
        self.B_Transpose = QtWidgets.QPushButton(self.centralwidget)
        self.B_Transpose.setGeometry(QtCore.QRect(490, 240, 331, 23))
        self.B_Transpose.setObjectName("B_Transpose")
        self.B_Reverse = QtWidgets.QPushButton(self.centralwidget)
        self.B_Reverse.setGeometry(QtCore.QRect(490, 300, 331, 23))
        self.B_Reverse.setObjectName("B_Reverse")
        self.mult = QtWidgets.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(400, 70, 61, 41))
        self.mult.setObjectName("mult")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(400, 120, 61, 41))
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(400, 170, 61, 41))
        self.minus.setObjectName("minus")
        self.Question = QtWidgets.QPushButton(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(830, 0, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Question.setFont(font)
        self.Question.setStyleSheet("")
        self.Question.setObjectName("Question")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 390, 341, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("border:1px solid rgb(0, 128, 255);border-radius:10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MatrixCalc.setCentralWidget(self.centralwidget)

        self.retranslateUi(MatrixCalc)
        QtCore.QMetaObject.connectSlotsByName(MatrixCalc)

    def retranslateUi(self, MatrixCalc):
        _translate = QtCore.QCoreApplication.translate
        MatrixCalc.setWindowTitle(_translate("MatrixCalc", "MainWindow"))
        self.A_Matrix_Input.setHtml(_translate("MatrixCalc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\"><br /></span></p></body></html>"))
        self.B_Matrix_Input.setHtml(_translate("MatrixCalc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\"><br /></span></p></body></html>"))
        
        self.matrixA.setText(_translate("MatrixCalc", "Матрица А"))
        self.matrixB.setText(_translate("MatrixCalc", "Матрица B"))
        self.A_Transpose.setText(_translate("MatrixCalc", "Транспонировать"))
        self.A_Det.setText(_translate("MatrixCalc", "Найти определитель"))
        self.A_Reverse.setText(_translate("MatrixCalc", "Найти обратную"))
        self.A_Mult.setText(_translate("MatrixCalc", "Умножить на"))
        self.A_Input.setText(_translate("MatrixCalc", "2"))
        self.B_Det.setText(_translate("MatrixCalc", "Найти определитель"))
        self.B_Input.setText(_translate("MatrixCalc", "2"))
        self.B_Mult.setText(_translate("MatrixCalc", "Умножить на"))
        self.B_Transpose.setText(_translate("MatrixCalc", "Транспонировать"))
        self.B_Reverse.setText(_translate("MatrixCalc", "Найти обратную"))
        self.mult.setText(_translate("MatrixCalc", "A * B"))
        self.plus.setText(_translate("MatrixCalc", "A + B"))
        self.minus.setText(_translate("MatrixCalc", "A - B"))
        self.Question.setText(_translate("MatrixCalc", "?"))
        self.label.setText(_translate("MatrixCalc", ""))