from ast import Index
import enum
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from Gecmis import Ui_Gecmis
from panel import *



#class Anasayfa(QWidget) :
    #def __init__(self) :
        #super().__init__()
        #self.formMainWindow.lineEdit_ara.textChanged[str].connect(self.Ara)

#arayüz
#-
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_Anasayfa()
ui.setupUi(pencere)
pencere.show()

#database
import sqlite3

baglanti = sqlite3.connect("StokTakip.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("Create Table if Not Exists Kayit(Urun_Adi text,Urun_Alis_Fiyati text,Urun_Satis_Fiyati text,Adet text,Kdv text)")
baglanti.commit()

ui.tbl1.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV"))

def kayit_ekle():
    Urun_Adi = ui.lne1.text()
    Urun_Alis_Fiyati = ui.lne2.text()
    Urun_Satis_Fiyati = ui.lne3.text()
    Adet = ui.lne4.text()
    Kdv = ui.cmb1.currentText()



    try:
        ekle = "insert into Kayit(Urun_adi,urun_alis_fiyati,urun_satis_fiyati,adet,KDV) values (?,?,?,?,?)"
        islem.execute(ekle,(Urun_Adi,Urun_Alis_Fiyati,Urun_Satis_Fiyati,Adet,Kdv))
        baglanti.commit()
        ui.statusbar.showMessage ("Ürün eklendi !",5000)
        kayit_listele()
    except:
        ui.statusbar.showMessage("Ürün eklenemedi",5000)

def kayit_listele():
    ui.tbl1.clear()
    ui.tbl1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tbl1.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV"))
    ui.tbl1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from Kayit"
    islem.execute(sorgu)

    for indexSatir,kayitNumarasi in enumerate(islem):
        for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl1.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))

kayit_listele()
def Kdvye_gore_listele():
    listelenecek_Kdv = ui.cmb2.currentText()
    sorgu = "select * from Kayit where Kdv = ?"
    islem.execute(sorgu,(listelenecek_Kdv,))
    ui.tbl1.clear()
    ui.tbl1.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV"))
    for indexSatir,kayitNumarasi in enumerate(islem):
        for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl1.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))


def kayit_liste():
    ui.tbl1.clear()
    ui.tbl1.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV"))
    ui.tbl1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from Kayit"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tbl1.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere,"Silme İşlemini Onayla","Silmek İstediğinizden Emin Misiniz ?")
    QMessageBox.Yes |QMessageBox.No

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tbl1.selectedItems()
        silinecek_kayit = secilen_kayit [0].text()

        sorgu = "delete from Kayit where Urun_Adi = ?"

        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Silindi.",5000)
            kayit_listele()
        except:
            ui.statusbar.showMessage("Kayıt Silinemedi.",5000)
    
    else:
        ui.statusbar.showMessage("Silme işlemi İptal Edildi.",5000)


def yeni_pencere():
    uygulama = QApplication(sys.argv)
    pencere = QtWidgets.QMainWindow()
    ui = Ui_Gecmis()
    ui.setupUi(pencere)
    pencere.show()

     










#buton

ui.btn1.clicked.connect(kayit_ekle)
ui.btn3.clicked.connect(kayit_sil)
ui.btn2.clicked.connect(Kdvye_gore_listele)
ui.btn4.clicked.connect(kayit_liste)
ui.btn5.clicked.connect(yeni_pencere)




kayit_listele()


sys.exit(uygulama.exec_())

