# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Debug_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 171)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 90, 181, 16))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 181, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 70, 181, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setGeometry(QtCore.QRect(20, 110, 181, 16))
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setObjectName("radioButton_9")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 10, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 90, 181, 16))
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 50, 181, 16))
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setGeometry(QtCore.QRect(20, 70, 181, 16))
        self.radioButton_8.setObjectName("radioButton_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 110, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 10, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_11.setGeometry(QtCore.QRect(20, 50, 181, 16))
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_12.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_13.setGeometry(QtCore.QRect(20, 70, 181, 16))
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Debug模式"))
        self.groupBox.setTitle(_translate("Form", "通道"))
        self.radioButton_4.setText(_translate("Form", "3 channel test"))
        self.radioButton_2.setText(_translate("Form", "CH39"))
        self.radioButton.setText(_translate("Form", "CH9"))
        self.radioButton_3.setText(_translate("Form", "CH72"))
        self.radioButton_9.setText(_translate("Form", "Full channel test"))
        self.groupBox_2.setTitle(_translate("Form", "温度"))
        self.radioButton_5.setText(_translate("Form", "Full temperature"))
        self.radioButton_6.setText(_translate("Form", "25C"))
        self.radioButton_7.setText(_translate("Form", "-5C"))
        self.radioButton_8.setText(_translate("Form", "75C"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "手动下电"))
        self.groupBox_3.setTitle(_translate("Form", "ICR测试选择"))
        self.checkBox_11.setText(_translate("Form", "Rx BW test"))
        self.checkBox_12.setText(_translate("Form", "Phase error test"))
        self.checkBox_13.setText(_translate("Form", "Responsivity test"))
        self.pushButton_3.setText(_translate("Form", "写入SN"))
