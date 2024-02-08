import os
import glob
import zipfile
import subprocess

cmlr_dataset_dir = '/data/dev/dataset/CMLRdataset'
video_path = os.path.join(cmlr_dataset_dir, 'video')
audio_path = os.path.join(cmlr_dataset_dir, 'audio')

cmlr_dataset_output_dir = '/data/dev/dataset/CMLRdataset_output'
cmlr_dataset_video_output_dir = os.path.join(cmlr_dataset_output_dir, 'video')
cmlr_dataset_audio_output_dir = os.path.join(cmlr_dataset_output_dir, 'audio')
cmlr_dataset_sync_output_dir = os.path.join(cmlr_dataset_output_dir, 'sync')
os.makedirs(cmlr_dataset_video_output_dir, exist_ok=True)
os.makedirs(cmlr_dataset_audio_output_dir, exist_ok=True)
os.makedirs(cmlr_dataset_sync_output_dir, exist_ok=True)


def unpack():
    """解压"""
    for root, _, files in os.walk(video_path):
        for file in files:
            src_file = os.path.join(root, file)
            zip_file = zipfile.ZipFile(src_file, 'r')
            zip_file.extractall(cmlr_dataset_video_output_dir)
            zip_file.close()

    for root, _, files in os.walk(audio_path):
        for file in files:
            src_file = os.path.join(root, file)
            zip_file = zipfile.ZipFile(src_file, 'r')
            zip_file.extractall(cmlr_dataset_audio_output_dir)
            zip_file.close()


def sync():
    """合成"""
    for root, _, files in os.walk(cmlr_dataset_video_output_dir):
        for file in files:
            if file.endswith('.mp4'):
                print(os.path.join(root, file))
                src_video_file = os.path.join(root, file)
                src_aideo_file = os.path.join(root.replace('video', 'audio'), file.replace('.mp4', '.wav'))
                dst_sync_file = os.path.join(cmlr_dataset_sync_output_dir, file)
                subprocess.run(['ffmpeg',
                                '-i', src_video_file,
                                '-i', src_aideo_file,
                                '-c:v', 'copy',
                                '-c:a', 'aac', "-b:a", "192k",
                                dst_sync_file],
                               check=False)


if __name__ == '__main__':
    unpack()
    # 不需要调用 sync() 将音频合成到 mp4。请用 preprocess_cmlr.py 进行预处理。
    video_filelist = glob.glob(os.path.join(cmlr_dataset_video_output_dir, '*/*/*.mp4'))
    audio_filelist = glob.glob(os.path.join(cmlr_dataset_audio_output_dir, '*/*/*.wav'))
    print(f'视频数量：{len(video_filelist)}')
    print(f'音频数量：{len(audio_filelist)}')
