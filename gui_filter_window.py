# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.check_name = QtWidgets.QCheckBox(self.centralwidget)
        self.check_name.setObjectName("check_name")
        self.horizontalLayout_2.addWidget(self.check_name)
        self.check_desc = QtWidgets.QCheckBox(self.centralwidget)
        self.check_desc.setObjectName("check_desc")
        self.horizontalLayout_2.addWidget(self.check_desc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Search:"))
        self.check_name.setText(_translate("MainWindow", "Name"))
        self.check_desc.setText(_translate("MainWindow", "Description"))
        self.label.setText(_translate("MainWindow", "Class:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Any"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Barbarian"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bard"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cleric"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Druid"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Fighter"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Monk"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Paladin"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Ranger"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Sorcerer"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Warlock"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Wizard"))
        self.label_2.setText(_translate("MainWindow", "Level"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Any"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "9"))
        self.pushButton.setText(_translate("MainWindow", "Update"))

