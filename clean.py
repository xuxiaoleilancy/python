# -*- coding: utf-8 -*-

import string
import os
import os.path
import sys
import shutil

rootdir = "../../"
print(os.path.abspath(rootdir))

for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:

        #删除所有的 debug release tmp目录
        if (dirname.__eq__("debug") or dirname.__eq__("release") or dirname.__eq__("tmp")):
            shutil.rmtree(os.path.join(parent,dirname))
            print("remove dir:" + os.path.join(parent, dirname))

    for filename in filenames:
        #删除 sln sdf suo vcxproj vcxproj.filters 文件
        if (filename.endswith("sln") or filename.endswith("sdf")
            or filename.endswith("suo") or filename.endswith("vcxproj")
            or filename.endswith("vcxproj.filters")):
            os.remove(os.path.join(parent, filename))
            print("cur dir is:" + parent)
            print("remove file:" + filename)
            #print("the full name of the file is:" + os.path.join(parent, filename))