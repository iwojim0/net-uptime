import subprocess

def ping (address, port, socks_proxy):
    ping = subprocess.check_call(['/net-uptime/src/pingers/test.sh', address, port, socks_proxy])
    is_alive = True

    if ping == None:
        ping = -1
        is_alive = False

    return {
        "ping": int(float(ping)),
        "is_alive": is_alive
    }
