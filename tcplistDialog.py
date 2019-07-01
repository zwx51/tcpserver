# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcplistDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import re



class TcplistDialog(QDialog):
    global ui

    def __init__(self):
        global ui
        QDialog.__init__(self)
        ui = Ui_tcplistDialog()
        ui.setupUi(self)


    def settcpdict(self, my_dict):
        global ui
        ui.clearall()
        #pattern = re.compile("'[0-9]*'")

        for key in sorted(my_dict.items(), key=lambda item: item[1]):
            #str_re = pattern.findall(my_dict[key])
            ui.add(key[1][0], key[1][1], key[1][2], key[0], key[1][3])
            #ui.add(str_re[0][1:-1], str_re[1][1:-1], str_re[2][1:-1], key, )



class Ui_tcplistDialog(object):
    global co
    co = 0

    def setupUi(self, tcplistDialog):
        tcplistDialog.setObjectName("tcplistDialog")
        tcplistDialog.setWindowModality(QtCore.Qt.NonModal)
        tcplistDialog.resize(580, 534)
        tcplistDialog.setMaximumSize(580, 534)
        tcplistDialog.setMinimumSize(580, 534)
        tcplistDialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.verticalLayoutWidget = QtWidgets.QWidget(tcplistDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 550, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.verticalHeader().setHidden(True)

        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 75)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(tcplistDialog)
        self.pushButton.setGeometry(QtCore.QRect(485, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.closewindows())
        #self.selectButton = QtWidgets.QPushButton(tcplistDialog)
        #self.selectButton.setGeometry(QtCore.QRect(400, 500, 75, 23))
        #self.selectButton.setObjectName("selectButton")
        #self.selectButton.clicked.connect(lambda: self.closewindows())
        #self.retranslateUi(tcplistDialog)
        QtCore.QMetaObject.connectSlotsByName(tcplistDialog)

    def retranslateUi(self, tcplistDialog):
        _translate = QtCore.QCoreApplication.translate
        tcplistDialog.setWindowTitle(_translate("tcplistDialog", "tcp服务器"))
        self.label.setText(_translate("tcplistDialog", "连接列表"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tcplistDialog", "机器号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tcplistDialog", "工作模式"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tcplistDialog", "计数"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("tcplistDialog", "ip地址"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("tcplistDialog", "更新时间"))
        self.pushButton.setText(_translate("tcplistDialog", "关闭服务器"))
        #self.selectButton.setText(_translate("tcplistDialog", "查询"))
    def add(self, id, mode, count, ip, time):
        global co

        row = self.tableWidget.rowCount()
        if co >= row:
            self.tableWidget.insertRow(row)

        item_id = QTableWidgetItem(str(id))
        item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

        item_mode = QTableWidgetItem(mode)
        item_mode.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

        item_count = QTableWidgetItem(count)
        item_count.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

        item_ip = QTableWidgetItem(ip)
        item_ip.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

        item_time = QTableWidgetItem(time)
        item_time.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

        self.tableWidget.setItem(co, 0, item_id)
        self.tableWidget.setItem(co, 1, item_mode)
        self.tableWidget.setItem(co, 2, item_count)
        self.tableWidget.setItem(co, 3, item_ip)
        self.tableWidget.setItem(co, 4, item_time)
        co += 1

    def clearall(self):
        global co
        self.tableWidget.clearContents()
        co = 0

    def closewindows(self):
        sys.exit(0)
