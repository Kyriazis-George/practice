import os
import glob

directory = r"C:\\Users\\kyria\\Pictures\\me playing"
pattern = "*.jpeg"
new_base_name = "Stage_1"

files = glob.glob(os.path.join(directory, pattern))
files.sort()

print("\nFound files:")
print(files)

if not files:
    print("\nNo files found. Check your pattern and directory path.")
else:
    for i, old_path in enumerate(files, start=1):
        ext = os.path.splitext(old_path)[1]
        new_name = f"{new_base_name}{i}{ext}"
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {os.path.basename(old_path)} → {new_name}")