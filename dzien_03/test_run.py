import subprocess
r1 = subprocess.run(["python", "-V"])

try:
    r2 = subprocess.run(["python", "-r"], capture_output=True)
except Exception as e:
    print(e)

print(r1)
