# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18bOUfObgZi3DnpaerSOaSxyMWusuaZK0
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("download (2).jpg")
rasm2=cv2.imread("download.jpg")
rasm3=cv2.imread("de91778a8901cff99fff7024b892a5bc.jpg")
rasm4=cv2.imread("Screenshot 2024-01-29 231703.png")
rasm5=cv2.imread("Screenshot 2024-01-24 181852.png")
cv2_imshow(rasm)
cv2_imshow(rasm2)
cv2_imshow(rasm3)
cv2_imshow(rasm4)
cv2_imshow(rasm5)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm5,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)