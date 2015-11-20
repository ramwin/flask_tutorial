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
@app.route('/file', methods=["GET"])
def get_file():
    path = request.args['path']
    text = open(path,'rb').read()
    return text

@app.route('/')
def index():
    return "Hello<a href='/file/get' download='wangx.txt'>click me</a>"
    return "<a href='/file/get/'></a>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
