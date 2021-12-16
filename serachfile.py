import os

def find_files(filename, search_path):
   flag=0
   for root, dir, files in os.walk(search_path):
      if filename in files:
         return os.path.join(root, filename)
         flag=1
   if flag==0:
       return "file not found"
       
      


filename=input("Enter File Name :")
search_path=input("Enter Path Where you want to search file :")
print(find_files(filename,search_path))
