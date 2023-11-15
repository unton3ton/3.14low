Внедряем сообщение в коэффициенты дискретного косинус преобразования изображения


original:  
![](https://raw.githubusercontent.com/unton3ton/3.14low/main/trivial_DCT_WM/amelieOrigin.png)


Изменяем коэффициенты:  
imF[0][0] += 100000000  
imF[0][1] += 1  
imF[0][2] += 100 


DCT:  
![](https://raw.githubusercontent.com/unton3ton/3.14low/main/trivial_DCT_WM/DCT_crop_hightKoeff.png)


Результат:  
![](https://raw.githubusercontent.com/unton3ton/3.14low/main/trivial_DCT_WM/amelieWMhightKoeff.png)

md5sum:  
cc9f3d023a03732216e199484122dc19  amelieOrigin.png  
1347bcd0a3ebddb8e3d49e9770449375  amelieWMhightKoeff.png


compare:  
![](https://raw.githubusercontent.com/unton3ton/3.14low/main/trivial_DCT_WM/diffHK.png)


## Sources

* [Как применить DCT к изображению в Python?](https://questu.ru/questions/7110899/)
* [Простыми словами о преобразовании Фурье](https://habr.com/ru/articles/196374/)
* [scipy.fftpack.dct](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html)
* [Implementing Discrete Cosine Transform Using Python](https://tesfagabir.github.io/2016/12/04/Implementing-Discrete-Cosine-Transform-Using-Python.html)
* [Как обрезать часть изображения в Python (библиотека Pillow)](https://python-scripts.com/pillow-crop)
* [Image Resizing in Python explained](https://imagekit.io/blog/image-resizing-in-python/)
* [Numpy → Python implements two-dimensional DCT, IDCT transformation](https://www.programmersought.com/article/669010343179/)
