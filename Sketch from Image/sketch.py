import numpy as np
import cv2
import scipy.ndimage
import imageio

img="photo.jpg"
s=imageio.imread(img)

#converts rgb image to grayscale
def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def dodge(front,back):
    result = front*255/(255-back)
    result[result>255] = 255
    result[back==255] = 255
    return result.astype('uint8')


g = grayscale(s)
i = 255-g

b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r = dodge(b,g)
cv2.imwrite('sketch.png',r)