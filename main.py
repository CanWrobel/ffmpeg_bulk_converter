import os
import subprocess

output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir('.'):
    if filename.lower().endswith('.mov'):
        input_path = os.path.join('.', filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp4")

        command = ['ffmpeg', '-i', input_path, '-vcodec', 'copy', '-acodec', 'copy', output_path]
        subprocess.run(command)

        print(f"Konvertierte {input_path} zu {output_path}")

print("done")
