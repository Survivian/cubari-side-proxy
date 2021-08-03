# Importing the os library
import os
 
# The path for listing items
path = r"D:\Everything Else\The Images\Pennys Problem"
url = r"http://66.168.178.255/The%20Images/Pennys%20Problem/" 
# The list of items
files = os.listdir(path)
 
# Loop to print each filename separately
files = sorted(files)
for filename in files:
    filename = filename.replace(" ", "%20")
    fullname = url + filename
    print('"' + fullname + '",')