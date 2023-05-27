from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
from ui_design_ui import Ui_cardMain

class mainApp(QMainWindow, Ui_cardMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initBtns()

    def checkCard(self):
        cardNum = self.cardInputLineEdit.text()
        
        nDigits = len(cardNum)
        nSum = 0
        isSecond = False

        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNum[i]) - ord('0')
        
            if (isSecond == True):
                d = d * 2
    
            # We add two digits to handle
            # cases that make two digits after
            # doubling
            nSum += d // 10
            nSum += d % 10
    
            isSecond = not isSecond
        
        if (nSum % 10 == 0):
            self.cardStatusLbl.setText(f"[ card status ] : VALID")
            self.checkCardType()
        else:
            self.cardStatusLbl.setText(f"[ card status ] : INVALID")

    def checkCardType(self):

        cardNum = self.cardInputLineEdit.text()

        if len(cardNum) == 15 and cardNum[:2] in ('34', '37'):
            self.cardBrandLbl.setText("[ card brand ] : AMERICAN EXPRESS")
        elif len(cardNum) == 16:
            if cardNum[:2] in ('51', '52', '53', '54', '55'):
                self.cardBrandLbl.setText("[ card brand ] : MASTERCARD")
            elif (cardNum[:2] in '65' or cardNum[:4] in '6011'):
                self.cardBrandLbl.setText("[ card brand ] : DISCOVER")
            elif cardNum[:1] in '4':
                self.cardBrandLbl.setText("[ card brand ] : VISA")
        elif (len(cardNum) == 13 and (cardNum[:1] in '4')):
            self.cardBrandLbl.setText("[ card brand ] : VISA")
    
    def initBtns(self):
        self.checkBtn.clicked.connect(self.checkCard)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainApp()
    win.show()

    app.exec()