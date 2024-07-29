
import cv2
import matplotlib.pyplot as plt

# Baca gambar menggunakan OpenCV
image = cv2.imread("coba.jpg")

# Ubah gambar menjadi abu-abu menggunakan OpenCV
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar abu-abu menggunakan Matplotlib
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()



