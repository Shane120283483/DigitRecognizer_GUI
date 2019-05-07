#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import os
from PIL import Image
import random
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.externals import joblib


'''将图片转换为向量'''


def image_vector(fname):
    im = Image.open("mnist_train/"+fname).convert('L')
    im = im.resize((28, 28))
    tmp = np.array(im)
    vector = tmp.ravel()           # 转换成1*784的向量
    return vector


def image_vector_2(fname):
    im = Image.open("mnist_test/"+fname).convert('L')
    im = im.resize((28, 28))
    tmp = np.array(im)
    vector = tmp.ravel()           # 转换成1*784的向量
    return vector


'''随机训练1000张图片'''


def split_data(paths):
    fn_list = os.listdir(paths)
    X = []
    y = []
    d0 = random.sample(fn_list, 1000)
    for i, name in enumerate(d0):
        y.append(name[0])  # 获取文件名的第一个字符，例如0_train_1.bmp,则得到数字标签0
        X.append(image_vector(name))  # 获取图片并利用函数转换为1*784向量
    return X, y


'''构建分类器'''


def knn_clf(X_train, y_train_label):
    classifier = knn()
    classifier.fit(X_train, y_train_label)
    return classifier


'''保存模型'''


def save_model(model, output_name):
    joblib.dump(model, output_name)


'''训练模型'''


X_train_1, y_train_label_1 = split_data("mnist_train")
clf = knn_clf(X_train_1, y_train_label_1)
save_model(clf, 'mnist_knn1000.m')


'''加载模型'''


def load_model(model):
    joblib.load(model)


'''获取测试集'''


def testdata(filename):
    X = []
    X.append(image_vector_2(filename))
    return X


'''测试模型'''


load_model('mnist_knn1000.m')
test_sample = "8_test_1170.bmp"
test_result = clf.predict(testdata(test_sample))
print(test_result)
if test_sample[0] == test_result[0]:
    print("Bingo")
else:
    print("Wrong")