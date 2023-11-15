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
