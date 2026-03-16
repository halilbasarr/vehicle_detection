# OpenCV ile Araç Tespiti (Haar Cascade)

Bu proje, Python ve OpenCV kütüphanesi kullanılarak videolardaki araçları gerçek zamanlı (veya video üzerinden) tespit etmek amacıyla geliştirilmiştir. Haar Cascade sınıflandırıcısı kullanılarak araçların koordinatları belirlenmekte ve görüntü üzerine işaretlenmektedir.

## 🚀 Proje Hakkında
Bu çalışma, görüntü işleme temellerini anlamak ve nesne tespiti algoritmalarını pratik etmek için hazırlanmıştır. Proje kapsamında:
* Haar Cascade algoritmalarının çalışma prensibi incelenmiştir.
* Video kareleri üzerinde gri tonlama (grayscale) dönüşümleri yapılmıştır.
* `detectMultiScale` fonksiyonu ile araç tespiti optimize edilmiştir.

## 🛠 Kullanılan Teknolojiler
* **Python**
* **OpenCV** (Görüntü İşleme)
* **Numpy** (Matematiksel İşlemler)

## 📁 Dosya Yapısı
* `vehicle_detection.py`: Ana uygulama kodu.
* `cars.xml`: Araç tespiti için eğitilmiş Haar Cascade modeli.
* `dataset/`: Test için kullanılan video dosyalarını içeren klasör.

## 💻 Kurulum ve Çalıştırma
Projeyi yerel bilgisayarınızda çalıştırmak için:

1. Bu depoyu klonlayın:
   ```bash
   git clone [https://github.com/kullanici-adiniz/arac-tespiti-opencv.git](https://github.com/kullanici-adiniz/arac-tespiti-opencv.git)
