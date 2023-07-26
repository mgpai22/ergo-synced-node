import ipaddress
import socket


def splitIP(ipAddr: str) -> str:
    ip, separator, port = ipAddr.rpartition(':')
    assert separator  # separator (`:`) must be present
    port = int(port)  # convert to integer
    ip = ipaddress.ip_address(ip.strip("[]"))  # convert to `IPv4Address` or `IPv6Address`
    return ip


def ip_address_isIPV4(ip_with_port: str) -> bool:
    try:
        ip, port = ip_with_port.split(':')
        port = int(port)
        if not (1 <= port <= 65535):
            return False
    except ValueError:
        return False

    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        pass
    try:
        ipaddress.IPv6Address(ip)
        return False
    except ipaddress.AddressValueError:
        pass

    return False


def portCheck(ip: str, port: int) -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    result = sock.connect_ex((ip, port))
    if result == 0:
        sock.close()
        return 'open'
    else:
        sock.close()
        return 'close'
