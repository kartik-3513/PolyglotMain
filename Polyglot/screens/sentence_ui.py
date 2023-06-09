# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Projects\btp8\Polyglot\screens\sentence.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_player_window(object):
    def setupUi(self, player_window):
        player_window.setObjectName("player_window")
        player_window.setEnabled(True)
        player_window.resize(1067, 774)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(player_window.sizePolicy().hasHeightForWidth())
        player_window.setSizePolicy(sizePolicy)
        player_window.setAutoFillBackground(False)
        player_window.setStyleSheet("background: rgb(43, 46, 59);\n"
"")
        self.layout = QtWidgets.QWidget(player_window)
        self.layout.setMinimumSize(QtCore.QSize(1067, 661))
        self.layout.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.layout.setStyleSheet("QWidget#landing{\n"
"background: rgb(43, 46, 59);\n"
"}")
        self.layout.setObjectName("layout")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layout)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setSizeIncrement(QtCore.QSize(10, 10))
        self.frame.setBaseSize(QtCore.QSize(200, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphTitle_l = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphTitle_l.sizePolicy().hasHeightForWidth())
        self.graphTitle_l.setSizePolicy(sizePolicy)
        self.graphTitle_l.setMinimumSize(QtCore.QSize(0, 60))
        self.graphTitle_l.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.graphTitle_l.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.graphTitle_l.setWordWrap(True)
        self.graphTitle_l.setObjectName("graphTitle_l")
        self.verticalLayout_5.addWidget(self.graphTitle_l)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.graphWidget = PlotWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setAutoFillBackground(True)
        self.graphWidget.setStyleSheet("background: rgb(FF, FF, FF);")
        self.graphWidget.setObjectName("graphWidget")
        self.verticalLayout_5.addWidget(self.graphWidget)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 10)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.instructions_l = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instructions_l.sizePolicy().hasHeightForWidth())
        self.instructions_l.setSizePolicy(sizePolicy)
        self.instructions_l.setMinimumSize(QtCore.QSize(0, 60))
        self.instructions_l.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.instructions_l.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.instructions_l.setScaledContents(False)
        self.instructions_l.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.instructions_l.setWordWrap(True)
        self.instructions_l.setObjectName("instructions_l")
        self.verticalLayout.addWidget(self.instructions_l)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.english_l = QtWidgets.QLabel(self.frame)
        self.english_l.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.english_l.sizePolicy().hasHeightForWidth())
        self.english_l.setSizePolicy(sizePolicy)
        self.english_l.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.english_l.setObjectName("english_l")
        self.verticalLayout.addWidget(self.english_l)
        self.english_edit = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.english_edit.sizePolicy().hasHeightForWidth())
        self.english_edit.setSizePolicy(sizePolicy)
        self.english_edit.setMinimumSize(QtCore.QSize(550, 0))
        self.english_edit.setMaximumSize(QtCore.QSize(1000000, 200))
        self.english_edit.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.english_edit.setPlainText("")
        self.english_edit.setObjectName("english_edit")
        self.verticalLayout.addWidget(self.english_edit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.hindi_l = QtWidgets.QLabel(self.frame)
        self.hindi_l.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.hindi_l.setObjectName("hindi_l")
        self.verticalLayout.addWidget(self.hindi_l)
        self.hindi_edit = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hindi_edit.sizePolicy().hasHeightForWidth())
        self.hindi_edit.setSizePolicy(sizePolicy)
        self.hindi_edit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.hindi_edit.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.hindi_edit.setObjectName("hindi_edit")
        self.verticalLayout.addWidget(self.hindi_edit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.nepali_l = QtWidgets.QLabel(self.frame)
        self.nepali_l.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.nepali_l.setObjectName("nepali_l")
        self.verticalLayout.addWidget(self.nepali_l)
        self.nepali_edit = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nepali_edit.sizePolicy().hasHeightForWidth())
        self.nepali_edit.setSizePolicy(sizePolicy)
        self.nepali_edit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.nepali_edit.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"color: white;")
        self.nepali_edit.setObjectName("nepali_edit")
        self.verticalLayout.addWidget(self.nepali_edit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_b = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_b.sizePolicy().hasHeightForWidth())
        self.back_b.setSizePolicy(sizePolicy)
        self.back_b.setMinimumSize(QtCore.QSize(100, 50))
        self.back_b.setBaseSize(QtCore.QSize(100, 100))
        self.back_b.setStyleSheet(":enabled {\n"
"border-radius: 0px;\n"
"font-family: Courier New;\n"
"color: #ffffff;\n"
"font-size: 14pt;\n"
"background: transparent;\n"
"padding: 10pt 20pt 10pt 20pt;\n"
"border: 5px solid #ffffff;\n"
"text-decoration: none;\n"
"}\n"
":hover {\n"
"background: white;\n"
"color: rgb(43, 46, 59);\n"
"border: 0px;\n"
"}")
        self.back_b.setDefault(False)
        self.back_b.setFlat(False)
        self.back_b.setObjectName("back_b")
        self.horizontalLayout_3.addWidget(self.back_b)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.analyse_b_xlmr = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyse_b_xlmr.sizePolicy().hasHeightForWidth())
        self.analyse_b_xlmr.setSizePolicy(sizePolicy)
        self.analyse_b_xlmr.setMinimumSize(QtCore.QSize(120, 50))
        self.analyse_b_xlmr.setBaseSize(QtCore.QSize(100, 100))
        self.analyse_b_xlmr.setStyleSheet(":enabled {\n"
"border-radius: 0px;\n"
"font-family: Courier New;\n"
"color: #ffffff;\n"
"font-size: 14pt;\n"
"background: transparent;\n"
"padding: 10pt 20pt 10pt 20pt;\n"
"border: 5px solid #ffffff;\n"
"text-decoration: none;\n"
"}\n"
":hover {\n"
"background: white;\n"
"color: rgb(43, 46, 59);\n"
"border: 0px;\n"
"}")
        self.analyse_b_xlmr.setDefault(False)
        self.analyse_b_xlmr.setFlat(False)
        self.analyse_b_xlmr.setObjectName("analyse_b_xlmr")
        self.horizontalLayout_3.addWidget(self.analyse_b_xlmr)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.analyse_b_labse = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyse_b_labse.sizePolicy().hasHeightForWidth())
        self.analyse_b_labse.setSizePolicy(sizePolicy)
        self.analyse_b_labse.setMinimumSize(QtCore.QSize(120, 50))
        self.analyse_b_labse.setBaseSize(QtCore.QSize(100, 100))
        self.analyse_b_labse.setStyleSheet(":enabled {\n"
"border-radius: 0px;\n"
"font-family: Courier New;\n"
"color: #ffffff;\n"
"font-size: 14pt;\n"
"background: transparent;\n"
"padding: 10pt 20pt 10pt 20pt;\n"
"border: 5px solid #ffffff;\n"
"text-decoration: none;\n"
"}\n"
":hover {\n"
"background: white;\n"
"color: rgb(43, 46, 59);\n"
"border: 0px;\n"
"}")
        self.analyse_b_labse.setDefault(False)
        self.analyse_b_labse.setFlat(False)
        self.analyse_b_labse.setObjectName("analyse_b_labse")
        self.horizontalLayout_3.addWidget(self.analyse_b_labse)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.analyse_b_mpnet = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyse_b_mpnet.sizePolicy().hasHeightForWidth())
        self.analyse_b_mpnet.setSizePolicy(sizePolicy)
        self.analyse_b_mpnet.setMinimumSize(QtCore.QSize(120, 50))
        self.analyse_b_mpnet.setBaseSize(QtCore.QSize(100, 100))
        self.analyse_b_mpnet.setStyleSheet(":enabled {\n"
"border-radius: 0px;\n"
"font-family: Courier New;\n"
"color: #ffffff;\n"
"font-size: 14pt;\n"
"background: transparent;\n"
"padding: 10pt 20pt 10pt 20pt;\n"
"border: 5px solid #ffffff;\n"
"text-decoration: none;\n"
"}\n"
":hover {\n"
"background: white;\n"
"color: rgb(43, 46, 59);\n"
"border: 0px;\n"
"}")
        self.analyse_b_mpnet.setDefault(False)
        self.analyse_b_mpnet.setFlat(False)
        self.analyse_b_mpnet.setObjectName("analyse_b_mpnet")
        self.horizontalLayout_3.addWidget(self.analyse_b_mpnet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        player_window.setCentralWidget(self.layout)

        self.retranslateUi(player_window)
        QtCore.QMetaObject.connectSlotsByName(player_window)

    def retranslateUi(self, player_window):
        _translate = QtCore.QCoreApplication.translate
        player_window.setWindowTitle(_translate("player_window", "MainWindow"))
        self.graphTitle_l.setText(_translate("player_window", "Visualisation of sentence embeddings of different languages in 2D vector space"))
        self.instructions_l.setText(_translate("player_window", "Input sentences and analyse to get two dimensional sentence embeddings"))
        self.english_l.setText(_translate("player_window", "English:"))
        self.hindi_l.setText(_translate("player_window", "Hindi:"))
        self.nepali_l.setText(_translate("player_window", "Nepali:"))
        self.back_b.setText(_translate("player_window", "Back"))
        self.analyse_b_xlmr.setText(_translate("player_window", "XLMR"))
        self.analyse_b_labse.setText(_translate("player_window", "LaBSE"))
        self.analyse_b_mpnet.setText(_translate("player_window", "MPNet"))
from pyqtgraph import PlotWidget
