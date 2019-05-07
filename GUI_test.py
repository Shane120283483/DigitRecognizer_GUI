#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import os
from PIL import Image
from model2 import test


class my_frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 300))
        self.Show(True)

        splitter = wx.SplitterWindow(self, size=(500, 300))
        panel1 = wx.Panel(splitter, size=(250, 300))
        panel2 = wx.Panel(splitter, size=(250, 300))
        splitter.SplitVertically(panel1, panel2)

        b1 = wx.Button(panel1, label="选择识别图片", size=(250, 300))
        b1.Bind(wx.EVT_BUTTON, self.on_open)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(panel2, style=wx.TE_MULTILINE, size=(250, 300))
        vbox2.Add(self.text, 1, flag=wx.ALL | wx.EXPAND, border=10)
        panel2.SetSizer(vbox2)

    def on_open(self, e):
        dlg = wx.FileDialog(self, u"请选择一个图片", 'mnist_test', "", "*.*", wx.FD_OPEN)
        # 调用一个函数打开对话框
        if dlg.ShowModal() == wx.ID_OK:
            im = Image.open(dlg.GetPath())
            im.show()
            path = dlg.GetPath()
            test_sample = path.split("\\")[-1]
            result = test(test_sample)
            self.text.AppendText(u"识别结果："+result+'\n')
            if result == test_sample[0]:
                self.text.AppendText(u"根据标签判断识别结果：" + u"正确"+'\n')
            elif result != test_sample[0]:
                self.text.AppendText(u"根据标签判断识别结果：" + u"错误"+'\n')
            dlg.Destroy()


app = wx.App()
frame = my_frame(None, '手写数字识别')
app.MainLoop()
