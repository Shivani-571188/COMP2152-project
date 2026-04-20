import socket

target = "telnet.0x10.cloud"
port = 2323

print("Checking Telnet port...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

result = sock.connect_ex((target, port))

if result == 0:
    print("\n[!] VULNERABILITY FOUND")
    print("Telnet port is OPEN.")
    print("Passwords are sent in plain text.")
else:
    print("\n[OK] Port is closed.")

sock.close()