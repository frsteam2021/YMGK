# YMGK
Fırat Üniversitesi Yazılım Mühendisliği bölümü Yazılım Mühendisliği Güncel Konular ders projesi

Alfa Sürümü Kurulumu:
İlk olarak opencv yi bilgisayarınıza kurmanız gerekmektedir.
Size yardımcı olması açısından linkler bırakılmıştır.
https://www.youtube.com/watch?v=RW_kxqDEzIQ
Kendiniz manuel kurmak isterseniz 
https://sourceforge.net/projects/opencvlibrary/files/4.5.1/
İkinci olarak telefonunuza IP Webcam adlı mobil uygulamayı indirin.


Alfa Sürüm Nasıl Kullanılır
1- Proje dosyası çalıştırılır.
2- VeriTabaniKayit.py adlı dosya açılır ve çalıştırılır. Çalışmaya başladığında veri tabanına kayıt edilecek yüzün kişisel bilgileri istenecektir.
   Veri tabanına kayıt edilirken çalışan yada ziyaretci olduğunuzu belirten soruyu doğru cevaplamalısınız.
   Sistem mavi çerçeve içerisinde yüzünüzü algılar ve 100 adet verinizi sisteme kayıt eder.
   Mavi çerçeve aktif olmazsa görüntü almayı sistem otomatik olarak durdurur.
3  Verileri_isle.py adlı proje dosyası açılır ve çalıştırılır. Bu sayede artık kayıt altına alınan görüntülerimiz ile eğitilmiş bir model ortaya çıkarılır.
4  Telefonunuuzun bilgisayar ile aynı wifi ağına bağlı olduğuna emin olunuz. Aksi takdirde kamera algılanmaz. Ip webcam uygulamasını açınız ve sayfanın aşağısında bulunan 
"Start server" butonuna basınız. Karşınıza çıkan ekranda "IPv4:" bir ifade göreceksiniz. Bu ifadede sadece 192.168.1.101:8080 formatında olan kısmı YuzTanımaSistemi.py dosyasını çalıştırdığınızda
gelen url sorusuna cevap olarak giriniz. Kamerayı güvenliğini sağlaycağınız binanın kaçıncı katında kullanacaksanız. Kat sorusuna cevap verin.
5  Artık sistem kurulumu tamamdır. Güvenli Günler Dileriz..(FrsTeam)


Alfa Sürüm:
1- Her kişiye verilen benzersiz id ile görüntüyü Veriler klasörüne aktarır.
2- Kişinin kişisel bilgileri veri tabanında tutulur.
2- Veriler klasöründe bulunan verileri opencv sayesinde eğiterek bir egitim adında model ortaya çıkarır.
3- Bağlamak istediğiniz kamerayı kat bilgileri ile sisteme kayıt edersiniz.
4- Kişisel bilgiler bölümünde kişiye atanan izinli kat değeri ile kameraya atanan kat değeri aynı ise herhangi bir güvenlik açığı olmayacaktır.
5- Kişisel bilgiler bölümünde kişiye atanan izinli kat değeri ile kameraya atanan kat değeri aynı değil yetkisiz giriş ile ekranda görevli kişiyi uyaran bir ibare olacaktır.
6- Eğer sisteme kayıtlı olmayan biri binaya giriş yaparsa sistem tehlikeli giriş ifadesi ile sistemde görevli kişiye uyarı verecektir.



























