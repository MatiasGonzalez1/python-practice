import pytube

link = input('Enter YOUTUBE Video URL')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('download', link)