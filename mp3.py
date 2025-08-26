import os
import subprocess

def extract_audio_folder(input_folder, output_folder):
    ffmpeg_path = r'C:\tools\ffmpeg\bin\ffmpeg.exe'  # ffmpeg.exe 경로

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp4', '.mov')):
            input_path = os.path.join(input_folder, filename)
            base_filename = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, base_filename + '.mp3')

            command = [
                ffmpeg_path,
                '-i', input_path,
                '-vn',
                '-acodec', 'libmp3lame',
                '-b:a', '192k',   # 192kbps 권장 (필요하면 320k로 변경 가능)
                output_path
            ]
            print(f"MP3 변환 중: {filename} -> {base_filename}.mp3")
            subprocess.run(command, check=True)

    print("✅ 모든 MP3 변환 완료!")

# 예시
input_folder = r'C:\Users\games\Videos\vids'
output_folder = r'C:\Users\games\Music\audios'
extract_audio_folder(input_folder, output_folder)
