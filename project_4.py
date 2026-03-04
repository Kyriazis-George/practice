# import os

# def main():
#     folder = "xzy"
#     for count, filename in enumerate(os.listdir(folder)):
#         dst = f"Picture {str(count)}.jpg"
#         src = f"{folder}/{filename}"
#         dst = f"{folder}/{dst}"

#         os.rename(src.dst)

# if __name__== '__main__':
#     main()        

# import os
# import glob

# def rename_files(directory, pattern, new_base_name):
    
#     if not os.path.isdir(directory):
#         print("Error: This directory does not exist")
#         return
    
#     files = glob.glob(os.path.join(directory,pattern))
#     if not files:
#         print("no files matching the pattern.")
#         return
#     print(f"\nFound {len(files)} files(s) to rename: \n")
#     for f in files:
#         print(os.path.basename(f))

#     print("\nRenaming files....\n")
#     for i, old_path in enumerate(files, start=1):
#         ext = os.path.splitext(old_path)[1]
#         new_name = f"{new_base_name}{i}{ext}"
#         new_path = os.path.join(directory, new_name)
#         os.rename(old_path, new_path)
#     print("\n All files renames successfully!")

# if __name__ == "__main__":
#     directory = input("Enter directory path: ").strip()
#     pattern = input("Enter file pattern").strip()
#     new_base_name = input("enter new base name").strip()            


import os
import glob

directory = input("Enter directory path: ").strip()
pattern = input("Enter file pattern (e.g. *.jpg): ").strip()
new_base_name = input("Enter new base name (e.g. photo_): ").strip()

files = glob.glob(os.path.join(directory, pattern))
print("\nFound files:")
print(files)

if not files:
    print("\n No files found. Check your pattern and directory path.")
else:
    for i, old_path in enumerate(files, start=1):
        ext = os.path.splitext(old_path)[1]
        new_name = f"{new_base_name}{i}{ext}"
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {os.path.basename(old_path)} → {new_name}")
        