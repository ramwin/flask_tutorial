#!/usr/bin/python
# coding: utf-8
from flask import Flask
import json
from flask import request

django_host="192.168.1.111"
django_user="wangx"
django_password="******"
scpFile_path="/home/wangx/Documents/flask_tutorial/scpFile"

app = Flask(__name__)

def readFile(fn,buf_size=262144):
    f = open(fn,"rb")
    while True:
        c = f.read(buf_size)
        if c:
            yield c
        else:
            break
    f.close()

# 传输文件
@app.route('/file/get', methods=["GET"])
def get_file():
    # 获取传递的参数
    # file_path = request.json["file_path"]
    # return readFile(file_path)
    text = open('./123.png','rb').read()
    return text
    # 原来想用scp的，但是一想，我要不直接就读取数据传递得了
    # store_path = request.json["store_path"]
    # try:    # 执行命令
    #     command = "{scpFile_path} {file_path} {django_user} {django_password} {store_path}".format{
    #         scpFile_path: scpFile_path,
    #         file_path: file_path,
    #         django_user: django_user,
    #         django_password: django_password,
    

@app.route('/')
def index():
    return "Hello<a href='/file/get' download='wangx.txt'>click me</a>"
    return "<a href='/file/get/'></a>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
