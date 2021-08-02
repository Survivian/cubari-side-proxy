# Importing the os library
import os
 
# The path for listing items
path = r"D:/Everything Else/The Images/Eeveelution Maid Sets"
url = "http://192.168.1.92/The%20Images/Eeveelution%20Maid%20Sets/" 
# The list of items
files = os.listdir(path)
 
# Loop to print each filename separately
for filename in files:
    filename = filename.replace(" ", "%20")
    fullname = url + filename
    print('"' + fullname + '",')