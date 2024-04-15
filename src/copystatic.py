import os
import shutil

def copy_file_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        full_source_path = os.path.join(source_dir, item)
        full_dest_path = os.path.join(dest_dir, item)
        print(f" * {full_source_path} -> {full_dest_path}")
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, full_dest_path)
        else:
            copy_file_recursive(full_source_path, full_dest_path)