# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request, redirect, url_for
from .views.account import account as account_blueprint
from .views.home import home as home_blueprint
from .views.movies_show import movie as movies_blueprint

def HttpServerApp():
    app = Flask(__name__)
    app.register_blueprint(account_blueprint, url_prefix='/manage')
    app.register_blueprint(home_blueprint)
    app.register_blueprint(movies_blueprint)
    app.config.from_object('settings.BasicConfig')
    app.config["DEBUG"] = True
    @app.before_request
    def check():
        if (not session.get('user') and not request.path.startswith('/static')
                and request.path != '/manage/login'):
            return redirect(url_for('account.login'))

    @app.template_filter("split_path")
    def split_path(path):
        path_list = path.split('/')
        path_list = [[path_list[i - 1], '/'.join(path_list[:i])] for i in range(1, len(path_list)+1)]
        return path_list

    @app.errorhandler(404)
    def error(error_no):
        return redirect(url_for('account.home'))

    return app
