from HttpServer import HttpServerApp

app = HttpServerApp()

if __name__ == '__main__':
    app.run(host='192.168.4.94', port = 5000,threaded=True)#
