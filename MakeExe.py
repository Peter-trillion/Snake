'''
作者: Peter
日期: 2021-08-14 22:28:41
最后一次编辑时间: 2021-08-16 21:10:35
简介: 用于将代码编译为程序
路径: \Snake\MakeExe.py
'''
import os
os.system('pyinstaller main.py -w -n 贪吃蛇1.1 -i ico\\icon.ico')