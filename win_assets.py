import sys
import os

argc = len(sys.argv)

if argc != 3:
    print("Usage: python win_assets.py <path> <starting number>")
    sys.exit()

path = sys.argv[1]

# Check if path ends with a slash
if path[-1] != "/":
    path += "/"

num = int(sys.argv[2])

dir_list = os.listdir(path)

# Check if the directory is empty
if len(dir_list) == 0:
    print("Directory is empty")
    sys.exit()

for file in dir_list:
    # Rename the file
    os.rename(path + file, path + str(num) + ".png")
    num += 1
