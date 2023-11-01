import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def copy_file(src_path, dest_path):
    shutil.copy2(src_path, dest_path)
    print(f"Copied: {src_path} to {dest_path}")

def copy_firmwares(src_directory, dest_directory):
    uf2_files = []
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(src_directory):
            for file in files:
                if file.endswith(".uf2"):
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_directory, file)
                    
                    uf2_files.append(file.replace(".uf2", ""))
                    executor.submit(copy_file, src_path, dest_path)

    return uf2_files

def copy_examples(src_directory, dest_directory, uf2_files):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(src_directory):
            if '.git' in root or '.github' in root or 'build' in root:
                continue
            dir_name = os.path.basename(root)
            if dir_name in uf2_files and ('CMakeLists.txt' in files):
                rel_path = os.path.relpath(root, src_directory)
                dest_path = os.path.join(dest_directory, rel_path)
                
                executor.submit(shutil.copytree, root, dest_path, dirs_exist_ok=True)
                print(f"Copied example directory: {root} to {dest_path}")

if __name__ == "__main__":
    uf2_files = copy_firmwares("/pico-examples/build", "/workspace/firmware")
    copy_examples("/pico-examples", "/workspace/examples", uf2_files)
