# Form implementation generated from reading ui file 'ui files\thongke.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_thongKeWindow(object):
    def setupUi(self, thongKeWindow):
        thongKeWindow.setObjectName("thongKeWindow")
        thongKeWindow.resize(909, 722)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/nguye/OneDrive/Hình ảnh/donga.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        thongKeWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=thongKeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 441, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label.setObjectName("label")
        self.soSach = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soSach.setGeometry(QtCore.QRect(80, 30, 121, 22))
        self.soSach.setReadOnly(True)
        self.soSach.setObjectName("soSach")
        self.soBanDoc = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soBanDoc.setGeometry(QtCore.QRect(80, 70, 121, 22))
        self.soBanDoc.setReadOnly(True)
        self.soBanDoc.setObjectName("soBanDoc")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        self.soViPham = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soViPham.setGeometry(QtCore.QRect(80, 110, 121, 22))
        self.soViPham.setReadOnly(True)
        self.soViPham.setObjectName("soViPham")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 55, 16))
        self.label_3.setObjectName("label_3")
        self.soMuonTra = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soMuonTra.setGeometry(QtCore.QRect(300, 110, 121, 22))
        self.soMuonTra.setReadOnly(True)
        self.soMuonTra.setObjectName("soMuonTra")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(230, 30, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(230, 110, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(230, 70, 55, 16))
        self.label_6.setObjectName("label_6")
        self.soTheLoai = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soTheLoai.setGeometry(QtCore.QRect(300, 70, 121, 22))
        self.soTheLoai.setReadOnly(True)
        self.soTheLoai.setObjectName("soTheLoai")
        self.soTacGia = QtWidgets.QLineEdit(parent=self.groupBox)
        self.soTacGia.setGeometry(QtCore.QRect(300, 30, 121, 22))
        self.soTacGia.setReadOnly(True)
        self.soTacGia.setObjectName("soTacGia")
        self.sachChuaTra_QGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.sachChuaTra_QGroupBox.setGeometry(QtCore.QRect(10, 430, 891, 281))
        self.sachChuaTra_QGroupBox.setObjectName("sachChuaTra_QGroupBox")
        self.sachChuaTra_tableWidget = QtWidgets.QTableWidget(parent=self.sachChuaTra_QGroupBox)
        self.sachChuaTra_tableWidget.setGeometry(QtCore.QRect(10, 30, 871, 241))
        self.sachChuaTra_tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.sachChuaTra_tableWidget.setShowGrid(False)
        self.sachChuaTra_tableWidget.setObjectName("sachChuaTra_tableWidget")
        self.sachChuaTra_tableWidget.setColumnCount(9)
        self.sachChuaTra_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.sachChuaTra_tableWidget.setHorizontalHeaderItem(8, item)
        self.sachChuaTra_tableWidget.horizontalHeader().setDefaultSectionSize(88)
        self.sachChuaTra_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.sachChuaTra_tableWidget.verticalHeader().setVisible(False)
        self.viPham_QGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.viPham_QGroupBox.setGeometry(QtCore.QRect(10, 170, 891, 251))
        self.viPham_QGroupBox.setObjectName("viPham_QGroupBox")
        self.viPham_tableWidget = QtWidgets.QTableWidget(parent=self.viPham_QGroupBox)
        self.viPham_tableWidget.setGeometry(QtCore.QRect(10, 30, 871, 211))
        self.viPham_tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.viPham_tableWidget.setShowGrid(False)
        self.viPham_tableWidget.setObjectName("viPham_tableWidget")
        self.viPham_tableWidget.setColumnCount(7)
        self.viPham_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.viPham_tableWidget.setHorizontalHeaderItem(6, item)
        self.viPham_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.viPham_tableWidget.verticalHeader().setVisible(False)
        self.soLuongRow_viPham = QtWidgets.QLineEdit(parent=self.viPham_QGroupBox)
        self.soLuongRow_viPham.setGeometry(QtCore.QRect(160, 0, 151, 22))
        self.soLuongRow_viPham.setStyleSheet("")
        self.soLuongRow_viPham.setText("")
        self.soLuongRow_viPham.setReadOnly(True)
        self.soLuongRow_viPham.setObjectName("soLuongRow_viPham")
        self.traSach_groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.traSach_groupBox.setGeometry(QtCore.QRect(470, 10, 431, 71))
        self.traSach_groupBox.setObjectName("traSach_groupBox")
        self.traSach_pushButton = QtWidgets.QPushButton(parent=self.traSach_groupBox)
        self.traSach_pushButton.setGeometry(QtCore.QRect(320, 30, 93, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui files\\../icon/backspace_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.traSach_pushButton.setIcon(icon1)
        self.traSach_pushButton.setObjectName("traSach_pushButton")
        self.ngayTra_dateEdit = QtWidgets.QDateEdit(parent=self.traSach_groupBox)
        self.ngayTra_dateEdit.setGeometry(QtCore.QRect(10, 30, 301, 31))
        self.ngayTra_dateEdit.setObjectName("ngayTra_dateEdit")
        self.soLuongRow_sachChuaTra = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.soLuongRow_sachChuaTra.setGeometry(QtCore.QRect(170, 430, 151, 22))
        self.soLuongRow_sachChuaTra.setStyleSheet("")
        self.soLuongRow_sachChuaTra.setText("")
        self.soLuongRow_sachChuaTra.setReadOnly(True)
        self.soLuongRow_sachChuaTra.setObjectName("soLuongRow_sachChuaTra")
        self.nopPhat_GroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.nopPhat_GroupBox.setGeometry(QtCore.QRect(470, 90, 431, 71))
        self.nopPhat_GroupBox.setObjectName("nopPhat_GroupBox")
        self.tienPhat_lineEdit = QtWidgets.QLineEdit(parent=self.nopPhat_GroupBox)
        self.tienPhat_lineEdit.setGeometry(QtCore.QRect(10, 30, 301, 31))
        self.tienPhat_lineEdit.setReadOnly(False)
        self.tienPhat_lineEdit.setObjectName("tienPhat_lineEdit")
        self.nopPhat_pushButton = QtWidgets.QPushButton(parent=self.nopPhat_GroupBox)
        self.nopPhat_pushButton.setGeometry(QtCore.QRect(320, 30, 93, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui files\\../icon/add_circle_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.nopPhat_pushButton.setIcon(icon2)
        self.nopPhat_pushButton.setObjectName("nopPhat_pushButton")
        self.maViPham = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.maViPham.setGeometry(QtCore.QRect(540, 90, 111, 22))
        self.maViPham.setStyleSheet("")
        self.maViPham.setText("")
        self.maViPham.setReadOnly(True)
        self.maViPham.setObjectName("maViPham")
        self.maSachMuon = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.maSachMuon.setGeometry(QtCore.QRect(540, 10, 111, 22))
        self.maSachMuon.setStyleSheet("")
        self.maSachMuon.setText("")
        self.maSachMuon.setReadOnly(True)
        self.maSachMuon.setObjectName("maSachMuon")
        self.chonTheMuonBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chonTheMuonBtn.setGeometry(QtCore.QRect(330, 430, 93, 21))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui files\\../icon/check_box_24dp_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.chonTheMuonBtn.setIcon(icon3)
        self.chonTheMuonBtn.setObjectName("chonTheMuonBtn")
        self.chonViPhamBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chonViPhamBtn.setGeometry(QtCore.QRect(330, 170, 93, 21))
        self.chonViPhamBtn.setIcon(icon3)
        self.chonViPhamBtn.setObjectName("chonViPhamBtn")
        self.viPham_QGroupBox.raise_()
        self.groupBox.raise_()
        self.sachChuaTra_QGroupBox.raise_()
        self.traSach_groupBox.raise_()
        self.soLuongRow_sachChuaTra.raise_()
        self.nopPhat_GroupBox.raise_()
        self.maViPham.raise_()
        self.maSachMuon.raise_()
        self.chonTheMuonBtn.raise_()
        self.chonViPhamBtn.raise_()
        thongKeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=thongKeWindow)
        self.statusbar.setObjectName("statusbar")
        thongKeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(thongKeWindow)
        QtCore.QMetaObject.connectSlotsByName(thongKeWindow)

    def retranslateUi(self, thongKeWindow):
        _translate = QtCore.QCoreApplication.translate
        thongKeWindow.setWindowTitle(_translate("thongKeWindow", "Thống kê"))
        self.groupBox.setTitle(_translate("thongKeWindow", "Số lượng"))
        self.label.setText(_translate("thongKeWindow", "Sách"))
        self.label_2.setText(_translate("thongKeWindow", "Bạn đọc"))
        self.label_3.setText(_translate("thongKeWindow", "Vi phạm"))
        self.label_4.setText(_translate("thongKeWindow", "Tác giả"))
        self.label_5.setText(_translate("thongKeWindow", "Lần mượn"))
        self.label_6.setText(_translate("thongKeWindow", "Thể loại"))
        self.sachChuaTra_QGroupBox.setTitle(_translate("thongKeWindow", "Lượt mượn chưa trả hết"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("thongKeWindow", "Mã"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("thongKeWindow", "Bạn đọc"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("thongKeWindow", "Thủ thư"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("thongKeWindow", "Ngày mượn"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("thongKeWindow", "Ngày trả"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("thongKeWindow", "Sách mượn"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("thongKeWindow", "Tình trạng"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("thongKeWindow", "Ngày cập nhật"))
        item = self.sachChuaTra_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("thongKeWindow", "Ngày thêm"))
        self.viPham_QGroupBox.setTitle(_translate("thongKeWindow", "Vi phạm chưa nộp phạt"))
        item = self.viPham_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("thongKeWindow", "Mã vi phạm"))
        item = self.viPham_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("thongKeWindow", "Bạn đọc"))
        item = self.viPham_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("thongKeWindow", "Thủ thư"))
        item = self.viPham_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("thongKeWindow", "Nội dung"))
        item = self.viPham_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("thongKeWindow", "Tiền phạt"))
        item = self.viPham_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("thongKeWindow", "Tình trạng"))
        item = self.viPham_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("thongKeWindow", "Ngày thêm"))
        self.soLuongRow_viPham.setPlaceholderText(_translate("thongKeWindow", "Số lượng: 0"))
        self.traSach_groupBox.setTitle(_translate("thongKeWindow", "Trả sách"))
        self.traSach_pushButton.setText(_translate("thongKeWindow", "Trả sách"))
        self.ngayTra_dateEdit.setDisplayFormat(_translate("thongKeWindow", "yyyy-MM-dd"))
        self.soLuongRow_sachChuaTra.setPlaceholderText(_translate("thongKeWindow", "Số lượng: 0"))
        self.nopPhat_GroupBox.setTitle(_translate("thongKeWindow", "Nộp phạt"))
        self.tienPhat_lineEdit.setPlaceholderText(_translate("thongKeWindow", "1000"))
        self.nopPhat_pushButton.setText(_translate("thongKeWindow", "Nộp phạt"))
        self.maViPham.setPlaceholderText(_translate("thongKeWindow", "Mã: #00"))
        self.maSachMuon.setPlaceholderText(_translate("thongKeWindow", "Mã: #00"))
        self.chonTheMuonBtn.setText(_translate("thongKeWindow", "Chọn"))
        self.chonViPhamBtn.setText(_translate("thongKeWindow", "Chọn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thongKeWindow = QtWidgets.QMainWindow()
    ui = Ui_thongKeWindow()
    ui.setupUi(thongKeWindow)
    thongKeWindow.show()
    sys.exit(app.exec())
