#/usr/bin/env python
# -*- coding: utf-8 -*-


def insertionsort(IN): # fonksiyon oluştutduk
    for i in range(1, len(IN)): # dizinin uzunluğu kadar döngüye soktuk
        key = IN[i] # anahtar olarak yani bakılacak sayı olarak dizinin 0 değil  1. indexsini aldık
        j = i - 1 # j dediğimiz şey 0. index oldu her döngüde 1 eksiği olmuş olcak :)
        while IN[j] > key and j >= 0: # j keyimizden büyükse ve j 0 dan büyük yada eşitse kaydırma yapcaz saten aksi olamaz sonsuz döngü olur :)
            IN[j+1] = IN[j] # j yi 1 arttırdık yani sonraki indexe geçtik
            j = j - 1 # daha sonra jden bir çıkardık sol taraf 0 dı en başında yani 1 eksiği solunda olmuş olucak
        IN[j+1] = key # son olarak en son keyimize son indexi gömdük


a = int(input("Kaç Sayı Sıralamak İstersiniz: ")) # kaç adet sayı sıralanaağını aldık
IN = [x for x in range(a)] # dizide sayı kadar yer açtık
for z in range(a): # sayıları girmesi için döngü başlattım
    IN[z] = int(input(str(z) + ". Sayıyı giriniz: ")) # sayıları istedim :)
insertionsort(IN) # dizimizi belirttim
print(IN) # yazdır :)