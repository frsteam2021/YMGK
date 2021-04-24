import sqlite3
import cv2
import numpy as np
from ssl import SSLContext,PROTOCOL_TLSv1
from urllib.request import urlopen
from past.builtins import raw_input

class YuzTanimaSistemi():

    def __init__(self,url,kat):
        self.url=url
        self.kat=kat

    def yuzTani(self):
        id = 0
        tanıyıcı = cv2.face.LBPHFaceRecognizer_create()
        tanıyıcı.read("egitim\\egitim.yml")
        cascadePath='Cascade\\haarcascade_frontalface_default.xml'
        yüzCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        def getProfile(id):
            bağlantı = sqlite3.connect("VeriTabanı/YuzTanimaDB.db")
            cmd = "SELECT * FROM Face Where ID=" + str(id)
            gez = bağlantı.execute(cmd)
            profil = None
            for i in gez:
                profil = i
            bağlantı.close()
            return profil

        while True:
            gcontext = SSLContext(PROTOCOL_TLSv1)
            bilgilendirme = urlopen(self.url, context=gcontext).read()
            imgNp = np.array(bytearray(bilgilendirme), dtype=np.uint8)
            im = cv2.imdecode(imgNp, -1)
            im = cv2.resize(im, (740, 580))
            gri = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            yüzler = yüzCascade.detectMultiScale(gri, 1.3, 5)
            for (x, y, w, h) in yüzler:
                # tehlikeli giriş renk
                color_riskli = (0, 0, 255)
                # risksiz giriş renk
                color_risksiz = (0, 255, 0)
                #yetkisiz kat girişi
                color_yetkisiz=(255,0,0)
                id, uyum = tanıyıcı.predict(gri[y:y + h, x:x + w])
                if (uyum<85):
                    profil = getProfile(id)
                    if(self.kat==str(profil[7])):
                        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), color_risksiz, 4)
                        cv2.putText(im, "Ad : " + str(profil[2]), (x, y + h + 38), font, 0.55, color_risksiz, 1)
                        uyum = f"Uyum=  {round(uyum, 0)}%"
                        cv2.putText(im, str(uyum), (x, y + h + 60), font, 0.55, color_risksiz, 1)
                    else:
                        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 4)
                        cv2.putText(im, "Yetkisiz Kat Girisi", (x, y + h + 38), font, 0.55, color_yetkisiz, 1)
                        cv2.putText(im, "Ad : " + str(profil[2]), (x, y + h + 60), font, 0.55, color_yetkisiz, 1)
                        uyum = f"Uyum=  {round(uyum, 0)}%"
                        cv2.putText(im, str(uyum), (x, y + h + 60), font, 0.55, color_yetkisiz, 1)

                else:
                    cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), color_riskli, 4)
                    cv2.putText(im, "Tehlikeli Giris!!!", (x, y + h + 38), font, 0.55, color_riskli, 1)
                    uyum = f"Uyum=  {round(uyum, 0)}%"
                    cv2.putText(im, str(uyum), (x, y + h + 60), font, 0.55, color_riskli, 1)



            cv2.imshow('KAMERA - '+str(self.kat), im)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break


urlGir = str(raw_input("URL GİR : "))
katGir = str(raw_input("Bu Kamera Kaçıncı Kata Ait : "))
var=YuzTanimaSistemi(url="http://"+urlGir+"//shot.jpg",kat=katGir)
var.yuzTani()
