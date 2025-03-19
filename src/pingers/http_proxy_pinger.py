import pycurl
from io import BytesIO

def ping (address, port, http_proxy, stat):
  output = BytesIO()
  url='http://'+str(address)+':'+str(port)

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, http_proxy)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
  query.setopt(pycurl.HEADER, 1)
  query.setopt(pycurl.NOBODY, 1)
  query.setopt(pycurl.CONNECTTIMEOUT, 1)
  query.setopt(pycurl.WRITEDATA, output)
  query.perform()

#  print('Status: %d' % query.getinfo(query.RESPONSE_CODE))
#  print('Time: %f' % query.getinfo(query.TOTAL_TIME))
  
  resp = query.getinfo(query.RESPONSE_CODE)
  ping = int(query.getinfo(query.TOTAL_TIME)*1000)

  query.close()
  is_alive = True
  
  if ( stat == 1 ) and ( ping > 0 ):
    ping = 0

  if (resp > 300):
    ping = -1
    is_alive = False

  return {
    "ping": ping,
    "is_alive": is_alive
  }
