# Preprocessed-CMLR-Dataset-For-Wav2Lip

## 解压

``` sh
python app.py
```

## Wav2lip 预处理

将 `preprocess_cmlr.py` 复制到 `Wav2lip` 目录。

``` sh
python preprocess_cmlr.py --ngpu 1 --batch_size 32 --data_root /data/dev/dataset/CMLRdataset_output/ --preprocessed_root /data/dev/dataset/CMLRdataset_output/wav2lip/
```

> 3090 TI 使用 `--batch_size 32` 似乎合适。当然，也要考虑 CPU。

## 超分

将 `inference.py` 复制到 `CodeFormer` 目录。

目录：/data/dev/dataset/CMLRdataset_output/wav2lip/s9/20120904/section_4_002/
输出：/data/dev/dataset/CMLRdataset_output/enhanced/s9/20120904/section_4_002/

``` sh
cd /data/dev/CodeFormer/
python inference.py --upscale 1 -w 1.0 --input_path /data/dev/dataset/CMLRdataset_output/wav2lip/ --output_path /data/dev/dataset/CMLRdataset_output/enhanced/
```

本地测试：

``` sh
cd /Users/alby/Workspace/OpenSource/ML/wav2lip/CodeFormer/
python inference.py --upscale 1 -w 1.0 --input_path /Users/alby/Workspace/section_4_003/ --output_path /Users/alby/Workspace/section_4_003-1/
```
