# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 448)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        Form.setFont(font)
        Form.setWindowOpacity(0.8)
        self.WinRate = QtWidgets.QLabel(Form)
        self.WinRate.setGeometry(QtCore.QRect(20, 280, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.WinRate.setFont(font)
        self.WinRate.setAlignment(QtCore.Qt.AlignCenter)
        self.WinRate.setObjectName("WinRate")
        self.UserHandCards = QtWidgets.QLabel(Form)
        self.UserHandCards.setGeometry(QtCore.QRect(260, 210, 421, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.UserHandCards.setFont(font)
        self.UserHandCards.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UserHandCards.setObjectName("UserHandCards")
        self.LPlayer = QtWidgets.QFrame(Form)
        self.LPlayer.setGeometry(QtCore.QRect(20, 80, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LPlayer.setFont(font)
        self.LPlayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LPlayer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LPlayer.setObjectName("LPlayer")
        self.RPlayer = QtWidgets.QFrame(Form)
        self.RPlayer.setGeometry(QtCore.QRect(290, 80, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RPlayer.setFont(font)
        self.RPlayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RPlayer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RPlayer.setObjectName("RPlayer")
        self.RPlayedCard = QtWidgets.QLabel(self.RPlayer)
        self.RPlayedCard.setGeometry(QtCore.QRect(0, 0, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RPlayedCard.setFont(font)
        self.RPlayedCard.setAlignment(QtCore.Qt.AlignCenter)
        self.RPlayedCard.setObjectName("RPlayedCard")
        self.Player = QtWidgets.QFrame(Form)
        self.Player.setGeometry(QtCore.QRect(20, 200, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Player.setFont(font)
        self.Player.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Player.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Player.setObjectName("Player")
        self.PredictedCard = QtWidgets.QLabel(self.Player)
        self.PredictedCard.setGeometry(QtCore.QRect(0, 0, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PredictedCard.setFont(font)
        self.PredictedCard.setStyleSheet("")
        self.PredictedCard.setFrameShape(QtWidgets.QFrame.Panel)
        self.PredictedCard.setLineWidth(1)
        self.PredictedCard.setAlignment(QtCore.Qt.AlignCenter)
        self.PredictedCard.setObjectName("PredictedCard")
        self.ThreeLandlordCards = QtWidgets.QLabel(Form)
        self.ThreeLandlordCards.setGeometry(QtCore.QRect(520, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ThreeLandlordCards.setFont(font)
        self.ThreeLandlordCards.setAlignment(QtCore.Qt.AlignCenter)
        self.ThreeLandlordCards.setObjectName("ThreeLandlordCards")
        self.BidWinrate = QtWidgets.QLabel(Form)
        self.BidWinrate.setGeometry(QtCore.QRect(260, 290, 171, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BidWinrate.setFont(font)
        self.BidWinrate.setObjectName("BidWinrate")
        self.PreWinrate = QtWidgets.QLabel(Form)
        self.PreWinrate.setGeometry(QtCore.QRect(500, 290, 171, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PreWinrate.setFont(font)
        self.PreWinrate.setObjectName("PreWinrate")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(520, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.LPlayedCard = QtWidgets.QLabel(Form)
        self.LPlayedCard.setGeometry(QtCore.QRect(20, 80, 201, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LPlayedCard.setFont(font)
        self.LPlayedCard.setAlignment(QtCore.Qt.AlignCenter)
        self.LPlayedCard.setObjectName("LPlayedCard")
        self.CardsRecorder = QtWidgets.QLabel(Form)
        self.CardsRecorder.setGeometry(QtCore.QRect(20, 10, 431, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CardsRecorder.setFont(font)
        self.CardsRecorder.setStyleSheet("")
        self.CardsRecorder.setAlignment(QtCore.Qt.AlignCenter)
        self.CardsRecorder.setObjectName("CardsRecorder")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(20, 370, 651, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.SingleButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SingleButton.setFont(font)
        self.SingleButton.setObjectName("SingleButton")
        self.LoopButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LoopButton.setFont(font)
        self.LoopButton.setObjectName("LoopButton")
        self.StopButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("StopButton")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 50, 431, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_D = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_D.setFont(font)
        self.label_D.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_D.setText("")
        self.label_D.setAlignment(QtCore.Qt.AlignCenter)
        self.label_D.setObjectName("label_D")
        self.label_X = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_X.setFont(font)
        self.label_X.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_X.setText("")
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_A = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_A.setFont(font)
        self.label_A.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_A.setText("")
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.label_A.setObjectName("label_A")
        self.label_K = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_K.setFont(font)
        self.label_K.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_K.setText("")
        self.label_K.setAlignment(QtCore.Qt.AlignCenter)
        self.label_K.setObjectName("label_K")
        self.label_Q = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Q.setFont(font)
        self.label_Q.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Q.setText("")
        self.label_Q.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Q.setObjectName("label_Q")
        self.label_J = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_J.setFont(font)
        self.label_J.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_J.setText("")
        self.label_J.setAlignment(QtCore.Qt.AlignCenter)
        self.label_J.setObjectName("label_J")
        self.label_T = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_T.setFont(font)
        self.label_T.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_T.setText("")
        self.label_T.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T.setObjectName("label_T")
        self.label_9 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hi"))
        self.WinRate.setText(_translate("Form", "评分"))
        self.UserHandCards.setText(_translate("Form", "手牌"))
        self.RPlayedCard.setText(_translate("Form", "下家出牌区域"))
        self.PredictedCard.setText(_translate("Form", "AI出牌区域"))
        self.ThreeLandlordCards.setText(_translate("Form", "地主牌"))
        self.BidWinrate.setText(_translate("Form", "叫牌胜率："))
        self.PreWinrate.setText(_translate("Form", "局前胜率："))
        self.label.setText(_translate("Form", "游戏状态"))
        self.LPlayedCard.setText(_translate("Form", "上家出牌区域"))
        self.CardsRecorder.setText(_translate("Form", "D X 2 A K Q J 10 9 8 7 6 5 4 3"))
        self.SingleButton.setText(_translate("Form", "单局"))
        self.LoopButton.setText(_translate("Form", " 连续"))
        self.StopButton.setText(_translate("Form", "停止"))
import picture_rc
