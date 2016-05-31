#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-04 11:43:05
import json, time, os, re
from flask import Flask
from flask import request
from flask import render_template
from functools import wraps
from flask import make_response
import requests
app = Flask(__name__)

class Log():
    def __init__(self,path):
        self.path = path
    def warning(self,text):
        print(text)
        self.files = open(self.path,'a')
        timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.files.write("[WARN][{time}] {text}\n".format(text=normal_str(text),time=timestr))
        self.files.close()
    def info(self,text):
        print(text)
        self.files = open(self.path,'a')
        timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.files.write("[INFO][{time}] {text}\n".format(text=normal_str(text),time=timestr))
        self.files.close()
    def error(self,text):
        print(text)
        self.files = open(self.path+'.err','a')
        timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        self.files.write("[ERR ][{time}] {text}\n".format(text=normal_str(text),time=timestr))
        self.files.close()

log = Log('./log/appapi.log')

# ---------------------------通用函数------------------
def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun
    
def normal_str(string):
    if isinstance(string, str):
        return string
    elif isinstance(string, unicode):
        return string.encode('utf-8')
        
# ---------------------------web请求-----------------
# 测试用
@app.route('/test/', methods=["GET"])
def test():
    return render_template('test.html')
@app.route('/test2/', methods=["POST"])
def test2():
    value = request.json['value'] # 获取到的是str
    text = '汉字{0}'.format(value)
    print(type(text))
    print(type('汉字'))
    return json.dumps({'status':'success'}),200


# ----------------------------zettage------------------
@app.route('/getall/v1.0/device/<device_id>/sensor/<sensor_id>/',methods=["GET"])
@allow_cross_domain
def getalldata(device_id, sensor_id):
    all_result = {
        'sensor_id': '26',
        'data': [
            ['2016-01-03 17:55:31','23'],
            ['2016-01-03 17:56:31','24'],
            ['2016-01-03 17:57:31','21'],
            ['2016-01-03 17:58:31','22'],
            ['2016-01-03 17:59:31','26'],
            ['2016-01-03 18:00:31','24'],
            ['2016-01-03 18:01:31','23'],
        ]
    }
    return json.dumps(all_result), 200
import sys
def magic(request):
    a= request
    while True:
        cmd = sys.stdin.readline()
        if not cmd:
            continue
        try:
            exec(cmd)
        except Exception as err:
            if isinstance(err, KeyboardInterrupt):
                break
            traceback.print_last()
from flask import render_template
@app.route('/index/', methods=["GET"])
def index():
    return render_template('index.html')
@app.route('/crossget/', methods=["GET","POST"])
@allow_cross_domain
def crosstest1(): # 跨域发送GET请求
    return '返回的数据', 200

@app.route('/postparams/', methods=["POST"])
@allow_cross_domain
def postparams(): # 跨域发送POST请求
    # print(dir(request))
    print('postparams')
    file = open('test','wb')
    text = request.data
    print(type(text))
    print(text)
    # for i in range(len(request.data)//2):
    #     text = chr(int(request.data[2*i:2*i+2],16))
    file.write(text)
    file.close()
    # print(request.get_data())
    # print(request.form['username']) 
    return 'postparams返回了数据', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=23759,debug=True)
