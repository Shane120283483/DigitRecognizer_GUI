#!/usr/bin/python
# -*- coding:utf-8 -*-

import struct
import numpy as np
import PIL.Image

'''解析测试标签后得到数字并保存在解析的图片文件名中'''


def getTestLabels():
    f1 = open("mnist_data/t10k-labels.idx1-ubyte", 'rb')
    buf1 = f1.read()
    f1.close()
    index = 0
    magic, num = struct.unpack_from(">II", buf1, 0)
    index += struct.calcsize('>II')
    labs = []
    labs = struct.unpack_from('>' + str(num) + 'B', buf1, index)
    return labs


filename = 'mnist_data/t10k-images.idx3-ubyte'
binfile = open(filename, 'rb')
buf = binfile.read()
index = 0
magic, numImages, numRows, numColumns = struct.unpack_from('>IIII', buf, index)
index += struct.calcsize('>IIII')
for image in range(0, numImages):
    im = struct.unpack_from('>784B', buf, index)
    index += struct.calcsize('>784B')
    im = np.array(im, dtype='uint8')
    im = im.reshape(28, 28)
    im = PIL.Image.fromarray(im)
    label = getTestLabels()
    imagenumber = label[image]
    im.save('mnist_test/%s_test_%s.bmp' % (imagenumber, image), 'bmp')
