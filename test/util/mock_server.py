from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from functools import partial
from os.path import abspath


def run_server(directory=".", port=0):
    hostname = "localhost"
    directory = abspath(directory)
    handler = partial(SimpleHTTPRequestHandler, directory=directory)
    httpd = HTTPServer((hostname, port), handler, False)

    httpd.server_bind()
    address = "http://%s:%d" % (hostname, httpd.server_port)
    httpd.server_activate()

    def serve_forever(httpd):
        with httpd:
            httpd.serve_forever()

    thread = Thread(target=serve_forever, args=(httpd, ))
    thread.daemon = True
    thread.start()

    return httpd, address
