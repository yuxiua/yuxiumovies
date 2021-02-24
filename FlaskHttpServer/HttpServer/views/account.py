# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify,current_app

account = Blueprint('account', __name__)


@account.route('/')
def home():
    return redirect(url_for('account.login'))


@account.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('account.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'yuxiu' and pwd == '123':
            current_app.config['BASEDIR'] = r'D:\Web相关\FlaskHttpServer\HttpServer\static\movies'
            session['user'] = user
            return jsonify({"code": 200, "error": ""})
        if user == 'admin' and pwd == '123':
            current_app.config['BASEDIR'] = r'D:\\'
            session['user'] = user
            return jsonify({"code": 200, "error": ""})
        else:
            return jsonify({"code": 401, "error": "用户名或密码错误"})


@account.route('/logout')
def logout():
    del session['user']
    return redirect(url_for('account.login'))

