import socket

print("Basic Network Security Tool")
print("----------------------------")

target = "127.0.0.1"

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389]

print("Checking common ports on your computer...")
print()

for port in ports: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
       print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()

print()
print("Scan complete.")