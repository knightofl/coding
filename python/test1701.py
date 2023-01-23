import numpy as np
import sys, os
sys.path.append('./scratch1')
from dataset.mnist import load_mnist
from PIL import Image

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape, t_train.shape)
print(x_test.shape, t_test.shape)

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_train[0]
label = t_train[0]
print(img, img.shape)
print(label)

img = img.reshape(28, 28)
print(img, img.shape)
img_show(img)