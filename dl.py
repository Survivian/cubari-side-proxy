# Needed imports
import subprocess
url = "https://kemono.party/patreon/user/10734570/post/51222189"
subprocess.run(["gallery-dl", '-d', 'D:\Everything Else', url, '--zip'], shell=True)