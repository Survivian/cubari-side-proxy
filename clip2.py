# Importing the os library
import os
 
# The path for listing items
path = r"D:\Everything Else\The Images\Tojyo Patreon"
url = r"http://66.168.178.255/The%20Images/Tojyo%20Patreon/" 
# The list of items
files = os.listdir(path)
 
# Loop to print each filename separately
files = sorted(files)
for filename in files:
    filename = filename.replace(" ", "%20")
    fullname = url + filename
    print('"' + fullname + '",')