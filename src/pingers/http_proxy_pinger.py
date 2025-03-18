import pycurl
from io import BytesIO
import time

def ping (address, port, http_proxy):
  output = BytesIO()
  url='http://'+str(address)+':'+str(port)

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, http_proxy)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
  query.setopt(query.HEADER, 1)
  query.setopt(query.NOBODY, 1) # header only, no body
  t1=time.time_ns()
  query.perform()
  query.close()
  t2=time.time_ns()

  ping=int((t2-t1)/1000000)
  is_alive = True

  if ping == None:
    ping = -1
    is_alive = False

  return {
    "ping": ping,
    "is_alive": is_alive
  }
