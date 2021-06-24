from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShazamLikeApp(object):
    def setupUi(self, ShazamLikeApp):
        ShazamLikeApp.setObjectName("Shazam-like")
        ShazamLikeApp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ShazamLikeApp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 525))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_8)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.slider1 = QtWidgets.QSlider(self.frame_3)
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.verticalLayout.addWidget(self.slider1)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.play3 = QtWidgets.QPushButton(self.frame_3)
        self.play3.setObjectName("play3")
        self.gridLayout_3.addWidget(self.play3, 0, 2, 1, 1)
        self.mix = QtWidgets.QPushButton(self.frame_3)
        self.mix.setObjectName("mix")
        self.gridLayout_3.addWidget(self.mix, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ChooseFrame = QtWidgets.QFrame(self.frame_7)
        self.ChooseFrame.setMinimumSize(QtCore.QSize(60, 100))
        self.ChooseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ChooseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ChooseFrame.setObjectName("ChooseFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.ChooseFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MainFeatures = QtWidgets.QCheckBox(self.ChooseFrame)
        self.MainFeatures.setObjectName("MainFeatures")
        self.verticalLayout_3.addWidget(self.MainFeatures)
        self.Hash = QtWidgets.QCheckBox(self.ChooseFrame)
        self.Hash.setObjectName("Hash")
        self.verticalLayout_3.addWidget(self.Hash)
        self.Both = QtWidgets.QCheckBox(self.ChooseFrame)
        self.Both.setObjectName("Both")
        self.verticalLayout_3.addWidget(self.Both)
        self.compare = QtWidgets.QPushButton(self.ChooseFrame)
        self.compare.setObjectName("compare")
        self.verticalLayout_3.addWidget(self.compare)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.ChooseFrame)
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comparisontable = QtWidgets.QTableWidget(self.frame_6)
        self.comparisontable.setObjectName("comparisontable")
        self.comparisontable.setColumnCount(0)
        self.comparisontable.setRowCount(0)
        self.gridLayout_6.addWidget(self.comparisontable, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)
        ShazamLikeApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShazamLikeApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.Open = QtWidgets.QMenu(self.menubar)
        self.Open.setObjectName("Open")
        ShazamLikeApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShazamLikeApp)
        self.statusbar.setObjectName("statusbar")
        ShazamLikeApp.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(ShazamLikeApp)
        self.actionLoad.setObjectName("actionLoad")
        self.Open.addAction(self.actionLoad)
        self.menubar.addAction(self.Open.menuAction())

        self.retranslateUi(ShazamLikeApp)
        QtCore.QMetaObject.connectSlotsByName(ShazamLikeApp)

    def retranslateUi(self, ShazamLikeApp):
        _translate = QtCore.QCoreApplication.translate
        ShazamLikeApp.setWindowTitle(_translate("ShazamLikeApp", "ShazamLikeApp"))
        self.label.setText(_translate("ShazamLikeApp", "Music 1"))
        self.play3.setText(_translate("ShazamLikeApp", "Play "))
        self.mix.setText(_translate("ShazamLikeApp", "Mix"))
        self.MainFeatures.setText(_translate("ShazamLikeApp", "Main Features"))
        self.Hash.setText(_translate("ShazamLikeApp", "Hash"))
        self.Both.setText(_translate("ShazamLikeApp", "Both"))
        self.compare.setText(_translate("ShazamLikeApp", "Compare"))
        self.Open.setTitle(_translate("ShazamLikeApp", "Open"))
        self.actionLoad.setText(_translate("ShazamLikeApp", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShazamLikeApp = QtWidgets.QMainWindow()
    ui = Ui_ShazamLikeApp()
    ui.setupUi(ShazamLikeApp)
    ShazamLikeApp.show()
    sys.exit(app.exec_())
