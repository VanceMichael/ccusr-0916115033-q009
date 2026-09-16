import os
from wsgiref.simple_server import make_server
from .db import upgrade
def app(env,start):
 if env.get('PATH_INFO')!='/health': start('404 Not Found',[]); return [b'']
 body=b'{"status":"ok"}'; start('200 OK',[('Content-Type','application/json')]); return [body]
if __name__=='__main__': upgrade(); make_server('',int(os.environ.get('PORT','8080')),app).serve_forever()
