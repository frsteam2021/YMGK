# YMGK
Fırat Üniversitesi Yazılım Mühendisliği bölümü Yazılım Mühendisliği Güncel Konular ders projesi

Prototip Sürümü Kurulumu
İlk olarak opencv yi bilgisayarınıza kurmanız gerekmektedir.
Size yardımcı olması açısından linkler bırakılmıştır.
https://www.youtube.com/watch?v=RW_kxqDEzIQ
Kendiniz manuel kurmak isterseniz 
https://sourceforge.net/projects/opencvlibrary/files/4.5.1/


Prototip sürüm nasıl kullanılır
1-)Proje dosyası çalıştırılır.
2-)VeriTabaniKayit.py adlı dosya açılır ve çalıştırılır. Çalışmaya başladığında sisteme kayıt edilecek yüzün benzersiz olacak bir id'si istenecektir.
   Sisteme id yazıldıktan sonra bir görüntü ekranı açılacaktır. Sistem mavi çerçeve içerisinde yüzünüzü algılar ve 100 adet verinizi sisteme kayıt eder.
   Mavi çerçeve aktif olmazsa görüntü almayı sistem otomatik olarak durdurur.
3-)Verileri_isle.py adlı proje dosyası açılır ve çalıştırılır. Bu sayede artık kayıt altına alınan görüntülerimiz ile eğitilmiş bir model ortaya çıkarılır.
4-)YuzTanımaSistemi.py proje dosyası açılır ve içerisinde bulunan isimler değişkeni bulunur. Kayıt etmiş olduğunuz görüntü kime ait ise isim-1 yerine yazılır ve çalıştırılır.


Prototip Sürüm:
1- Her kişiye verilen benzersiz id ile görüntüyü Veriler klasörüne aktarır.
2- Veriler klasöründe bulunan verileri opencv sayesinde eğiterek bir egitim adında model ortaya çıkarır.
3- Bilgisayara ait webcam ile canlı görüntüden yüzler algılanır ve modeldeki yüzler ile karşılaştırılır. Yüz mevcut ise id karşılığı olan isim ekranda yüzü çerçeveleyen yerde yazdırılır.
Eğer yüz modelde mevcut değil ise ekranda "tehlikeli giriş" yazısı yazdırılır.

