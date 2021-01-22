# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(449, 564)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(29, 200, 295, 321))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.seven = QPushButton(self.gridLayoutWidget)
        self.seven.setObjectName(u"seven")

        self.gridLayout.addWidget(self.seven, 0, 0, 1, 1)

        self.four = QPushButton(self.gridLayoutWidget)
        self.four.setObjectName(u"four")

        self.gridLayout.addWidget(self.four, 1, 0, 1, 1)

        self.two = QPushButton(self.gridLayoutWidget)
        self.two.setObjectName(u"two")

        self.gridLayout.addWidget(self.two, 2, 1, 1, 1)

        self.one = QPushButton(self.gridLayoutWidget)
        self.one.setObjectName(u"one")

        self.gridLayout.addWidget(self.one, 2, 0, 1, 1)

        self.Three = QPushButton(self.gridLayoutWidget)
        self.Three.setObjectName(u"Three")

        self.gridLayout.addWidget(self.Three, 2, 2, 1, 1)

        self.zero = QPushButton(self.gridLayoutWidget)
        self.zero.setObjectName(u"zero")

        self.gridLayout.addWidget(self.zero, 3, 1, 1, 1)

        self.eight = QPushButton(self.gridLayoutWidget)
        self.eight.setObjectName(u"eight")

        self.gridLayout.addWidget(self.eight, 0, 1, 1, 1)

        self.five = QPushButton(self.gridLayoutWidget)
        self.five.setObjectName(u"five")

        self.gridLayout.addWidget(self.five, 1, 1, 1, 1)

        self.six = QPushButton(self.gridLayoutWidget)
        self.six.setObjectName(u"six")

        self.gridLayout.addWidget(self.six, 1, 2, 1, 1)

        self.nine = QPushButton(self.gridLayoutWidget)
        self.nine.setObjectName(u"nine")

        self.gridLayout.addWidget(self.nine, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(32, 121, 291, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.seven.setText(QCoreApplication.translate("Form", u"7", None))
        self.four.setText(QCoreApplication.translate("Form", u"4", None))
        self.two.setText(QCoreApplication.translate("Form", u"2", None))
        self.one.setText(QCoreApplication.translate("Form", u"1", None))
        self.Three.setText(QCoreApplication.translate("Form", u"3", None))
        self.zero.setText(QCoreApplication.translate("Form", u"0", None))
        self.eight.setText(QCoreApplication.translate("Form", u"8", None))
        self.five.setText(QCoreApplication.translate("Form", u"5", None))
        self.six.setText(QCoreApplication.translate("Form", u"6", None))
        self.nine.setText(QCoreApplication.translate("Form", u"9", None))
    # retranslateUi

