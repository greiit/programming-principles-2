#1
import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)

path = r"C:\your\specified\path"
print("Directories:", list_directories(path))
print("Files:", list_files(path))
print("All Entries:", list_all(path))   

#2
import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

path = r"C:\your\specified\path" 
exists, readable, writable, executable = check_access(path)
print(f"Exists: {exists}, Readable: {readable}, Writable: {writable}, Executable: {executable}")

#3
import os

def path_details(path):
    if os.path.exists(path):
        directory_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        return directory_name, file_name
    else:
        return None, None

path = r"C:\your\specified\path"
directory_name, file_name = path_details(path)
if directory_name and file_name:
    print(f"Directory: {directory_name}, Filename: {file_name}")
else:
    print("Path does not exist.")

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = 'demofile.txt'  
print(f"Number of lines: {count_lines(file_path)}")

#5
def write_list_to_file(list_items, file_path):
    with open(file_path, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")

list_items = ['item1', 'item2', 'item3']  
file_path = 'demofile.txt'  
write_list_to_file(list_items, file_path)

#6
def generate_alphabet_files():
    for letter in range(65, 91):  
        with open(f"{chr(letter)}.txt", 'w') as file:
            file.write(f"This is the file for letter {chr(letter)}.")

generate_alphabet_files()

#7
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source:
        contents = source.read()
    with open(destination_path, 'w') as destination:
        destination.write(contents)

source_path = 'source_file.txt' 
destination_path = 'destination_file.txt' 
copy_file(source_path, destination_path)

#8
import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False

path = r"\your\specified\path" 
if delete_file(path):
    print("File deleted successfully.")
else:
    print("File cannot be deleted (might not exist or lack permissions).")


