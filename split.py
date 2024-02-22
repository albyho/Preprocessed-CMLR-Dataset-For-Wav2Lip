import os
import random

# 定义目录和文件路径
data_dir = '/data/dev/dataset/CMLRdataset_output/enhanced/'
output_dir = '/data/dev/enhanced_wav2lip/filelists/'
train_file = os.path.join(output_dir, 'train.txt')
test_file = os.path.join(output_dir, 'test.txt')

# 获取最后一级子目录
last_level_subdirs = []
for root, dirs, files in os.walk(data_dir):
    for d in dirs:
        if 'section' in d:
            last_level_subdirs.append(os.path.join(root, d))

# 打乱文件列表
random.shuffle(last_level_subdirs)

# 定义训练集、测试集和验证集的比例
train_ratio = 0.8
test_ratio = 0.2

# 计算文件数量
num_files = len(last_level_subdirs)
num_train = int(num_files * train_ratio)
num_test = int(num_files * test_ratio)

# 将文件分割成训练集、测试集和验证集
train_files = last_level_subdirs[:num_train]
test_files = last_level_subdirs[num_train:num_train+num_test]

# 写入训练集文件名到txt文件
with open(train_file, 'w', encoding='utf-8') as f:
    for filename in train_files:
        f.write(filename + '\n')

# 写入测试集文件名到txt文件
with open(test_file, 'w', encoding='utf-8') as f:
    for filename in test_files:
        f.write(filename + '\n')

print("Split information written to", train_file, test_file)
