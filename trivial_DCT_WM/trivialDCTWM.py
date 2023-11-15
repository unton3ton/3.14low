# python3 -m venv DISCRETE
# source DISCRETE/bin/activate
# pip install --upgrade pip

# pip install scikit-image


from scipy.fftpack import dct, idct

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')    

from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

# read RGB image and convert to grayscale
im = rgb2gray(imread('amelie.jpg')) 

imF = dct2(im)


# print('len =', len(imF), '\n') # 736

# for i in range(5):
#     print(imF[700][i])
# print('\n')

# print(imF[700][0], '\n')

# imF[700][0] += 101

# print(imF[700][0], '\n')

# for i in range(5):
#     print(imF[700][i])
# print('\n')

# $ md5sum amelieOrigin.png amelieWM101.png 
# cc9f3d023a03732216e199484122dc19  amelieOrigin.png
# 6e01ba79e131dd6498a72121a654aa8b  amelieWM101.png

# for i in range(5):
#     print(imF[0][i])
# print('\n')

# print(imF[0][0], '\n')

# imF[0][0] += 100000000
# imF[0][1] += 1
# imF[0][2] += 100

# print(imF[0][0], '\n')

# for i in range(5):
#     print(imF[0][i])
# print('\n')

# $ md5sum amelieOrigin.png amelieWM.png 
# cc9f3d023a03732216e199484122dc19  amelieOrigin.png
# 1347bcd0a3ebddb8e3d49e9770449375  amelieWM.png


# for i in range(5):
#     print(imF[0][i])
# print('\n')

# print(imF[0][0], '\n')

# imF[0][0] += 100_000_000

# print(imF[0][0], '\n')

# for i in range(5):
#     print(imF[0][i])
# print('\n')

# $ md5sum amelieOrigin.png amelieWM_100_000_000.png 
# cc9f3d023a03732216e199484122dc19  amelieOrigin.png
# cc9f3d023a03732216e199484122dc19  amelieWM_100_000_000.png


# for i in range(10):
#     print(imF[0][i])
# print('\n')

# imF[0][0] += 100
# imF[0][2] += 1
# # imF[0][5] += 1
# # imF[0][7] += 0.1
# # imF[0][8] += 0.01

# for i in range(10):
#     print(imF[0][i])
# print('\n')

# $ compare amelieOrigin.png amelieWMhightKoeff.png diffHK.png
# $ md5sum amelieOrigin.png amelieWMhightKoeff.png 
# cc9f3d023a03732216e199484122dc19  amelieOrigin.png
# e654aeedefaa94b1e63dca47afee6426  amelieWMhightKoeff.png





for i in range(5):
    print(imF[0][i])
print('\n')

# 430.1794838475065
# -1.3544250429445963
# 141.63742589274676
# -49.464077873776034
# -23.52892789835101


print(imF[0][0], '\n')

imF[0][0] = 10_001_001_010 # передаваемое сообщение

print(imF[0][0], '\n')

for i in range(5):
    print(imF[0][i])
print('\n')

# 10001001010.0
# -1.3544250429445963
# 141.63742589274676
# -49.464077873776034
# -23.52892789835101


# $ md5sum amelieOrigin.png amelieWMoneLine.png 
# cc9f3d023a03732216e199484122dc19  amelieOrigin.png
# cc9f3d023a03732216e199484122dc19  amelieWMoneLine.png
# $ compare amelieOrigin.png amelieWMoneLine.png diffOneLine.png

im1 = idct2(imF)




imF1 = dct2(im1)
print(imF1[0][0])
print('\n')

# 10001001010.000004
# -1.3544250575394108
# 141.63742582173015
# -49.464077868828014
# -23.52892787817697


# check if the reconstructed image is nearly equal to the original image
np.allclose(im, im1)
# True

# plot original and reconstructed images with matplotlib.pylab
plt.gray()
# plt.subplot(311), plt.imshow(im), plt.axis('off'), plt.title('original image', size=10)
plt.subplot(211), plt.imshow(imF), plt.axis('off'), plt.title('DCT of image', size=10)
plt.subplot(212), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed image (DCT+IDCT)', size=10)
plt.show()

plt.imsave('amelieOrigin.png', im)
plt.imsave('amelieWMoneLine.png', im1) 
plt.imsave('DCT_10_001_001_010.png', imF)


# $ compare amelieOrigin.png amelieWM_100_000_000.png diff.png
# $ compare amelieOrigin.png amelieWM_100_000_000.png diff_100_000_000.png
# $ compare amelieOrigin.png amelieWM101.png diff_101.png
# $ compare amelieOrigin.png amelieWM.png diff.png


from PIL import Image
 
im = Image.open('DCT_10_001_001_010.png')
im_crop = im.crop((0, 0, 30, 30))
im_crop = im_crop.resize((400, 400))
im_crop.save('DCT_crop_10_001_001_010.png', quality=100)