# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
        @Author yuxiankai
        @Date 2022/3/9 4:47 下午
        @Describe 
        @Version 1.0
    """
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World 8081'

@app.route('/vod')
def vod():
    return "8081 - vod"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)