import cv2
from past.builtins import raw_input
class VeriTabaniKayit:
    def __init__(self,yuz_id):
        # Her yüz için farklı bir id ataması yapılmalı ki sistem yüzleri algılarken doğru bilgileri getirsin
        self.yuz_id=yuz_id

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
        sayac = 0
        while (True):
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
                cv2.imwrite("Veriler/" + str(self.yuz_id) + '.' + str(sayac) + ".jpg", gri[y:y + h, x:x + w])
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
calistir=VeriTabaniKayit(yuz_id=id)
print("Kişisel Bilgiler Sisteme Kayıt Edildi")
print("Yüz tanıma sistemine kayıt için lütfen başınızı mavi çerçeveden çıkmayacak şekilde sağa sola yukarı ve aşağı şekilde oynatınız..")
calistir.sistemeGoruntuKayit()