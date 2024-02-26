import os
import shutil

# 源目录
source_dir = "/data/dev/dataset/CMLRdataset_output/wav2lip"

# 目标目录
target_dir = "/data/dev/dataset/CMLRdataset_output/enhanced"

source_dir = source_dir.rstrip('/')
target_dir = target_dir.rstrip('/')

# 遍历源目录下的所有子目录和文件
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file == "audio.wav":
            source_file_path = os.path.join(root, file)
            target_subdir = root.replace(source_dir, "").lstrip("/")
            target_subdir_path = os.path.join(target_dir, target_subdir)
            os.makedirs(target_subdir_path, exist_ok=True)
            target_file_path = os.path.join(target_subdir_path, file)
            # shutil.copy(source_file_path, target_file_path)

if __name__ == "__main__":
    root = "/data/dev/dataset/CMLRdataset_output/wav2lip"
    source_file_path = "/data/dev/dataset/CMLRdataset_output/wav2lip/s1/20220202/section.1.2/audio.wav"
    target_subdir = root.replace(source_dir, "").lstrip("/")
    target_subdir_path = os.path.join(target_dir, target_subdir)
    target_file_path = os.path.join(target_subdir_path, "s1/20220202/section.1.2/audio.wav")
    print(target_subdir)
    print(target_subdir_path)
    print(target_file_path)
