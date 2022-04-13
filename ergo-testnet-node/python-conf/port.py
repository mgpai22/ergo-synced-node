import socket
from ipaddress import ip_address


def splitIP(ipAddr):
    ip, separator, port = ipAddr.rpartition(':')
    assert separator  # separator (`:`) must be present
    port = int(port)  # convert to integer
    ip = ip_address(ip.strip("[]"))  # convert to `IPv4Address` or `IPv6Address`
    return ip


def portCheck(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    result = sock.connect_ex((ip, port))
    if result == 0:
        sock.close()
        return 'open'
    else:
        sock.close()
        return 'close'
