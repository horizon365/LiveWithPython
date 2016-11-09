# -*- coding: UTF-8 -*-
import os,re

def Rrename(Path):
    ''' Path路径末尾需加/,涉及修改的文件名包括子目录，返回修改前改目录所有的文件名'''
    lista = []
    for item in os.listdir(Path):
        if os.path.isdir(Path+item):  # 例外情况最好放前面
            Rrename(Path+item+'/')   # 文件夹的末尾没有/
        else:
            lista.append(item)
            try:
                newitem = re.match(r'([\[\【].*[\】\]])(.*)',item).group(2)
                os.rename(Path+item,Path+newitem)
            except AttributeError:
                pass
    return lista
