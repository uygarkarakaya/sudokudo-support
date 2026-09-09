from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory='dist',**kwargs)
 def do_GET(self):
  route=urlsplit(self.path).path
  if route in ['/privacy','/support']:self.path=route+'.html'
  if route not in ['/privacy','/support','/'] and not Path('dist'+route).is_file():
   self.send_response(404)
   self.send_header('Content-Type','text/html; charset=utf-8')
   self.end_headers()
   self.wfile.write(Path('dist/404.html').read_bytes())
   return
  super().do_GET()
ThreadingHTTPServer(('127.0.0.1',4173),Handler).serve_forever()
