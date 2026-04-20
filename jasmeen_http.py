import urllib.request

target = "http://blog.0x10.cloud/"

print("Checking for directory listing...")

try:
    response = urllib.request.urlopen(target, timeout=5)
    content = response.read().decode().lower()

    if "index of" in content:
        print("\n[!] VULNERABILITY FOUND")
        print("Directory listing is enabled.")
    else:
        print("\n[OK] No directory listing.")

except Exception as e:
    print("Error:", e) 
    