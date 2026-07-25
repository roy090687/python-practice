import subprocess
import re

result = subprocess.run("ipconfig", capture_output=True, text=True)
print(result.stdout)
print(type(result.stdout))
ip_address = re.compile(r"IPv4.*?:\s*([\d.]+)")
matches = ip_address.findall(result.stdout)

for ip in matches:
    print(ip)




