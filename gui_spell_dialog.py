# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spell_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 439)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.casting_layout = QtWidgets.QHBoxLayout()
        self.casting_layout.setObjectName("casting_layout")
        self.casting_time_lbl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.casting_time_lbl.setFont(font)
        self.casting_time_lbl.setObjectName("casting_time_lbl")
        self.casting_layout.addWidget(self.casting_time_lbl)
        self.casting_time_val = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.casting_time_val.sizePolicy().hasHeightForWidth())
        self.casting_time_val.setSizePolicy(sizePolicy)
        self.casting_time_val.setObjectName("casting_time_val")
        self.casting_layout.addWidget(self.casting_time_val)
        self.verticalLayout.addLayout(self.casting_layout)
        self.range_layout = QtWidgets.QHBoxLayout()
        self.range_layout.setObjectName("range_layout")
        self.range_lbl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.range_lbl.setFont(font)
        self.range_lbl.setObjectName("range_lbl")
        self.range_layout.addWidget(self.range_lbl)
        self.range_text = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.range_text.sizePolicy().hasHeightForWidth())
        self.range_text.setSizePolicy(sizePolicy)
        self.range_text.setObjectName("range_text")
        self.range_layout.addWidget(self.range_text)
        self.verticalLayout.addLayout(self.range_layout)
        self.Comp_layout = QtWidgets.QHBoxLayout()
        self.Comp_layout.setObjectName("Comp_layout")
        self.comp_layout = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comp_layout.setFont(font)
        self.comp_layout.setObjectName("comp_layout")
        self.Comp_layout.addWidget(self.comp_layout)
        self.comp_text = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comp_text.sizePolicy().hasHeightForWidth())
        self.comp_text.setSizePolicy(sizePolicy)
        self.comp_text.setObjectName("comp_text")
        self.Comp_layout.addWidget(self.comp_text)
        self.verticalLayout.addLayout(self.Comp_layout)
        self.dur_layout = QtWidgets.QHBoxLayout()
        self.dur_layout.setObjectName("dur_layout")
        self.dur_lbl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dur_lbl.setFont(font)
        self.dur_lbl.setObjectName("dur_lbl")
        self.dur_layout.addWidget(self.dur_lbl)
        self.dur_text = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dur_text.sizePolicy().hasHeightForWidth())
        self.dur_text.setSizePolicy(sizePolicy)
        self.dur_text.setObjectName("dur_text")
        self.dur_layout.addWidget(self.dur_text)
        self.verticalLayout.addLayout(self.dur_layout)
        self.class_layout = QtWidgets.QHBoxLayout()
        self.class_layout.setObjectName("class_layout")
        self.class_lbl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.class_lbl.setFont(font)
        self.class_lbl.setObjectName("class_lbl")
        self.class_layout.addWidget(self.class_lbl)
        self.class_text = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_text.sizePolicy().hasHeightForWidth())
        self.class_text.setSizePolicy(sizePolicy)
        self.class_text.setObjectName("class_text")
        self.class_layout.addWidget(self.class_text)
        self.verticalLayout.addLayout(self.class_layout)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Spell"))
        self.label.setText(_translate("Dialog", "SPELLNAME"))
        self.label_2.setText(_translate("Dialog", "Nth Level Illusion"))
        self.casting_time_lbl.setText(_translate("Dialog", "Casting Time:"))
        self.casting_time_val.setText(_translate("Dialog", "CASTINGTIMETEXT"))
        self.range_lbl.setText(_translate("Dialog", "Range:"))
        self.range_text.setText(_translate("Dialog", "RANGE TEXT"))
        self.comp_layout.setText(_translate("Dialog", "Components:"))
        self.comp_text.setText(_translate("Dialog", "COMPONENTS"))
        self.dur_lbl.setText(_translate("Dialog", "Duration:"))
        self.dur_text.setText(_translate("Dialog", "DURATION"))
        self.class_lbl.setText(_translate("Dialog", "Classes:"))
        self.class_text.setText(_translate("Dialog", "CLASSES"))

