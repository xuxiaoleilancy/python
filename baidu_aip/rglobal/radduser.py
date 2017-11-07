
from baidu import baiduaip
import rglobalfunc

def add_user(uid):
    add_result = baiduaip.aipFace.addUser(
        uid,
        uid,
        'suirui',
        rglobalfunc.get_file_content(rglobalfunc.get_src_iamge_abs_path(uid))
    )
    return add_result

add_uid = 'jiangsheng'
print baiduaip.aipFace.getUser('jinshaobo')
print baiduaip.aipFace.getUser('tianlijun')

'''
print add_user('fengwenlan')
print baiduaip.aipFace.getUser('fengwenlan')

upload_uid = 'shiyingle'
baiduaip.aipFace.deleteGroupUser('suirui',upload_uid)
print baiduaip.aipFace.getUser(upload_uid)

add_user(upload_uid)

print baiduaip.aipFace.getUser(upload_uid)
'''