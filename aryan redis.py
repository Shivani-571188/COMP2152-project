import socket

target = "redis.0x10.cloud"
port = 6379

print("Checking Redis port...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

result = sock.connect_ex((target, port))

if result == 0:
    print("\n[!] VULNERABILITY FOUND")
    print("Redis port is OPEN.")
    print("Possible unauthorized access to data.")
else:
    print("\n[OK] Port is closed.")

sock.close()