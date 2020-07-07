from PyQt5 import QtCore, QtGui, QtWidgets
import resource_rc


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1366, 768)
        mainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        mainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 111, 71))
        self.label.setStyleSheet("image: url(:/icon/icon.ico);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 651, 131))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.diagnosa = QtWidgets.QPushButton(self.centralwidget)
        self.diagnosa.setGeometry(QtCore.QRect(620, 280, 100, 50))
        self.diagnosa.setIconSize(QtCore.QSize(30, 25))
        self.diagnosa.setObjectName("diagnosa")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 380, 100, 50))
        self.pushButton_2.setIconSize(QtCore.QSize(30, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 290, 279, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.g1y = QtWidgets.QRadioButton(self.layoutWidget)
        self.g1y.setObjectName("g1y")
        self.horizontalLayout_31.addWidget(self.g1y)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 600, 289, 39))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 520, 289, 44))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 430, 289, 50))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 330, 289, 56))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 289, 65))
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 380, 279, 44))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.g2y = QtWidgets.QRadioButton(self.layoutWidget1)
        self.g2y.setObjectName("g2y")
        self.horizontalLayout_32.addWidget(self.g2y)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 470, 279, 44))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.g3y = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.g3y.setObjectName("g3y")
        self.horizontalLayout_33.addWidget(self.g3y)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 550, 279, 44))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.g4y = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.g4y.setObjectName("g4y")
        self.horizontalLayout_34.addWidget(self.g4y)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 630, 279, 44))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.g5y = QtWidgets.QRadioButton(self.layoutWidget_4)
        self.g5y.setObjectName("g5y")
        self.horizontalLayout_35.addWidget(self.g5y)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(310, 470, 279, 44))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.g8y = QtWidgets.QRadioButton(self.layoutWidget_5)
        self.g8y.setObjectName("g8y")
        self.horizontalLayout_36.addWidget(self.g8y)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 330, 289, 56))
        self.label_5.setObjectName("label_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, 520, 289, 44))
        self.label_13.setObjectName("label_13")
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(310, 630, 279, 44))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.g10y = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.g10y.setObjectName("g10y")
        self.horizontalLayout_37.addWidget(self.g10y)
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(310, 550, 279, 44))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.g9y = QtWidgets.QRadioButton(self.layoutWidget_7)
        self.g9y.setObjectName("g9y")
        self.horizontalLayout_38.addWidget(self.g9y)
        self.layoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(310, 380, 279, 44))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.g7y = QtWidgets.QRadioButton(self.layoutWidget_8)
        self.g7y.setObjectName("g7y")
        self.horizontalLayout_39.addWidget(self.g7y)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(310, 600, 289, 39))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 430, 289, 50))
        self.label_16.setObjectName("label_16")
        self.layoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_9.setGeometry(QtCore.QRect(310, 290, 279, 44))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.g6y = QtWidgets.QRadioButton(self.layoutWidget_9)
        self.g6y.setObjectName("g6y")
        self.horizontalLayout_40.addWidget(self.g6y)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(310, 240, 289, 65))
        self.label_17.setObjectName("label_17")
        self.deskripsi = QtWidgets.QTextEdit(self.centralwidget)
        self.deskripsi.setGeometry(QtCore.QRect(800, 10, 551, 361))
        self.deskripsi.setObjectName("deskripsi")
        self.penanganan = QtWidgets.QTextEdit(self.centralwidget)
        self.penanganan.setGeometry(QtCore.QRect(800, 390, 551, 361))
        self.penanganan.setObjectName("penanganan")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "EXPERT SYSTEM"))
        self.label_3.setText(_translate("mainWindow", "HEADACHE EXPERT SYSTEM"))
        self.label_2.setText(_translate("mainWindow", "APLIKASI EXPERT SYSTEM BERBASIS BAHASA PYTHON\n"
"ISILAH GEJALA-GEJALA YANG DIMILIKI OLEH PASIEN DENGAN JUJUR\n"
"CUKUP ISI GEJALA YANG DIDERITA!"))
        self.diagnosa.setText(_translate("mainWindow", "DIAGNOSA"))
        self.pushButton_2.setText(_translate("mainWindow", "RESET"))
        self.g1y.setText(_translate("mainWindow", "Ya"))
        self.label_9.setText(_translate("mainWindow", "5. Mata Merah?"))
        self.label_8.setText(_translate("mainWindow", "4. Nyeri Kepala Terpusat Pada Mata?"))
        self.label_7.setText(_translate("mainWindow", "3. Pusing Berputar?"))
        self.label_4.setText(_translate("mainWindow", "2. Nyeri Otot Leher?"))
        self.label_6.setText(_translate("mainWindow", "1. Lelah?"))
        self.g2y.setText(_translate("mainWindow", "Ya"))
        self.g3y.setText(_translate("mainWindow", "Ya"))
        self.g4y.setText(_translate("mainWindow", "Ya"))
        self.g5y.setText(_translate("mainWindow", "Ya"))
        self.g8y.setText(_translate("mainWindow", "Ya"))
        self.label_5.setText(_translate("mainWindow", "7. Nyeri Seperti Tertekan?"))
        self.label_13.setText(_translate("mainWindow", "9. Konsentrasi Terganggu?"))
        self.g10y.setText(_translate("mainWindow", "Ya"))
        self.g9y.setText(_translate("mainWindow", "Ya"))
        self.g7y.setText(_translate("mainWindow", "Ya"))
        self.label_15.setText(_translate("mainWindow", "10. Sulit Tidur / Susah Bangun?"))
        self.label_16.setText(_translate("mainWindow", "8. Gelisah?"))
        self.g6y.setText(_translate("mainWindow", "Ya"))
        self.label_17.setText(_translate("mainWindow", "6. Air Mata Keluar?"))
        self.deskripsi.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DESKRIPSI PENYAKIT</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.penanganan.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PENANGANAN PENYAKIT</p></body></html>"))

        self.diagnosa.clicked.connect(self.diagnosaa)
        self.pushButton_2.clicked.connect(self.reset)


    def reset(self):
        self.g1y.setChecked(False)
        self.g2y.setChecked(False)

        self.g3y.setChecked(False)
        self.g4y.setChecked(False)

        self.g5y.setChecked(False)
        self.g6y.setChecked(False)

        self.g7y.setChecked(False)
        self.g8y.setChecked(False)

        self.g9y.setChecked(False)
        self.g10y.setChecked(False)
        self.deskripsi.setText('DESKRIPSI PENYAKIT')
        self.penanganan.setText('PENANGANAN PENYAKIT')

    def diagnosaa(self):
        #sakit kepala cluster
        if self.g2y.isChecked() & self.g4y.isChecked() & self.g5y.isChecked() & self.g6y.isChecked() & self.g9y.isChecked():
            self.deskripsi.setText('''SAKIT KEPALA CLUSTER\n\n
*Sakit kepala cluster adalah salah satu jenis nyeri kepala yang paling nyeri.

*Sakit kepala cluster timbul dalam sebuah pola tertentu pada seseorang.

*Sakit kepala cluster dapat membangunkan seseorang ketika sedang tidur pada malam hari dengan nyeri khas di sekitar salah satu mata atau salah satu sisi kepala.


Faktor risiko yang termasuk dalam Sakit Kepala Cluster yaitu:
- Jenis kelamin.
  Laki-laki lebih mudah terkena nyeri kepala cluster daripada perempuan.

- Umur.
  Banyak sekali angka kejadian nyeri kepala cluster terjadi pada rentan umur 20 hingga 25 tahun.

- Merokok.
  Cluster sering kali menyerang pada seseorang dengan riwayat merokok.

- Penggunaan alkohol.
  Jika pernah mengalami nyeri kepala cluster, meminum alkohol selama masa serangan akan menjadikan penderita semakin mudah terkena serangan nyeri kepala cluster.

- Riwayat keluarga.
  Memiliki saudara atau anggota keluarga yang memiliki nyeri kepala cluster dapat meningkatkan kemungkinan terjadinya nyeri kepala cluster.


Penyebab Sakit Kepala Cluster
Penyebab pasti dari nyeri kepala cluster masih belum diketahui, namun pola serangan nyeri kepala cluster diketahui berkaitan dengan jam biologis seseorang. 


Diagnosis Sakit Kepala Cluster
- Pemeriksaan saraf.
  dilakukan untuk menyingkirkan kemungkinan penyebab neurologi lain. 

- MRI.
  Digunakan untuk memberikan gambaran detail pembuluh darah dalam otak

- CT Scan. 
  Digunakan untuk memberikan gambaran struktur otak.


Pencegahan Sakit Kepala Cluster
- Penyekat kanal kalsium.
  Agen penyekat kanal kalsium seperti verapamil sering digunakan untuk mencegah nyeri kepala cluster

- Steroid.
  Obat anti inflamasi steroid seperti prednison dapat digunakan secara efektif untuk mencegah nyeri kepala cluster.

- Lithium carbonat.
  Digunakan apabila pilihan terapi lain gagal digunakan untuk mencegah nyeri kepala cluster.            
            ''')


            self.penanganan.setText('''PENGOBATAN SAKIT KEPALA CLUSTER\n\n
Pengobatan untuk fase akut dapat dilakukan dengan memberikan beberapa pilihan obat:
- Oksigen.
  Pemberian oksigen dapat meredakan nyeri kepala dengan cepat.

- Triptan.
  Pilihan triptan yang juga digunakan pada nyeri kepala migrain juga dapat digunakan dalam nyeri kepala cluster.

- Dihydroergotamine.
  Dihydroergotamin dapat digunakan sebagai pereda nyeri yang efektif untuk nyeri kepala cluster.
             ''')

        #sakit kepala migrain
        elif self.g1y.isChecked() & self.g2y.isChecked() & self.g3y.isChecked() & self.g9y.isChecked():
            self.deskripsi.setText('''SAKIT KEPALA MIGRAIN\n\n
Migrain adalah suatu gangguan neurovascular yang disebabkan oleh inflamasi neurogenik.

Kondisi ini dimanifestasi klinis nyeri kepala yang lebih dominan di satu sisi (unilateral) dan umumnya berdenyut (pulsating) yang berlangsung selama 4-72 jam.


Faktor Risiko Migrain
Terdapat beberapa faktor risiko yang dapat menyebabkan seseorang lebih mudah alami migrain, yaitu:
- jenis kelamin

- umur

- mengalami stres.


Penyebab Migrain
Terdapat berbagai macam hipotesis mengenai migrain.

Hipotesis neurovaskular menyatakan bahwa migrain adalah kepekaan sistem trigeminal vaskular yang diturunkan.
Mekanisme utama yang mendasari seseorang mengalami migrain bisa meliputi teori biologis, psikologis, dan psikofisiologis. 


Diagnosis Migrain
Migrain dapat ditegakkan melalui anamesis yang lengkap, gejala nyeri kepala unilateral, kualitas nyeri kepala, ada atau tidaknya fase aura, serta lamanya nyeri kepala.

Kriteria diagnosis yaitu sebagai berikut:
- Migrain Tanpa Aura

  Setidaknya lima serangan memenuhi kriteria B hingga D.

  Serangan sakit kepala bisa terjadi 4 hingga 72 jam (tidak dirawat atau telah dirawat, tetapi belum sukses).

  Sakit kepala memiliki setidaknya dua dari karakteristik berikut:
	1. Lokasinya satu sisi (unilateral)

	2. Kualitas berdenyut (pulsating)

	3. Intensitas nyeri sedang atau berat

	4. Diperberat oleh atau menyebabkan terganggunya aktivitas fisik rutin/harian (misalnya berjalan atau naik tangga)


  Selama sakit kepala berlangsung setidaknya disertai satu hal berikut ini:
	1. Mual dan/atau muntah

	2. Photophobia dan phonophobia

	3. Tidak berhubungan dengan gangguan lainnya.

- Migrain dengan Aura
  Setidaknya dua serangan memenuhi kriteria B.

  Migrain dengan aura memenuhi kriteria B dan C untuk satu dari subklasifikasi. Jenisnya antara lain typical aura with migraine headache, typical aura with non-migraine headache, typical aura without headache, familial hemiplegic migraine, sporadic hemiplegic migraine, dan basilar-type migraine.

  Tidak berhubungan dengan gangguan lainnya.


Pencegahan Migrain

Hindari faktor-faktor pemicu yang bersifat multifaktorial, antara lain:
- Faktor hormonal.

- Diet (alkohol, daging yang mengandung nitrat, monosodium glutamat, aspartam, cokelat, keju yang sudah lama/basi, tidak makan, puasa, dan minuman mengandung kafein).

- Psikologis (stres, kondisi setelah stres/liburan akhir minggu, cemas, takut, depresi).

- Lingkungan fisik (cahaya menyilaukan, cahaya terang, stimulasi visual, dan sinar berpendar).            
            ''')

            self.penanganan.setText('''PENGOBATAN SAKIT KEPALA MIGRAIN\n\n
Pengobatan migrain dilakukan berdasarkan penyebab dari masing-masing orang

Sebaiknya segera melakukan pemeriksaan kepada dokter untuk penanganan yang tepat, umumnya terapi serangan akut untuk migrain juga bisa diberikan.            
            ''')

        #sakit kepala tegang
        elif self.g2y.isChecked() & self.g7y.isChecked() & self.g9y.isChecked():
            self.deskripsi.setText('''SAKIT KEPALA TEGANG
Sakit kepala tegang atau tension headache adalah jenis sakit kepala yang rasanya sering digambarkan seperti ada tali yang mengikat kuat pada kepala.

Kondisi ini bisa dialami siapa saja dan pada usia berapa pun, namun lebih sering terjadi pada wanita dewasa.

Meski cukup mengganggu, sebagian besar sakit kepala tegang tidak terlalu parah, sehingga penderitanya masih bisa melakukan kegiatan sehari-hari.


Penyebab Sakit Kepala Tegang
Penyebab sakit kepala tegang berupa kontraksi otot pada kepala dan di sekitar leher. Sedangkan faktor pemicunya berupa:
- Dehidrasi.

- Kelaparan.

- Kurangnya istirahat.

- Sinar matahari yang terlalu terik.

- Tidak banyak berolahraga.

- Kelebihan obat pereda sakit dalam jangka waktu lebih dari 10 hari.

- Stres.

- Jenis kelamin, khususnya wanita.

- Usia, khsusnya lebih diatas 40 tahun.

- Suara berisik.

- Aroma tertentu.

- Postur tubuh yang buruk.


Pencegahan Sakit Kepala Tegang

Memperbaiki gaya hidup, misalnya melakukan olahraga secara rutin, menjaga berat badan, cukup beristirahat, banyak minum air putih dan hindari merokok dan minuman keras.

Menghindari faktor pemicu sakit kepala.                        
            ''')

            self.penanganan.setText('''PENGOBATAN SAKIT KEPALA TEGANG\n\n
Sakit kepala tegang bisa disembuhkan dengan penanganan yang sederhana, seperti:
- Menghindari faktor pemicu sakit kepala.

- Mengompres bagian dahi dan leher dengan air hangat atau dingin.

- Melakukan sejumlah reknik relaksasi.

- Mengonsumsi analgesik sesuai dengan tata cara pemakaian   dan pemilihan jenis yang sesuai.

- Memperbaiki gaya hidup, misalnya melakukan olahraga secara rutin, menjaga berat badan, cukup beristirahat, banyak minum air putih dan hindari merokok dan minuman keras.            
            ''')            

        else:
            self.deskripsi.setText('PENYAKIT YANG DICARI TIDAK DITEMUKAN!')
            self.penanganan.setText('PENANGANAN YANG DICARI TIDAK DITEMUKAN!')

                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
