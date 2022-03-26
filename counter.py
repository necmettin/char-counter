chars = {}
extensions = []
nontext_extensions = ['.woff2', '.png', '.gif', '.pyc', '.tif', '.woff', '.ttf', '.pdf', '.lock', '.jpeg', '.db', '.z', '.zip', '.eot', '.pxm', '.icc', '.ico', '.otf', '.ser', '.xlsx', '.pem', '.jpg', '.docx', '.0', '.map', '.sln']
discarded_folders = [".git", "node_modules", ".vscode"]

import glob
import os
import sys
import operator

filenames = glob.glob("../**/*", recursive=True)
print(f"Counting characters in {len(filenames)} files")

for filename in filenames:
	if os.path.isfile(filename) and filename not in discarded_folders:
		extension = os.path.splitext(filename)[1]
		extensions.append(extension)
		if extension not in nontext_extensions:
			try:
				with open(filename, "r") as opened:
					contents = opened.read()
				for char in contents:
					if char in chars.keys():
						chars[char] += 1
					else:
						chars[char] = 1
			except:
				pass

sorted_x = sorted(chars.items(), key=operator.itemgetter(1), reverse=1)
sorted_x = sorted_x[0:299]

for x in sorted_x:
	print(x)
