# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_cardMain(object):
    def setupUi(self, cardMain):
        if not cardMain.objectName():
            cardMain.setObjectName(u"cardMain")
        cardMain.resize(800, 286)
        cardMain.setMaximumSize(QSize(800, 286))
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        cardMain.setFont(font)
        self.mainWidget = QWidget(cardMain)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setFont(font)
        self.mainWidget.setStyleSheet(u"QWidget {\n"
"	background-color: #B5838D\n"
"}")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.mainWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMaximumSize(QSize(16777215, 100))
        self.headerFrame.setFont(font)
        self.headerFrame.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}\n"
"QFrame {\n"
"	background-color: #E5989B;\n"
"}")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.headerLbl = QLabel(self.headerFrame)
        self.headerLbl.setObjectName(u"headerLbl")
        sizePolicy.setHeightForWidth(self.headerLbl.sizePolicy().hasHeightForWidth())
        self.headerLbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Cascadia Code"])
        font1.setPointSize(28)
        self.headerLbl.setFont(font1)
        self.headerLbl.setScaledContents(False)
        self.headerLbl.setAlignment(Qt.AlignCenter)
        self.headerLbl.setWordWrap(False)

        self.horizontalLayout.addWidget(self.headerLbl)

        self.statusFrame = QFrame(self.headerFrame)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #6D6875;\n"
"	border-radius: 12px;\n"
"}")
        self.statusFrame.setFrameShape(QFrame.NoFrame)
        self.statusFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.statusFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cardBrandLbl = QLabel(self.statusFrame)
        self.cardBrandLbl.setObjectName(u"cardBrandLbl")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(12)
        self.cardBrandLbl.setFont(font2)

        self.verticalLayout_2.addWidget(self.cardBrandLbl)

        self.cardStatusLbl = QLabel(self.statusFrame)
        self.cardStatusLbl.setObjectName(u"cardStatusLbl")
        self.cardStatusLbl.setFont(font2)

        self.verticalLayout_2.addWidget(self.cardStatusLbl)


        self.horizontalLayout.addWidget(self.statusFrame)


        self.verticalLayout.addWidget(self.headerFrame)

        self.inputFrame = QFrame(self.mainWidget)
        self.inputFrame.setObjectName(u"inputFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputFrame.sizePolicy().hasHeightForWidth())
        self.inputFrame.setSizePolicy(sizePolicy1)
        self.inputFrame.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}\n"
"QLineEdit {\n"
"	background-color: #FFCDB2;\n"
"	border-radius: 12px;\n"
"	color: #6D6875;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: #FFB4A2;\n"
"}\n"
"QPushButton {\n"
"	background-color: #FFCDB2;\n"
"	border-radius: 12px;\n"
"	color: #6D6875;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #FFB4A2\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6D6875;\n"
"	color: white;\n"
"}")
        self.inputFrame.setFrameShape(QFrame.NoFrame)
        self.inputFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.inputFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cardInputLineEdit = QLineEdit(self.inputFrame)
        self.cardInputLineEdit.setObjectName(u"cardInputLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cardInputLineEdit.sizePolicy().hasHeightForWidth())
        self.cardInputLineEdit.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Cascadia Code"])
        font3.setPointSize(18)
        self.cardInputLineEdit.setFont(font3)
        self.cardInputLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cardInputLineEdit)

        self.checkBtn = QPushButton(self.inputFrame)
        self.checkBtn.setObjectName(u"checkBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBtn.sizePolicy().hasHeightForWidth())
        self.checkBtn.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Cascadia Code"])
        font4.setPointSize(16)
        self.checkBtn.setFont(font4)

        self.verticalLayout_3.addWidget(self.checkBtn)

        self.disclaimerLbl = QLabel(self.inputFrame)
        self.disclaimerLbl.setObjectName(u"disclaimerLbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.disclaimerLbl.sizePolicy().hasHeightForWidth())
        self.disclaimerLbl.setSizePolicy(sizePolicy4)
        self.disclaimerLbl.setFont(font2)
        self.disclaimerLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.disclaimerLbl.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.disclaimerLbl)


        self.verticalLayout.addWidget(self.inputFrame)

        cardMain.setCentralWidget(self.mainWidget)

        self.retranslateUi(cardMain)

        QMetaObject.connectSlotsByName(cardMain)
    # setupUi

    def retranslateUi(self, cardMain):
        cardMain.setWindowTitle(QCoreApplication.translate("cardMain", u"Card Check", None))
        self.headerLbl.setText(QCoreApplication.translate("cardMain", u"[ card check ]", None))
        self.cardBrandLbl.setText(QCoreApplication.translate("cardMain", u"[ card brand ] : ///", None))
        self.cardStatusLbl.setText(QCoreApplication.translate("cardMain", u"[ card status ] : ///", None))
        self.checkBtn.setText(QCoreApplication.translate("cardMain", u"[ check ]", None))
        self.disclaimerLbl.setText(QCoreApplication.translate("cardMain", u"For educational purposes only, I don't condone cracking or any illegal-related stuffs and this app doesn't use any network/data.", None))
    # retranslateUi

