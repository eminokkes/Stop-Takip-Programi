from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Gecmis import *
import xlsxwriter

#arayüz
#-
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_Gecmis()
ui.setupUi(pencere)
pencere.show()


#database
import sqlite3

baglanti = sqlite3.connect("StokTakip.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("Create Table if Not Exists Gecmis(Urun_Adi text,Urun_Alis_Fiyati text,Urun_Satis_Fiyati text,Adet text,Kdv text,Alinan_Urun_Sayisi text,Satilan_Urun_Sayisi text,Tarih text)")
baglanti.commit()


ui.tbl2.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV","Alınan Ürün Sayısı","Satılan Ürün Sayısı,Tarih"))
#ui.tbl2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) sığdırma komutu


def kayit_ekle():
    Urun_Adi = ui.lne100.text()
    Urun_Alis_Fiyati = ui.lne101.text()
    Urun_Satis_Fiyati = ui.lne102.text()
    Adet = ui.lne103.text()
    #Adet =(Alinan_Urun_Sayisi)-(Satilan_Urun_Sayisi)
    Kdv = ui.cmb100.currentText()
    Alinan_Urun_Sayisi = ui.lne104.text()
    Satilan_Urun_Sayisi = ui.lne105.text()
    Tarih = ui.cmb102.currentText()
    #Kalan_Urun_Sayisi = (Alinan_Urun_Sayisi-Satilan_Urun_Sayisi)
    #imlec=baglanti.cursor()
    #imlec.execute("update Gecmis set Kalan_Urun_Sayisi=(Alinan_Urun_Sayisi-Satilan_Urun_Sayisi)")
    #imlec.commit()




    try:
        ekle = "insert into Gecmis(Urun_adi,urun_alis_fiyati,urun_satis_fiyati,adet,KDV,Alinan_Urun_Sayisi,Satilan_Urun_Sayisi,Tarih,Kalan_Urun_Sayisi) values (?,?,?,?,?,?,?,?,?)"
        islem.execute(ekle,(Urun_Adi,Urun_Alis_Fiyati,Urun_Satis_Fiyati,Adet,Kdv,Alinan_Urun_Sayisi,Satilan_Urun_Sayisi,Tarih))
        baglanti.commit()
        ui.statusbar.showMessage ("Ürün eklendi !",5000)
        kayit_listele()
    except:
        ui.statusbar.showMessage("Ürün eklenemedi",5000)







def kayit_listele():
    ui.tbl2.clear()
    ui.tbl2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tbl2.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV","Alınan Ürün Sayısı","Satılan Ürün Sayısı","Tarih"))
    sorgu = "select * from Gecmis"
    islem.execute(sorgu)

    for indexSatir,kayitNumarasi in enumerate(islem):
        for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl2.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))


def kayit_liste():
    ui.tbl2.clear()
    ui.tbl2.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV","Alınan Ürün Sayısı","Satılan Ürün Sayısı","Tarih"))
    ui.tbl2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from Gecmis"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tbl2.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


def Tarihe_gore_listele():
    listelenecek_Tarih = ui.cmb101.currentText()
    sorgu = "select * from Gecmis where Tarih = ?"
    islem.execute(sorgu,(listelenecek_Tarih,))
    ui.tbl2.clear()
    ui.tbl2.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV","Alınan Ürün Sayısı","Satılan Ürün Sayısı","Tarih"))
    for indexSatir,kayitNumarasi in enumerate(islem):
        for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl2.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))

def Ara():
    Ara = ui.lne106.text()
    sorgu = "select * from Gecmis where Urun_adi = ?"

    #sorgu = ("SELECT * FROM Gecmis WHERE Urun_adi LIKE '%"+str()+"%'")
    #dbcur.execute("SELECT urun_adi FROM urunler WHERE urun_adi LIKE "+"'%"+str(Ara)+"%'")
    islem.execute(sorgu,(Ara,))
    ui.tbl2.clear()
    ui.tbl2.setHorizontalHeaderLabels(("Ürün Adı","Ürün Alış Fiyatı","Ürün Satış Fiyatı","Adet","KDV","Alınan Ürün Sayısı","Satılan Ürün Sayısı","Tarih"))
    for indexSatir,kayitNumarasi in enumerate(islem):
        for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tbl2.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))

def kayit_sil_gecmis():
    sil_mesaj = QMessageBox.question(pencere,"Silme İşlemini Onayla","Silmek İstediğinizden Emin Misiniz ?")
    QMessageBox.Yes |QMessageBox.No

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tbl2.selectedItems()
        silinecek_kayit = secilen_kayit [0].text()

        sorgu = "delete from Gecmis where Urun_Adi = ?"

        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Silindi.",5000)
            kayit_listele()
        except:
            ui.statusbar.showMessage("Kayıt Silinemedi.",5000)
    
    else:
        ui.statusbar.showMessage("Silme işlemi İptal Edildi.",5000)

#workbook = xlsxwriter.Workbook('veri.xlsx')
#worksheet = workbook.add_worksheet()

#row = 0
#col = 0

#for row_data in Gecmis:
#worksheet.write(row, col, urun_adi)
#worksheet.write(row, col+1, row_data.2)
#worksheet.write(row, col+2, row_data.3)
#  row += 1

#workbook.close()



#buton
        
ui.btn100.clicked.connect(kayit_ekle)
ui.btn101.clicked.connect(Tarihe_gore_listele)
ui.btn102.clicked.connect(kayit_sil_gecmis)
ui.btn103.clicked.connect(Ara)
ui.btn104.clicked.connect(kayit_liste)


kayit_listele()


sys.exit(uygulama.exec_())
