import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


st.title('Aula do dia 16/04')

image = Image.open('peppers.png')

imagem_color_arr = np.array(image)

img_gray = np.mean(imagem_color_arr, axis=2)

st.text(img_gray.shape)

# limiar = st.slider('Limiar?', 0, 255, 25)

# st.text(limiar)

img_gray = np.mean(imagem_color_arr, axis=2)

num_color = st.selectbox("Quantas cores?", \
    (2, 4, 8, 16, 32, 64, 128))

# st.text(num_color)
# img_gray[img_gray != limiar] = 255
if num_color == 2:
    img_gray[img_gray < 127]  = 0
    img_gray[img_gray >= 127]  = 255

elif num_color == 4:
    img_gray[img_gray < 64]  = 0
    img_gray[(64 < img_gray) & (img_gray < 128)]  = 64
    img_gray[(128 < img_gray) & (img_gray < 192)]  = 128
    img_gray[img_gray > 192]  = 192

elif num_color == 8:
     img_gray[img_gray < 32] = 0
     img_gray[(32 < img_gray) & (img_gray < 64)] = 32
     img_gray[(64 < img_gray) & (img_gray < 96)] = 64
     img_gray[(96 < img_gray) & (img_gray < 128)] = 128
     img_gray[(128 < img_gray) & (img_gray < 160)] = 160
     img_gray[(160 < img_gray) & (img_gray < 192)] = 192
     img_gray[(192 < img_gray) & (img_gray < 224)] = 224
     img_gray[img_gray > 224] = 255

elif num_color == 16:
    aux = (255 // num_color) + 1
    aux1 = 12
    for i in range(num_color):
        if (i == 0):
            img_gray[img_gray < aux] = 0
        elif (i == num_color - 1):
            img_gray[img_gray > (255 - aux1)] = 255
        else:
            img_gray[(aux < img_gray) & (img_gray < aux + aux1)] = aux
            aux = aux + aux1
elif num_color == 32:
     aux = (255 // num_color) + 1
     aux1 = 8
     for i in range(num_color):
        if (i == 0):
            img_gray[img_gray < aux] = 0
        elif (i == num_color - 1):
            img_gray[img_gray > (255 - aux1)] = 255
        else:
            img_gray[(aux < img_gray) & (img_gray < aux + aux1)] = aux
            aux = aux + aux1

elif num_color == 64:
     aux = (255 // num_color) + 1
     aux1 = 4
     for i in range(num_color):
        if (i == 0):
            img_gray[img_gray < aux] = 0
        elif (i == num_color - 1):
            img_gray[img_gray > (255 - aux1)] = 255
        else:
            img_gray[(aux < img_gray) & (img_gray < aux + aux1)] = aux
            aux = aux + aux1

elif num_color == 128:
     aux = (255 // num_color) + 1
     aux1 = 2
     for i in range(num_color):
        if (i == 0):
            img_gray[img_gray < aux] = 0
        elif (i == num_color - 1):
            img_gray[img_gray > (255 - aux1)] = 255
        else:
            img_gray[(aux < img_gray) & (img_gray < aux + aux1)] = aux
            aux = aux + aux1
else:
    img_gray[img_gray < 32] = 0
    img_gray[(32 < img_gray) & (img_gray < 64)] = 32
    img_gray[(64 < img_gray) & (img_gray < 96)] = 64
    img_gray[(96 < img_gray) & (img_gray < 128)] = 128
    img_gray[(128 < img_gray) & (img_gray < 160)] = 160
    img_gray[(160 < img_gray) & (img_gray < 192)] = 192
    img_gray[(192 < img_gray) & (img_gray < 224)] = 224
    img_gray[img_gray > 224] = 255



# elif = 32, aux1 = 8; elif 64, aux1 = 4, elif 128, aux1 = 2

new_image = Image.fromarray(img_gray)

# plt.axis('off')
# plt.imshow(new_image)
# plt.show()
# st.pyplot()

st.image([new_image.convert("L"), image], caption=['Cinza', 'colorida'], width=480,) 
# st.image(image, caption='Colorida', width=320,)