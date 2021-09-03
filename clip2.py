# Importing the os library
import os
 
# The path for listing items
path = r"E:\File Server\My Files"
url = r"" 
# The list of items
files = os.listdir(path)
 
# Loop to print each filename separately
files = sorted(files)
for filename in files:
    filename = filename.replace(" ", "%20")
    fullname = url + filename
    print('"' + fullname + '",')