import numpy as np
import cv2
import os

# 1. Dosya Yollarını Dinamik Hale Getirme
# 'os.path.join' kullanarak klasör yapısına göre dosyaları otomatik buluyoruz.
# Bu sayede kullanıcılar projeyi indirdiğinde kendi bilgisayar yollarını yazmak zorunda kalmaz.
base_path = os.path.dirname(os.path.abspath(__file__))
cascade_path = os.path.join(base_path, 'cars.xml')
video_path = os.path.join(base_path, 'dataset', 'video2.avi')

# 2. Cascade Sınıflandırıcısını Yükleme
# Haar Cascade algoritmasını kullanarak araç tespiti yapacak modeli yüklüyoruz.
car_cascade = cv2.CascadeClassifier(cascade_path)

# Dosyanın doğru yüklenip yüklenmediğini kontrol ediyoruz.
if car_cascade.empty():
    print(f"Hata: Cascade dosyası bulunamadı! Lütfen şu yolu kontrol edin: {cascade_path}")
    exit()

# 3. Video Kaynağını Başlatma
cap = cv2.VideoCapture(video_path)

# Video dosyasının açılıp açılmadığını kontrol ediyoruz.
if not cap.isOpened():
    print(f"Hata: Video dosyası açılamadı! Lütfen şu yolu kontrol edin: {video_path}")
    exit()

while True:
    # Videodan kare kare okuma yapıyoruz.
    ret, frame = cap.read()
    
    # Video bittiyse veya okunamazsa döngüyü kırıyoruz.
    if not ret:
        print("Video akışı bitti veya kare okunamadı.")
        break

    # Görüntü İşleme: Kareyi gri tonlamaya çeviriyoruz (Haar Cascade gri tonda daha hızlı çalışır).
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Araç Tespiti: detectMultiScale ile araçların koordinatlarını buluyoruz.
    # scaleFactor=1.1, minNeighbors=3 (Hassasiyeti artırmak için bu değerlerle oynanabilir).
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    # Tespit edilen her araç için bir dikdörtgen çiziyoruz.
    for (x, y, w, h) in cars:
        # frame üzerine, (x,y) sol üst ve (x+w, y+h) sağ alt koordinatlarına yeşil (0,255,0) kutu çiziyoruz.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Arac', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Sonucu ekranda gösteriyoruz.
    cv2.imshow('Araba Tespiti Sistemi', frame)

    # 'q' tuşuna basıldığında döngüden çıkış yapıyoruz.
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırakma ve pencereleri kapatma.
cap.release()
cv2.destroyAllWindows()