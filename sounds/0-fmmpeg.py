import os

for element in os.listdir('./'):
    if element.endswith('.mp3'):
        print(element)
        os.system("ffmpeg -i "+element+" -acodec libopus -b:a 55000 -vbr on -compression_level 10 "+element.replace("mp3",'opus'))
