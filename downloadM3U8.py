# command line to download m3u8 video file
import os
file = open("m3u8url")
X = file.readlines()
file.close()


def download(url, n):
    folder = '/xxx/video/'
    file = folder+'v'+str(n)+".mp4"
    new_file = folder+'v'+str(n+1)+".mp4"
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(file):
        cmd = "ffmpeg -i "+url.strip("\n")+" "+file
        print(cmd)
        os.system(cmd)
    else:
        cmd = "ffmpeg -i " + url.strip("\n") + " " + new_file
        print(cmd)
        os.system(cmd)


n = 0
for url in X:
    download(url, n)
    n = n + 1

print("download done.")


