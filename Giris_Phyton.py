from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from panel import *
from Gecmis import *
from PyQt5.QtWidgets import *
from Giris import *

#arayüz
#-
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_Giris()
ui.setupUi(pencere)
pencere.show()

class Giris(QWidget):
    def __init__(self):
        super().__init__()
        self.formGiris = Ui_Giris()
        self.Anasayfa = Anasayfasayfa()
        self.Gecmis = Gecmissayfa()
        self.formGiris.btn200.clicked = self.Anasayfa_ac
    def Anasayfa_ac(self):
        self.panel.show()




#database
import sqlite3

baglanti = sqlite3.connect("StokTakip.db")
islem = baglanti.cursor()
baglanti.commit()

  



sys.exit(uygulama.exec_())