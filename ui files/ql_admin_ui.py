# Form implementation generated from reading ui file 'c:\Users\QUAN\Documents\btl python\PyQT6\ql_sach\ui files\ql_admin.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ql_adminWindow(object):
    def setupUi(self, ql_adminWindow):
        ql_adminWindow.setObjectName("ql_adminWindow")
        ql_adminWindow.resize(792, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/book_2_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ql_adminWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=ql_adminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 761, 111))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.username_lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.gridLayout_2.addWidget(self.username_lineEdit, 0, 1, 1, 1)
        self.role_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.role_comboBox.setObjectName("role_comboBox")
        self.role_comboBox.addItem("")
        self.role_comboBox.addItem("")
        self.gridLayout_2.addWidget(self.role_comboBox, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.matkhau_lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.matkhau_lineEdit.setObjectName("matkhau_lineEdit")
        self.gridLayout_2.addWidget(self.matkhau_lineEdit, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 761, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.them_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/add_circle_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.them_pushButton.setIcon(icon1)
        self.them_pushButton.setObjectName("them_pushButton")
        self.gridLayout.addWidget(self.them_pushButton, 0, 0, 1, 1)
        self.capNhat_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/sync_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.capNhat_pushButton.setIcon(icon2)
        self.capNhat_pushButton.setObjectName("capNhat_pushButton")
        self.gridLayout.addWidget(self.capNhat_pushButton, 0, 1, 1, 1)
        self.chon_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/check_box_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.chon_pushButton.setIcon(icon3)
        self.chon_pushButton.setObjectName("chon_pushButton")
        self.gridLayout.addWidget(self.chon_pushButton, 0, 2, 1, 1)
        self.timKiem_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/search_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.timKiem_pushButton.setIcon(icon4)
        self.timKiem_pushButton.setObjectName("timKiem_pushButton")
        self.gridLayout.addWidget(self.timKiem_pushButton, 0, 3, 1, 1)
        self.clear_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/backspace_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clear_pushButton.setIcon(icon5)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.gridLayout.addWidget(self.clear_pushButton, 0, 4, 1, 1)
        self.xoa_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\QUAN\\Documents\\btl python\\PyQT6\\ql_sach\\ui files\\icon/delete_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.xoa_pushButton.setIcon(icon6)
        self.xoa_pushButton.setObjectName("xoa_pushButton")
        self.gridLayout.addWidget(self.xoa_pushButton, 0, 5, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 761, 251))
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setShowGrid(False)
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
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.maRow = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.maRow.setGeometry(QtCore.QRect(140, 10, 81, 22))
        self.maRow.setStyleSheet("")
        self.maRow.setText("")
        self.maRow.setReadOnly(True)
        self.maRow.setObjectName("maRow")
        self.soLuongRow = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.soLuongRow.setGeometry(QtCore.QRect(230, 10, 151, 22))
        self.soLuongRow.setStyleSheet("")
        self.soLuongRow.setText("")
        self.soLuongRow.setReadOnly(True)
        self.soLuongRow.setObjectName("soLuongRow")
        ql_adminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ql_adminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 26))
        self.menubar.setObjectName("menubar")
        ql_adminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ql_adminWindow)
        self.statusbar.setObjectName("statusbar")
        ql_adminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ql_adminWindow)
        QtCore.QMetaObject.connectSlotsByName(ql_adminWindow)

    def retranslateUi(self, ql_adminWindow):
        _translate = QtCore.QCoreApplication.translate
        ql_adminWindow.setWindowTitle(_translate("ql_adminWindow", "Quản lý admin"))
        self.groupBox.setTitle(_translate("ql_adminWindow", "THÔNG TIN ADMIN"))
        self.label.setText(_translate("ql_adminWindow", "Username"))
        self.role_comboBox.setItemText(0, _translate("ql_adminWindow", "QUAN_TRI"))
        self.role_comboBox.setItemText(1, _translate("ql_adminWindow", "THU_THU"))
        self.label_4.setText(_translate("ql_adminWindow", "Password"))
        self.label_2.setText(_translate("ql_adminWindow", "Role"))
        self.groupBox_2.setTitle(_translate("ql_adminWindow", "THAO TÁC"))
        self.them_pushButton.setText(_translate("ql_adminWindow", "Thêm"))
        self.capNhat_pushButton.setText(_translate("ql_adminWindow", "Cập nhật"))
        self.chon_pushButton.setText(_translate("ql_adminWindow", "Chọn"))
        self.timKiem_pushButton.setText(_translate("ql_adminWindow", "Tìm kiếm"))
        self.clear_pushButton.setText(_translate("ql_adminWindow", "Làm trống"))
        self.xoa_pushButton.setText(_translate("ql_adminWindow", "Xóa"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ql_adminWindow", "Mã admin"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ql_adminWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ql_adminWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ql_adminWindow", "Role"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ql_adminWindow", "Ngày thêm"))