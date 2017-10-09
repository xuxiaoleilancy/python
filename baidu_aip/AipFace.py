from aip import AipFace
from aip import AipOcr

import cv2 as cv
import json

APP_ID = '10214255'
API_KEY = '2CctZ90VVHrPyiHgWkIChYSF'
SECRET_KEY = '4zfBt6RL1M6iR6bxRZCbdSONG9VlaBjS'

aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

isFront = True

options = {
    'detect_direction': False,
    'accuracy': 'high'
}

idcard_file = 'idcard_front.png'
front_result = aipOcr.idcard(get_file_content(idcard_file), isFront)
print json.dumps(front_result, encoding="UTF-8", ensure_ascii=False)

idcard_file = 'idcard.png'
result = aipOcr.idcard(get_file_content(idcard_file),False)
print json.dumps(result,encoding="UTF-8", ensure_ascii=False)

result = aipOcr.bankcard(get_file_content('bankcard.png'))
print json.dumps(result,encoding="UTF-8", ensure_ascii=False)

result = aipOcr.basicGeneral(get_file_content('general.png'))
print json.dumps(result,encoding="UTF-8", ensure_ascii=False)

'''
img_idcard = cv.imread(idcard_file)
cv.imshow('idcard',img_idcard)

'''
print '*************************************************************************'

'''
aipFace.deleteGroupUser('stars','huge')
add_result = aipFace.addUser(
            'huge',
            'huge',
            'stars',
            get_file_content('huge.jpg')
            )
print 'huge result---------------------------------------------------'
print add_result
print aipFace.getUser('huge')

aipFace.deleteGroupUser('stars','liutao')
add_result = aipFace.addUser(
            'liutao',
            'liutao',
            'stars',
            get_file_content('liutao.jpg')
            )
print 'liutao result---------------------------------------------------'
print add_result
print aipFace.getUser('liutao')

print 'masu result---------------------------------------------------'
print aipFace.getUser('masu')
'''

print 'group stars result---------------------------------------------------'
print aipFace.getGroupUsers('stars')

options = {
      'user_top_num': 10,
        'face_top_num': 10,
    }
identify_result =  aipFace.identifyUser('stars',get_file_content('face.jpg'))


#'''
options = {
    'max_face_num': 1000,
    'face_fields': "age,beauty,expression,faceshape,gender,race,qualities,landmark",
}

src_image = 'timg.jpg'
result = aipFace.detect(get_file_content(src_image),options)

print result

print result['result_num']

match_result = aipFace.match([
        get_file_content('face.jpg'),
        get_file_content('liutao.jpg'),
        get_file_content('huge.jpg'),
    ])


print '-------------------------------------'
print match_result
print '-------------------------------------'


img = cv.imread(src_image)
green = (0,255,0)
font = cv.FONT_HERSHEY_SIMPLEX

for i in range(0,result['result_num']):
    print result['result'][i]['landmark']
    print result['result'][i]['location']
    location = result['result'][i]['location']
    x = location['left']
    y = location['top']
    w = location['width']
    h = location['height']
    cv.rectangle(img,(x,y),(x+w,y+h),green)
    cv.putText(img, result['result'][i]['gender'][0], (x , y - 5 ),font ,0.7 , (0,255,255))
    cv.putText(img, str(int(result['result'][i]['age'])), (x, y - 25), font, 0.7, (0, 255, 255))
    cv.putText(img, result['result'][i]['race'][0], (x , y - 50 ),font ,0.7 , (0,255,255))

cv.imwrite("face_result.jpg",img)

img_src = cv.imread(src_image)
cv.imshow('src',img_src)
img_result = cv.imread("face_result.jpg")
cv.imshow('dest',img_result)
cv.waitKey(0)
cv.destoryAllWindows()
#'''

