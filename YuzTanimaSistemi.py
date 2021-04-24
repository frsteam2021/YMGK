import cv2

class YuzTanimaSistemi:
    def yuzTani(self):
        tanıyıcı = cv2.face.LBPHFaceRecognizer_create()
        # eğitmiş olduğumuz model
        tanıyıcı.read('egitim\\egitim.yml')
        # yüzleri algılamamız için gerekli araç
        cascadePath = "Cascade\\haarcascade_frontalface_default.xml"
        yüzCascade = cv2.CascadeClassifier(cascadePath)
        # ekranda yüzün etrafında çıktı almamız için gerekli font ayarı
        font = cv2.FONT_HERSHEY_SIMPLEX
        # id sayacı
        id = 0
        isimler = ['None', 'İsim-1',"İsim-2","İsim-3"]

        # Webcam'den görüntü almak için
        webcam = cv2.VideoCapture(0)
        webcam.set(3, 1000)  # video genişliğini belirle
        webcam.set(4, 800)  # video yüksekliğini belirle


        while True:
            # Webcam'den gelen görüntüyü okuma
            ret, img = webcam.read()
            # görüntüyü siyah beyaz yapma
            gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # yüzleri algılama
            yüzler = yüzCascade.detectMultiScale(gri, 1.3, 5)
            for (x, y, w, h) in yüzler:
                # tehlikeli giriş renk
                color_riskli=(0,0,255)
                #risksiz giriş renk
                color_risksiz=(0,255,0)
                # algılanan yüzlerin modeldeki yüzlerle uyum değeri
                id, uyum = tanıyıcı.predict(gri[y:y + h, x:x + w])

                # eğer bir uyum varsa ki burda uyum mantığı tam ters işliyor
                if (uyum < 85):
                    # algılanan yüzlerin etrafında çerçeve çiz
                    cv2.rectangle(img, (x, y), (x + w, y + h), color_risksiz, 2)
                    id = isimler[id]
                    uyum = f"Uyum=  {round(uyum, 0)}%"
                    # kişinin bilgilerini getirir
                    cv2.putText(img, "Ad : " + str(id), (x, y + h + 38), font, 0.55, color_risksiz, 1)
                    cv2.putText(img, str(uyum), (x, y + h + 60), font, 0.55, color_risksiz, 1)

                # kişi yoksa ekranda bilinmiyor yazdır ve tehlikeli giriş diye ekrana yazdır
                else:
                    # algılanan yüzlerin etrafında çerçeve çiz
                    cv2.rectangle(img, (x, y), (x + w, y + h), color_riskli, 2)
                    id = "Tehlikeli Giris"
                    uyum = f"Uyum=  {round(uyum, 0)}%"
                    cv2.putText(img, str(id), (x, y + h + 38), font, 0.55, color_riskli, 1)

            cv2.imshow('Yuz Tanima Sistemi', img)
            # Yüz Tanıma Sisteminden çıkış için Esc veya q tuşu
            k = cv2.waitKey(10) & 0xff
            if k == 27 or k == ord('q'):
                break
        # Belleği temizle
        print("\nProgramdan çıkılıyor ve bellek temizleniyor...")
        webcam.release()
        cv2.destroyAllWindows()

tani=YuzTanimaSistemi()
tani.yuzTani()