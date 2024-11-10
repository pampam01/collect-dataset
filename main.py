import cv2
import os

# Buat folder untuk menyimpan gambar jika belum ada
save_path = "dataset"
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Inisialisasi kamera
cap = cv2.VideoCapture(0)  # 0 untuk kamera depan

count = 0  # untuk menghitung jumlah gambar yang diambil

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Tampilkan hasil dari kamera
    cv2.imshow("Camera", frame)

    # Tekan 's' untuk menyimpan gambar atau 'q' untuk keluar
    key = cv2.waitKey(1)
    if key == ord("s"):
        img_name = os.path.join(save_path, f"image_{count}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Gambar {img_name} disimpan!")
        count += 1
    elif key == ord("q"):
        break

# Release kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()
