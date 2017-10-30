from flask import Flask, request ,jsonify,abort
import os
from baidu import baiduaip
import json
import base64


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/readme', methods=['GET'])
def readme():
    return '''
        <ur>
            <li><a href="/test">test</a></li>
        </ur>
        '''

@app.route('/test', methods=['GET'])
def test():
    print request
    print request.args
    print request.json
    print request.data
    print request.headers
    return jsonify({'task':tasks})

@app.route('/rest/1.0/face/v1/faceset/group/getlist',methods=['POST','GET'])
def getlist():
    options = {
        'start': 0,
        'num': 100,
    }
    return json.dumps(baiduaip.aipFace.getGroupList( options), ensure_ascii=False)

@app.route('/rest/1.0/face/v1/faceset/group/getusers', methods=['POST','GET'])
def getusers():
    options = {
        'start': 1,
        'num': 100,
    }
    groupid = request.args['groupid']
    return json.dumps(baiduaip.aipFace.getGroupUsers(groupid,options),ensure_ascii=False)

@app.route('/rest/1.0/face/v1/faceset/user/get', methods=['POST','GET'])
def getUser():
    options = {
        'start': 1,
        'num': 100,
    }
    uid = request.args['uid']
    if 'group_id' in request.args:
        groupid = request.args['group_id']
        return json.dumps(baiduaip.aipFace.getUser(uid,groupid),ensure_ascii=False)
    return json.dumps(baiduaip.aipFace.getUser(uid),ensure_ascii=False)

UPLOAD_FOLDER = './'
@app.route('/rest/1.0/face/v1/identify',methods=['POST'])
def identify():
    if not request.json:
        abort(400)

    options = {
        'user_top_num': 10,
        'face_top_num': 10,
    }

    # print 'requst-------' + request
    #  print request.values
    # print request.headers
    #print request.json
    print request.json
    groupid = request.json['group_id']
    filename = request.json['filename']
    imagedata = request.json['imagedata']

    '''
    file = open(filename,'wb')
    file.write(base64.b64decode(imagedata))
    file.flush()
    file.close()
    '''

    print 'groupid : ' + groupid
    print 'filename : ' + filename

    return json.dumps(baiduaip.aipFace.identifyUser(groupid,base64.b64decode(imagedata),options),ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0')