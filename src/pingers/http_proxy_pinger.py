import pycurl
import io

def ping (address, port, http_proxy):
  output = io.BytesIO()
  url='http://'+address+':'+port

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, http_proxy)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
#    return output.getvalue()
    print(output.getvalue())
  except pycurl.error as exc:
#    return "Unable to reach %s (%s)" % (url, exc)
    print("Unable to reach %s (%s)" % (url, exc))
  query.close()

  ping = 10
  is_alive = True

  if ping == None:
    ping = -1
    is_alive = False

  return {
    "ping": ping,
    "is_alive": is_alive
  }
