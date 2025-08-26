import os
import subprocess

def extract_audio_folder(input_folder, output_folder):
    ffmpeg_path = r'C:\tools\ffmpeg\bin\ffmpeg.exe'

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp4', '.mov')):
            input_path = os.path.join(input_folder, filename)
            base_filename = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, base_filename + '.flac')

            command = [
                ffmpeg_path,
                '-i', input_path,
                '-vn',
                '-acodec', 'flac',
                output_path
            ]
            print(f"FLAC 변환 중: {filename} -> {base_filename}.flac")
            subprocess.run(command, check=True)

    print("✅ 모든 FLAC 변환 완료!")

# 예시
input_folder = r'C:\Users\games\Videos\vids'
output_folder = r'C:\Users\games\Music\audios'
extract_audio_folder(input_folder, output_folder)
