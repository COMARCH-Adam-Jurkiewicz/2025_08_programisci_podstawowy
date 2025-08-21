import subprocess
r1 = subprocess.run(["ls", "-la"])
r2 = subprocess.run(["ls", "-la"], capture_output=True)
print(dir(r))
print(r)