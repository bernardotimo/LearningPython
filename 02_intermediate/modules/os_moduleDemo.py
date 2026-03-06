# Used for interacting with OS
# Checks the current directory
# Lists available files
# Accesses environment variables
import os
print("\n=== CURRENT WORK DIRECTORY ===")

cwd = os.getcwd()
print("Current working directory: ", cwd)


print("\n=== CHANGING DIRECTORY ===")
#changing = os.chdir("demo_folder")
#print("Directory changed:", changing)


print("\n=== LIST FILES IN DIRECTORY ===")

files = os.listdir()
for file in files:
    print(file)

print("\n=== CREATE A NEW DIRECTORY ===")

new_folder = "demo_folder"
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print("Folder created:", new_folder)
else:
    print("Folder already exists")


print("\n=== CHECK IF FILE OR DIRECTORY EXISTS ===")

print("Does demo_folder exist?", os.path.isdir("demo_folder"))


print("\n=== PATH OPERATIONS ===")

# file_path = os.path.join(cwd, "example.txt")
# print("Joined path:", file_path)


print("\n=== FILE INFORMATION ===")

if os.path.exists("exmaple.txt"):
    print("File size:", os.path.getsize("exmaple.txt"), "bytes")
else:
    print("File doesn't exist")


print("\n=== RENAME A FILE ===")

# Example (only works if the file exists)
# os.rename("old_name.txt", "new_name.txt")


print("\n=== REMOVE A FILE ===")

# Example (be careful with this)
# os.remove("example.txt")


print("\n=== REMOVE A DIRECTORY ===")

# Only works if directory is empty
# os.rmdir("demo_folder")


print("\n=== ENVIRONMENT VARIABLES ===")

print("Home directory:", os.environ.get("HOME"))
print("Path variable:", os.environ.get("PATH"))