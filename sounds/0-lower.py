import os

for i in os.listdir('./'):
    os.rename(i,i.lower().replace(' ','').replace('.mp3',''))
