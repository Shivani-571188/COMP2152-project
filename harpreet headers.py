import urllib.request

target = "http://api.0x10.cloud"

print("Checking headers...")

try:
    response = urllib.request.urlopen(target, timeout=5)
    headers = dict(response.headers)

    server = headers.get("Server")
    powered = headers.get("X-Powered-By")

    print("Server:", server)
    print("X-Powered-By:", powered)

    if server or powered:
        print("\n[!] VULNERABILITY FOUND")
        print("Server information is exposed.")
    else:
        print("\n[OK] No sensitive headers.")

except Exception as e:
    print("Error:", e)