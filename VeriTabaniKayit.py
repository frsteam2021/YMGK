import cv2
import sqlite3
from past.builtins import raw_input
import time
import datetime

class VeriTabaniKayit:
    def __init__(self,Id,Tc,Ad,Soyad,Birim,Adres,Telefon,IzinKat,Tarih):
        self.Id=Id
        self.Tc = Tc
        self.Ad = Ad
        self.Soyad = Soyad
        self.Birim = Birim
        self.Adres = Adres
        self.Telefon = Telefon
        self.IzinKat = IzinKat
        self.Tarih = Tarih
    def veriTabaniKayit(self):
        bağlantı=sqlite3.connect("VeriTabanı/YuzTanimaDB.db")
        komut="SELECT * FROM Face WHERE id="+str(self.Id)
        gez = bağlantı.execute(komut)
        isRecordExist = 0
        for i in gez:
            isRecordExist=1
        if(isRecordExist==1):
            komut="UPDATE Face id="+str(self.Id) +"AND tc="+str(self.Tc)+"AND ad="+str(self.Ad)+"AND soyad="+str(self.Soyad)+"AND birim="+str(self.Birim)+"AND adres="+str(self.Adres)+"AND telefon="+str(self.Telefon)+"AND izin="+str(self.IzinKat)+"AND tarih="+str(self.Tarih) +"WHERE id=" + str(self.id)
        else:
            bağlantı.execute("INSERT INTO Face (id,tc,ad,soyad,birim,adres,telefon,izin,tarih) Values(?,?,?,?,?,?,?,?,?)",(self.Id,self.Tc,self.Ad,self.Soyad,self.Birim,self.Adres,self.Telefon,self.IzinKat,self.Tarih))
        bağlantı.execute(komut)
        bağlantı.commit()
        bağlantı.close()
    def veriTabaniKayitSilme(self):
        bağlantı=sqlite3.connect("VeriTabanı/YuzTanimaDB.db")
        bağlantı.execute("Delete From Face Where id= ?", str(self.Id))
        bağlantı.commit()

    """YÜZ ALGILAMA VE SİSTEME KAYIT AŞAMASI"""
    def sistemeGoruntuKayit(self):
        """KAMERA İŞLEMLERİ"""
        # VideoCapture() içine 0 yazarsak donanımlarım içinden webcam'ı açar. Ek olarak donanım varsa 1,2 diyerek yazılabilir.
        webcam = cv2.VideoCapture(0)
        # video genişliğini belirle
        webcam.set(3, 640)
        # video yüksekliğini belirle
        webcam.set(4, 480)
        # OPEN-CV'nin sınıflandırıcısını ekliyoruz. Yüzleri eğitmemizde yardımcı araçtır. Görüntüde yüz algılamaya çalışır.
        yuz_tarayici = cv2.CascadeClassifier('Cascade\\haarcascade_frontalface_default.xml')
        sayac=0
        while True:
            # webcamdan gelen görüntüyü alma
            ret, img = webcam.read()
            # gelen görüntü farklı bir eksen de ise bu yardımcı kod parçasını kullan
            # img = cv2.flip(img, -1)
            # bulduğumuz görüntüyü siyah beyaz yapıyoruz
            gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # görüntüden yüzler algılıyoruz
            yuzler = yuz_tarayici.detectMultiScale(gri, 1.3, 5)
            for (x, y, w, h) in yuzler:
                # yüzlerin etrafına çerçeve çiziyoruz
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sayac += 1
                # Yakalanan yüzleri Veriler klasörüne kaydetiyoruz
                cv2.imwrite("Veriler/" + str(self.Id) + '.' + str(sayac) + ".jpg", gri[y:y + h, x:x + w])
                # açılan pencerenin adı ve açılan pencerede gözükecek görüntü
                cv2.imshow('Yüz Kayıt Sistemi', img)
                print("Kayıt no: ", sayac)
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif sayac >= 100:
                break
            # Belleği temizle
        print("\n  Program sonlanıyor ve bellek temizleniyor.")
        webcam.release()
        cv2.destroyAllWindows()



print("FRS-TEAM YÜZ TANIMA SİSTEMİ YÜZ KAYIT OTOMASYONU")
id = raw_input('ID : ')
tc = str(raw_input('TC : '))
ad = str(raw_input('AD : '))
soyad = str(raw_input('SOYAD : '))
birim = str(raw_input('Birim(Ziyaretci yada Çalışan, Çalışan ise lütfen birimi) : '))
adres = str(raw_input('ADRES : '))
telefon = str(raw_input('TELEFON : '))
kat = raw_input('İzin verilen kat : ')
tarih = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


Veri=VeriTabaniKayit(id,tc,ad,soyad,birim,adres,telefon,kat,tarih)
Veri.veriTabaniKayit()
print("Kişisel Bilgiler Veri Tabanına Kayıt Edildi")
print("Yüz tanıma sistemine kayıt için lütfen başınızı mavi çerçeveden çıkmayacak şekilde sağa sola yukarı ve aşağı şekilde oynatınız..")
Veri.sistemeGoruntuKayit()