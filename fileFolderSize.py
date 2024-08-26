import os
from concurrent.futures import ThreadPoolExecutor

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def process_folder(folder):
    return folder, get_folder_size(folder)

def get_sorted_folders_by_size(base_folder):
    folders = [os.path.join(base_folder, folder) for folder in os.listdir(base_folder) if
               os.path.isdir(os.path.join(base_folder, folder))]
    with ThreadPoolExecutor() as executor:
        folder_sizes = list(executor.map(process_folder, folders))
    folder_sizes.sort(key=lambda x: x[1], reverse=True)
    return folder_sizes

if __name__ == "__main__":
    folder_path = input("请输入文件夹路径：")
    sorted_folders = get_sorted_folders_by_size(folder_path)

    print("文件夹大小排序：")
    for folder, size in sorted_folders:
        print(f"{folder}: {size / (1024 * 1024):.2f} MB")
