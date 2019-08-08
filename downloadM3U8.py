# command line to download m3u8 video file
import os
file = open("m3u8url") # read m3u8 link list from this file
X = file.readlines()
file.close()


def download(url, n):
    cmd = "ffmpeg -i "+url.strip("\n")+" /xxx/video/v"+str(n)+".mp4"
    print(cmd)
    os.system(cmd)
    print("download done.")


n = 0
for url in X:
    download(url, n)
    n = n + 1


