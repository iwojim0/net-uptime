import subprocess

def ping (address, port, socks_proxy):
    ping_socat = subprocess.run(['/net-uptime/src/pingers/test.sh', str(address), str(port), str(socks_proxy)], capture_output=True, text=True)
    ping=ping_socat.stdout
    is_alive = True                                                                                                                      

    if int(ping) == -1:
        is_alive = False
                        
    return {            
        "ping": ping,
        "is_alive": is_alive            
    }
