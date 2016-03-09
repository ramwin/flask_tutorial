#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-02 14:57:02

from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/', method=["POST"])
def test():
    data = request.form['data']

