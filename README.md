# Preprocessed-CMLR-Dataset-For-Wav2Lip

``` sh
python app.py
```

``` sh
python preprocess_cmlr.py --ngpu 1 --batch_size 32 --data_root /data/dev/dataset/CMLRdataset_output/ --preprocessed_root /data/dev/dataset/CMLRdataset_output/wav2lip/
```

> 3090 TI 使用 `--batch_size 32` 似乎合适。当然，也要考虑 CPU。
