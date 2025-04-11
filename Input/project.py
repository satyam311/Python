import os

folders = input("Please provide list of folder name separated by comma:").split(',')
print(folders)

for folder in folders:
   try:
      files =  os.listdir(folder)
   except FileNotFoundError:
      print("please proide the valid folfer name:", folder )
      continue
   except PermissionError:
      print("No access to this folder",folder)
   print(files)
   for file in files:
      print(file)



