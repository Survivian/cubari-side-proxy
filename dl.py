# Needed imports
import subprocess
url = "https://kemono.party/patreon/user/5919535"
subprocess.run(["gallery-dl", '-d', 'D:\Everything Else', url, '--zip'], shell=True)