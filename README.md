# YMGK
Fırat Üniversitesi Yazılım Mühendisliği bölümü 
Yazılım Mühendisliği Güncel Konular Dersi Projesi

# Alfa Sürümü Kurulumu:

İlk olarak opencv yi bilgisayarınıza kurmanız gerekmektedir.
Size yardımcı olması açısından linkler bırakılmıştır.
https://www.youtube.com/watch?v=RW_kxqDEzIQ

Kendiniz manuel kurmak isterseniz
---
https://sourceforge.net/projects/opencvlibrary/files/4.5.1/

İkinci olarak telefonunuza IP Webcam adlı mobil uygulamayı indirin
---
![1)googleplay](https://user-images.githubusercontent.com/80630631/115965517-4f298100-a532-11eb-8ec4-9667e419be18.PNG)




# Alfa Sürüm Nasıl Kullanılır

1- Proje dosyası çalıştırılır.
---
2- VeriTabaniKayit.py adlı dosya açılır ve çalıştırılır. Çalışmaya başladığında veri tabanına kayıt edilecek yüzün kişisel bilgileri istenecektir.
   Veri tabanına kayıt edilirken çalışan yada ziyaretci olduğunuzu belirten soruyu doğru cevaplamalısınız.
   Sistem mavi çerçeve içerisinde yüzünüzü algılar ve 100 adet verinizi sisteme kayıt eder.
   Mavi çerçeve aktif olmazsa görüntü almayı sistem otomatik olarak durdurur.
---
![2)KayıtBilgileri](https://user-images.githubusercontent.com/80630631/115965746-42595d00-a533-11eb-97fe-3e1f9964ba7d.PNG)
![3)YüzKayıt](https://user-images.githubusercontent.com/80630631/115965774-60bf5880-a533-11eb-965a-2f6b74a15488.PNG)
---

3-  Verileri_isle.py adlı proje dosyası açılır ve çalıştırılır. Bu sayede artık kayıt altına alınan görüntülerimiz ile eğitilmiş bir model ortaya çıkarılır.
---
![4)egitimmodel](https://user-images.githubusercontent.com/80630631/115965797-759bec00-a533-11eb-9269-07f67cf59859.PNG)
---
4-  Telefonunuuzun bilgisayar ile aynı wifi ağına bağlı olduğuna emin olunuz. Aksi takdirde kamera algılanmaz. Ip webcam uygulamasını açınız ve sayfanın aşağısında bulunan 
"Start server" butonuna basınız. 

---
![startserver png](https://user-images.githubusercontent.com/80630631/115966527-a2053780-a536-11eb-80be-400783ef1d5f.jpg)
---
![ıpv4 png](https://user-images.githubusercontent.com/80630631/115966532-ac273600-a536-11eb-9058-11fe2e6db4dc.jpg)
---
5- YuzTanimaSistemi.py klasörünü çalıştırın.Karşınıza çıkan ekranda "IPv4:" bir ifade göreceksiniz. Bu ifadede sadece 192.168.1.101:8080 formatında olan kısmı YuzTanımaSistemi.py dosyasını çalıştırdığınızda gelen url sorusuna cevap olarak giriniz. Kamerayı güvenliğini sağlayacağınız binanın kaçıncı katında kullanacaksanız. Kat sorusuna cevap verin.
---
![5)KameraBilgileri](https://user-images.githubusercontent.com/80630631/115966574-ef81a480-a536-11eb-8cc5-00492bb945dd.PNG)
---
6-  Artık sistem kurulumu tamamdır. Güvenli Günler Dileriz..(FrsTeam)
---
![6)yüzTanıma](https://user-images.githubusercontent.com/80630631/115966618-29eb4180-a537-11eb-9b10-b0fbd2099d3d.PNG)



#Alfa Sürüm:
---
1- Her kişiye verilen benzersiz id ile görüntüyü Veriler klasörüne aktarır.
---
2- Kişinin kişisel bilgileri veri tabanında tutulur.
---
2- Veriler klasöründe bulunan verileri opencv sayesinde eğiterek bir egitim adında model ortaya çıkarır.
---
3- Bağlamak istediğiniz kamerayı kat bilgileri ile sisteme kayıt edersiniz.
---
4- Kişisel bilgiler bölümünde kişiye atanan izinli kat değeri ile kameraya atanan kat değeri aynı ise herhangi bir güvenlik açığı olmayacaktır.
---
5- Kişisel bilgiler bölümünde kişiye atanan izinli kat değeri ile kameraya atanan kat değeri aynı değil yetkisiz giriş ile ekranda görevli kişiyi uyaran bir ibare olacaktır.
---
6- Eğer sisteme kayıtlı olmayan biri binaya giriş yaparsa sistem tehlikeli giriş ifadesi ile sistemde görevli kişiye uyarı verecektir.
---

























