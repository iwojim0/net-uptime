import subprocess

def ping (address, port, socks_proxy):
    ping = subprocess.run(['/net-uptime/src/pingers/test.sh', str(address), str(port), str(socks_proxy)], capture_output=True, text=True)
    is_alive = True                                                                                                                      
                                                                                
    if ping == None:
        ping = -1   
        is_alive = False
                        
    return {            
        "ping": int(float(ping.stdout)),
        "is_alive": is_alive            
    }
