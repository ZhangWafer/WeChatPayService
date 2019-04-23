from gevent.pywsgi import WSGIServer
from FlaskApp import app

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 7000), app,keyfile='server.key',certfile='server.crt')
    http_server.serve_forever()


    # app.run(host='0.0.0.0', port=80, debug=True)
