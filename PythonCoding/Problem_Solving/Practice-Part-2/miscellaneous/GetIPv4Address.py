import socket

def get_ipv4_address():
    # Get system hostname
    hostname = socket.gethostname()
    print(hostname)
    ipv4_address = socket.gethostbyname(hostname) # Resolve to IPv4
    return ipv4_address

print(get_ipv4_address())


