import cv2
from tkinter.filedialog import *

photo = askopenfilename()
img = cv2.imread(photo)
img_color = img.copy()

# -- PASO 1 --
# downsample image using Gaussian pyramid
# Reducimos el ruido de la imagen usando la pirámide gaussianaz
for _ in range(5):
    img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

# -- PASO 2 --
# Convertimos la imagen a escala de grises
img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)

# -- PASO 3 --
# Aplicamos un desenfoque mediano
img_blur = cv2.medianBlur(img_gray, 7)

# -- PASO 4 --
# Detectamos y mejoramos los bordes
img_edge = cv2.Canny(img_blur, 30, 120)
img_edge = cv2.bitwise_not(img_edge)
# img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# -- PASO 5 --
# Convertimos de nuevo a color para que pueda ser bit-AND con la imagen a color
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)


# -- PASO 5 --
# Combinamos las dos imágenes en una sola
# bitwise_and: calcula la combinación lógica bit a bit por elemento de dos matrices/escalares/imágenes
cartoon = cv2.bitwise_and(img_color, img_edge)



cv2.imshow("Image", img)
cv2.imshow("Media", img_color)
cv2.imshow("Cartoon", cartoon)
cv2.imshow("Edges", img_edge)
cv2.imshow("Blur", img_blur)
cv2.imshow("Gray", img_gray)

#save
cv2.imwrite("filtro.jpg", img_color)
cv2.imwrite("grey.jpg", img_gray)
cv2.imwrite("blur.jpg", img_blur)
cv2.imwrite("edges.jpg", img_edge)
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()