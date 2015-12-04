#!/usr/bin/python
# coding: utf-8
from flask import Flask
import json,os,shutil
from flask import request

django_host="192.168.1.111"
django_user="wangx"
django_password="******"
scpFile_path="/home/wangx/Documents/flask_tutorial/scpFile"

app = Flask(__name__)


# 上传文件
@app.route('/file/v1/upload', methods=["POST"])
def upload_file():
    print('请求')
    # 直接
    # data = request.form['data']
    data =request.files['test.txt']
    return 'success'
    filename = request.headers['filename']
    # filename = request.form['filename']
    print filename
    # print filename.decode('utf-8')
    print type(filename)
    # filename = request.form['filename']
    file = open(filename.encode('utf-8'),'wb')
    file.write(data)
    file.close()
    return 'success'


# 传输文件
@app.route('/file/v1/get', methods=["GET"])
def get_file():
    path = request.args['path']
    print(path)
    text = open(path,'rb').read()
    return text
# 删除文件
@app.route('/file/v1/delete',methods=["POST"])
def delete_file():
    file_path = request.json['file_path']
    print file_path
    os_result = os.remove(file_path)
    print('删除文件的结果是')
    print(os_result)
    if os_result == None:
        print('删除成功')
        return 'success'
    else:
        return os_result
@app.route('/file/v1/rename',methods=["POST"])
def rename_file():
    file_path = request.json['file_path']
    new_path = request.json['destination']
    command = "mv {0} {1}".format(file_path,new_path)
    print(command)
    os_result = os.rename(file_path, new_path)
    print('删除文件的结果是')
    print(os_result)
    if os_result == None:
        print('删除成功')
        return 'success'
    else:
        return os_result
@app.route('/file/v1/copy', methods=["POST"])
def copy_file():
    file_path = request.json['file_path']
    new_path = request.json['new_path']
    os_result = shutil.copy(file_path,new_path)
    if os_result == None:
        print('复制成功')
        return 'success'
    else:
        return os_result

# 创建目录
@app.route('/dir/v1/create',methods=["POST"])
def create_dir():
    file_path = request.json['dir_path']
    os_result = os.mkdir(file_path)
    print('删除目录的结果是')
    if os_result == None:
        print('删除成功')
        return 'success'
    else:
        return os_result
# 删除目录
@app.route('/dir/v1/delete',methods=["POST"])
def delete_dir():
    file_path = request.json['dir_path']
    os_result = shutil.rmtree(file_path)
    print('删除目录的结果是')
    if os_result == None:
        print('删除成功')
        return 'success'
    else:
        return os_result
# 重命名目录
@app.route('/dir/v1/rename',methods=["POST"])
def rename_dir():
    file_path = request.json['file_path']
    new_path = request.json['destination']
    command = "mv {0} {1}".format(file_path,new_path)
    print(command)
    os_result = os.rename(file_path, new_path)
    print('重命名目录的结果是')
    print(os_result)
    if os_result == None:
        print('删除成功')
        return 'success'
    else:
        return os_result
# 复制目录
@app.route('/dir/v1/copy', methods=["POST"])
def copy_dir():
    file_path = request.json['file_path']
    new_path = request.json['new_path']
    os_result = shutil.copytree(file_path,new_path)
    if os_result == None:
        print('复制成功')
        return 'success'
    else:
        return os_result

@app.route('/')
def index():
    return "Hello<form method='POST' action='/file/v1/upload'><input type='file' name='data'/><input type='submit' value='click me'/></form>"
    return "Hello<a href='/file/get' download='wangx.txt'>click me</a>"
    return "<a href='/file/get/'></a>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
