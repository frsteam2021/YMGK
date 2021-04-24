import cv2
import numpy as np
from PIL import Image
import os
import cv2
import numpy as np
from PIL import Image

class FotografIsle:
    tanıyıcı = cv2.face.LBPHFaceRecognizer_create()
    dosyaYolu = 'Veriler'

    def verileriEgit(dosyaYolu):
        detector = cv2.CascadeClassifier("Cascade\\haarcascade_frontalface_default.xml")
        imagedosyaYolus = [os.path.join(dosyaYolu, f) for f in os.listdir(dosyaYolu)]
        ornekler = []
        ids = []
        for imagedosyaYolu in imagedosyaYolus:
            PIL_img = Image.open(imagedosyaYolu).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagedosyaYolu)[-1].split(".")[0])
            # print("id= ",id)
            yuzler = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in yuzler:
                ornekler.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return ornekler, np.array(ids)

    print("\n Yüzler eğitiliyor. Birkaç saniye bekleyin ...")
    yuzler, ids = verileriEgit(dosyaYolu)
    tanıyıcı.update(yuzler, ids)
    # Modeli egitim/egitim.yml dosyasına kaydet
    tanıyıcı.write('egitim\\egitim.yml')
    # Eğitilen yüz sayısını göster ve kodu sonlandır
    print(f"\n  {len(np.unique(ids))} yüz eğitildi. Program sonlandırılıyor.")

FotografIsle.verileriEgit('Veriler')
