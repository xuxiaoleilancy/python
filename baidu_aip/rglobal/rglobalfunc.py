import base64
import rglobalvalues
import os
import io
from os import path

def get_suirui_info(userid):
    if rglobalvalues.suirui_infos.has_key(userid):
        return rglobalvalues.suirui_infos[userid]
    else:
        return 'not find this user'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_file_content_base64(filePath):
    with open(filePath,'rb') as fp:
        return base64.b64encode(fp.read())

def get_src_iamge_abs_path(uid):
    return os.path.split(os.path.realpath(__file__))[0] + '\\files\\src_img\\' + uid + ".jpg"

def get_head_iamge_abs_path(uid):
    return os.path.split(os.path.realpath(__file__))[0] + '\\files\\result_img\\'  + "head_" + uid + ".png"

def get_default_head_iamge_abs_path():
    return os.path.split(os.path.realpath(__file__))[0] + '\\files\\result_img\\default\\head.png'