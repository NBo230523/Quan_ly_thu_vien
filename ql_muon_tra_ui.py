# Form implementation generated from reading ui file 'ui files\ql_muon_tra.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ql_muonTraWindow(object):
    def setupUi(self, ql_muonTraWindow):
        ql_muonTraWindow.setObjectName("ql_muonTraWindow")
        ql_muonTraWindow.resize(841, 584)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/nguye/OneDrive/Hình ảnh/donga.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ql_muonTraWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=ql_muonTraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(220, 100, 51, 16))
        self.label_4.setObjectName("label_4")
        self.ngayTra_dateEdit = QtWidgets.QDateEdit(parent=self.groupBox)
        self.ngayTra_dateEdit.setGeometry(QtCore.QRect(290, 100, 81, 20))
        self.ngayTra_dateEdit.setObjectName("ngayTra_dateEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 67, 61, 16))
        self.label_2.setObjectName("label_2")
        self.maAdmin_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.maAdmin_comboBox.setGeometry(QtCore.QRect(80, 67, 121, 20))
        self.maAdmin_comboBox.setObjectName("maAdmin_comboBox")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(220, 67, 71, 16))
        self.label_5.setObjectName("label_5")
        self.ngayMuon_dateEdit = QtWidgets.QDateEdit(parent=self.groupBox)
        self.ngayMuon_dateEdit.setGeometry(QtCore.QRect(290, 67, 81, 20))
        self.ngayMuon_dateEdit.setObjectName("ngayMuon_dateEdit")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 98, 61, 16))
        self.label_6.setObjectName("label_6")
        self.tinhTrang_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.tinhTrang_comboBox.setGeometry(QtCore.QRect(80, 98, 121, 20))
        self.tinhTrang_comboBox.setObjectName("tinhTrang_comboBox")
        self.tinhTrang_comboBox.addItem("")
        self.tinhTrang_comboBox.addItem("")
        self.tinhTrang_comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(9, 30, 65, 20))
        self.label_3.setObjectName("label_3")
        self.timBanDoc_lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.timBanDoc_lineEdit.setGeometry(QtCore.QRect(80, 30, 271, 20))
        self.timBanDoc_lineEdit.setObjectName("timBanDoc_lineEdit")
        self.maBanDoc_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.maBanDoc_comboBox.setGeometry(QtCore.QRect(80, 30, 291, 20))
        self.maBanDoc_comboBox.setObjectName("maBanDoc_comboBox")
        self.maRow = QtWidgets.QLineEdit(parent=self.groupBox)
        self.maRow.setGeometry(QtCore.QRect(130, 0, 81, 22))
        self.maRow.setStyleSheet("")
        self.maRow.setText("")
        self.maRow.setReadOnly(True)
        self.maRow.setObjectName("maRow")
        self.soLuongRow = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soLuongRow.setGeometry(QtCore.QRect(220, 0, 151, 22))
        self.soLuongRow.setStyleSheet("")
        self.soLuongRow.setText("")
        self.soLuongRow.setReadOnly(True)
        self.soLuongRow.setPlaceholderText("")
        self.soLuongRow.setObjectName("soLuongRow")
        self.label_4.raise_()
        self.ngayTra_dateEdit.raise_()
        self.label_2.raise_()
        self.maAdmin_comboBox.raise_()
        self.label_5.raise_()
        self.ngayMuon_dateEdit.raise_()
        self.label_6.raise_()
        self.tinhTrang_comboBox.raise_()
        self.label_3.raise_()
        self.maBanDoc_comboBox.raise_()
        self.timBanDoc_lineEdit.raise_()
        self.maRow.raise_()
        self.soLuongRow.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 821, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.them_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui files\\icon/add_circle_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.them_pushButton.setIcon(icon1)
        self.them_pushButton.setObjectName("them_pushButton")
        self.gridLayout_2.addWidget(self.them_pushButton, 0, 0, 1, 1)
        self.capNhat_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui files\\icon/sync_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.capNhat_pushButton.setIcon(icon2)
        self.capNhat_pushButton.setObjectName("capNhat_pushButton")
        self.gridLayout_2.addWidget(self.capNhat_pushButton, 0, 1, 1, 1)
        self.chon_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui files\\icon/check_box_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.chon_pushButton.setIcon(icon3)
        self.chon_pushButton.setObjectName("chon_pushButton")
        self.gridLayout_2.addWidget(self.chon_pushButton, 0, 2, 1, 1)
        self.timKiem_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui files\\icon/search_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.timKiem_pushButton.setIcon(icon4)
        self.timKiem_pushButton.setObjectName("timKiem_pushButton")
        self.gridLayout_2.addWidget(self.timKiem_pushButton, 0, 3, 1, 1)
        self.lamTrong_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui files\\icon/backspace_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.lamTrong_pushButton.setIcon(icon5)
        self.lamTrong_pushButton.setObjectName("lamTrong_pushButton")
        self.gridLayout_2.addWidget(self.lamTrong_pushButton, 0, 4, 1, 1)
        self.xoa_pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui files\\icon/delete_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.xoa_pushButton.setIcon(icon6)
        self.xoa_pushButton.setObjectName("xoa_pushButton")
        self.gridLayout_2.addWidget(self.xoa_pushButton, 0, 5, 1, 1)
        self.result_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.result_table.setGeometry(QtCore.QRect(10, 250, 821, 291))
        self.result_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.result_table.setShowGrid(False)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(9)
        self.result_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(8, item)
        self.result_table.horizontalHeader().setDefaultSectionSize(88)
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.verticalHeader().setVisible(False)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 10, 431, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listSachMuon_listWidget = QtWidgets.QListWidget(parent=self.groupBox_3)
        self.listSachMuon_listWidget.setGeometry(QtCore.QRect(10, 50, 281, 81))
        self.listSachMuon_listWidget.setObjectName("listSachMuon_listWidget")
        self.timKiemSach_lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.timKiemSach_lineEdit.setGeometry(QtCore.QRect(10, 20, 261, 21))
        self.timKiemSach_lineEdit.setObjectName("timKiemSach_lineEdit")
        self.them_sach_pushButton = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.them_sach_pushButton.setGeometry(QtCore.QRect(300, 20, 121, 31))
        self.them_sach_pushButton.setIcon(icon1)
        self.them_sach_pushButton.setObjectName("them_sach_pushButton")
        self.tra_sach_pushButton = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.tra_sach_pushButton.setGeometry(QtCore.QRect(300, 60, 121, 31))
        self.tra_sach_pushButton.setIcon(icon5)
        self.tra_sach_pushButton.setObjectName("tra_sach_pushButton")
        self.maSach_comboBox = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.maSach_comboBox.setGeometry(QtCore.QRect(10, 20, 281, 21))
        self.maSach_comboBox.setObjectName("maSach_comboBox")
        self.xoa_sach_pushButton = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.xoa_sach_pushButton.setGeometry(QtCore.QRect(300, 100, 121, 31))
        self.xoa_sach_pushButton.setIcon(icon6)
        self.xoa_sach_pushButton.setObjectName("xoa_sach_pushButton")
        self.listSachMuon_listWidget.raise_()
        self.them_sach_pushButton.raise_()
        self.tra_sach_pushButton.raise_()
        self.maSach_comboBox.raise_()
        self.timKiemSach_lineEdit.raise_()
        self.xoa_sach_pushButton.raise_()
        ql_muonTraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ql_muonTraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 21))
        self.menubar.setObjectName("menubar")
        ql_muonTraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ql_muonTraWindow)
        self.statusbar.setObjectName("statusbar")
        ql_muonTraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ql_muonTraWindow)
        QtCore.QMetaObject.connectSlotsByName(ql_muonTraWindow)

    def retranslateUi(self, ql_muonTraWindow):
        _translate = QtCore.QCoreApplication.translate
        ql_muonTraWindow.setWindowTitle(_translate("ql_muonTraWindow", "Lịch sử mượn trả"))
        self.groupBox.setTitle(_translate("ql_muonTraWindow", "THÔNG TIN MƯỢN"))
        self.label_4.setText(_translate("ql_muonTraWindow", "Ngày trả"))
        self.ngayTra_dateEdit.setDisplayFormat(_translate("ql_muonTraWindow", "yyyy-MM-dd"))
        self.label_2.setText(_translate("ql_muonTraWindow", "Thủ thư"))
        self.label_5.setText(_translate("ql_muonTraWindow", "Ngày mượn"))
        self.ngayMuon_dateEdit.setDisplayFormat(_translate("ql_muonTraWindow", "yyyy-MM-dd"))
        self.label_6.setText(_translate("ql_muonTraWindow", "Tình trạng"))
        self.tinhTrang_comboBox.setItemText(0, _translate("ql_muonTraWindow", "Chưa trả"))
        self.tinhTrang_comboBox.setItemText(1, _translate("ql_muonTraWindow", "Đã trả"))
        self.tinhTrang_comboBox.setItemText(2, _translate("ql_muonTraWindow", "Quá hạn"))
        self.label_3.setText(_translate("ql_muonTraWindow", "Bạn đọc"))
        self.timBanDoc_lineEdit.setPlaceholderText(_translate("ql_muonTraWindow", "Tìm kiếm bạn đọc"))
        self.maRow.setPlaceholderText(_translate("ql_muonTraWindow", "Mã: #00"))
        self.groupBox_2.setTitle(_translate("ql_muonTraWindow", "THAO TÁC"))
        self.them_pushButton.setText(_translate("ql_muonTraWindow", "Thêm"))
        self.capNhat_pushButton.setText(_translate("ql_muonTraWindow", "Cập nhật"))
        self.chon_pushButton.setText(_translate("ql_muonTraWindow", "Chọn"))
        self.timKiem_pushButton.setText(_translate("ql_muonTraWindow", "Tìm kiếm"))
        self.lamTrong_pushButton.setText(_translate("ql_muonTraWindow", "Làm trống"))
        self.xoa_pushButton.setText(_translate("ql_muonTraWindow", "Xóa"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("ql_muonTraWindow", "Mã"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("ql_muonTraWindow", "Bạn đọc"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("ql_muonTraWindow", "Thủ thư"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("ql_muonTraWindow", "Ngày mượn"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("ql_muonTraWindow", "Ngày trả"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("ql_muonTraWindow", "Sách mượn"))
        item = self.result_table.horizontalHeaderItem(6)
        item.setText(_translate("ql_muonTraWindow", "Tình trạng"))
        item = self.result_table.horizontalHeaderItem(7)
        item.setText(_translate("ql_muonTraWindow", "Ngày cập nhật"))
        item = self.result_table.horizontalHeaderItem(8)
        item.setText(_translate("ql_muonTraWindow", "Ngày thêm"))
        self.groupBox_3.setTitle(_translate("ql_muonTraWindow", "CHI TIẾT MƯỢN SÁCH"))
        self.timKiemSach_lineEdit.setPlaceholderText(_translate("ql_muonTraWindow", "Tìm kiếm sách"))
        self.them_sach_pushButton.setText(_translate("ql_muonTraWindow", "Mượn"))
        self.tra_sach_pushButton.setText(_translate("ql_muonTraWindow", "Trả"))
        self.xoa_sach_pushButton.setText(_translate("ql_muonTraWindow", "Xóa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ql_muonTraWindow = QtWidgets.QMainWindow()
    ui = Ui_ql_muonTraWindow()
    ui.setupUi(ql_muonTraWindow)
    ql_muonTraWindow.show()
    sys.exit(app.exec())
